import datetime
import jwt
from main.model.blacklist import BlacklistToken
from ..config import key
import os
from .. import db, flask_bcrypt

basedir = os.path.abspath(os.path.dirname(__file__))

# The drivers class inherits from db.Model class which declares the class as a model for sqlalchemy.
class Drivers(db.Model):
    """ User Model for storing drivers related details """
    __tablename__ = "drivers"
    #line 15 through 26 creates the required columns for the drivers table.
    driverid = db.Column(db.Integer,primary_key=True, nullable=False,autoincrement=True)
    drivername = db.Column(db.String(50))
    dlno = db.Column(db.String(50))
    dltype = db.Column(db.String(50))
    address = db.Column(db.String(50))
    dlexpiry = db.Column(db.DateTime, default=datetime.datetime.now())
    isactive = db.Column(db.Boolean, default=False, server_default="true")
    drivermobile = db.Column(db.String(50))
    fingerprint = db.Column(db.String(50))
    faceprint = db.Column(db.String(50))
    status = db.Column(db.String(50))
    statuschangedate = db.Column(db.DateTime, default=datetime.datetime.now())

    @property
    def password(self):
        raise AttributeError('password: write-only field')

#a setter for the field password_hash and it uses flask-bcryptto generate a hash using the provided password.
    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

#compares a given password with already savedpassword_hash.
    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<Drivers '{}'>".format(self.username)

# Encoding tokens
def encode_auth_token(self, driverid):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': driverid
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            return e

#Decoding: Blacklisted token, expired token and invalid token are taken into consideration while decoding the authentication token.
@staticmethod  
def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, key)
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

