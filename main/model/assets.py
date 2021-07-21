import datetime
import jwt
from main.model.blacklist import BlacklistToken
from ..config import key
import os
from .. import db, flask_bcrypt

basedir = os.path.abspath(os.path.dirname(__file__))

#The assets class inherits from db.Model class which declares the class as a model for sqlalchemy.
class Assets(db.Model):
    """ Assets Model for storing Assets related details """
    __tablename__ = "assets"
    
    #line 16 through 28 creates the required columns for the assets table.
    assetid = db.Column(db.Integer, primary_key=True, nullable=False,autoincrement=True)
    assetname = db.Column(db.String(100))
    category = db.Column(db.String(100))
    make = db.Column(db.String(100))
    model = db.Column(db.String(100))
    serialno = db.Column(db.String(100))
    location = db.Column(db.String(100))
    installationdate = db.Column(db.DateTime, default=datetime.datetime.now())
    assetcode = db.Column(db.String(100))
    status = db.Column(db.String(100))
    statuschangedate = db.Column(db.DateTime, default=datetime.datetime.now())
    categoryid = db.Column(db.Integer)
    locationid = db.Column(db.Integer)

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
        return "<Assets '{}'>".format(self.assetname)

#Encoding tokens
def encode_auth_token(self, assetid):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': assetid
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