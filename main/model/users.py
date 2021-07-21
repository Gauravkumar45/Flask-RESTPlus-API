import uuid
import datetime
import jwt
from main.model.blacklist import BlacklistToken
from ..config import key
import os
from .. import db, flask_bcrypt
from sqlalchemy.dialects.postgresql import JSON

basedir = os.path.abspath(os.path.dirname(__file__))

#users class inherits from db.Model class which declares the class as a model for sqlalchemy.
class Users(db.Model):
    """ Users Model for storing users related details """
    __tablename__ = "Users"
    
    # line 18 through 32 creates the required columns for the users table.
    UserId = db.Column(db.Integer, primary_key=True, nullable=False,autoincrement=True)
    Username = db.Column(db.String(100))
    DisplayName = db.Column(db.String(100))
    Email = db.Column(db.String(100))
    Source = db.Column(db.String(4))
    PasswordHash = db.Column(db.String(86))
    PasswordSalt = db.Column(db.String(10))
    LastDirectoryUpdate = db.Column(db.DateTime, default=datetime.datetime.now())
    UserImage = db.Column(db.String(100))
    InsertDate = db.Column(db.DateTime, default=datetime.datetime.now())
    InsertUserId = db.Column(db.Integer)
    UpdateDate = db.Column(db.DateTime, default=datetime.datetime.now())
    UpdateUserId = db.Column(db.Integer)
    IsActive = db.Column(db.Integer)
    Password = db.Column(db.String(50))

    @property
    def password(self):
        raise AttributeError('password: write-only field')

#a setter for the field password_hash and it uses flask-bcryptto generate a hash using the provided password
    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

#compares a given password with already savedpassword_hash.
    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<Users '{}'>".format(self.username)

# Encoding tokens
def encode_auth_token(self, userid):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': userid
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