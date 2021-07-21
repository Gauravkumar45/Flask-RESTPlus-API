import datetime
import jwt
from main.model.blacklist import BlacklistToken
from ..config import key
import os
from .. import db, flask_bcrypt

basedir = os.path.abspath(os.path.dirname(__file__))

#The owners class inherits from db.Model class which declares the class as a model for sqlalchemy.
class Owners(db.Model):
    """ User Model for storing owners related details """
    __tablename__ = "owners"
    #line 15 through 35 creates the required columns for the owner table.
    ownerid = db.Column(db.Integer,primary_key=True, nullable=False,autoincrement=True)
    ownername = db.Column(db.String(50))
    address1 = db.Column(db.String(50))
    address2 = db.Column(db.String(50))
    pan = db.Column(db.String(50))
    aadhar = db.Column(db.String(50))
    mobile = db.Column(db.String(50))
    gst = db.Column(db.String(50))
    startdate = db.Column(db.DateTime, default=datetime.datetime.now())
    enddate = db.Column(db.DateTime, default=datetime.datetime.now())
    dlno = db.Column(db.String(50))
    isactive = db.Column(db.Boolean,  default=False, server_default="true")
    status = db.Column(db.String(50))
    statuschangedate = db.Column(db.DateTime, default=datetime.datetime.now())
    stateid = db.Column(db.Integer)
    state = db.Column(db.String(50))
    pincode = db.Column(db.String(50))
    bankname = db.Column(db.String(50))
    accountno = db.Column(db.String(50))
    ifsc = db.Column(db.String(50))
    transportercode = db.Column(db.String(50))

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
        return "<Owner '{}'>".format(self.username)

# Encoding tokens
def encode_auth_token(self, ownerid):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': ownerid
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

