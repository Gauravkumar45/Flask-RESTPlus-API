import datetime
import jwt
from main.model.blacklist import BlacklistToken
from ..config import key

from .. import db, flask_bcrypt

#The railwaysiding class inherits from db.Model class which declares the class as a model for sqlalchemy.
class Railwaysiding(db.Model):
    """ railwaysiding Model for storing railwaysiding related details """
    __tablename__ = "railwaysiding"
    #line 13 through 33 creates the required columns for the railwaysiding table.
    entryid = db.Column(db.Integer,primary_key=True,nullable=False,autoincrement=True)
    vehicleno = db.Column(db.String(50))
    grosswb = db.Column(db.String(50))
    gross = db.Column(db.Integer)
    tarewb = db.Column(db.String(10))
    tare = db.Column(db.Integer)
    net = db.Column(db.Integer)
    entrytime = db.Column(db.DateTime, default=datetime.datetime.now())
    shortage = db.Column(db.Integer)
    exittime =  db.Column(db.DateTime, default=datetime.datetime.now())
    remarks = db.Column(db.String(50))
    vehicleid = db.Column(db.Integer)
    challannet = db.Column(db.Integer)
    challanno = db.Column(db.String(50))
    slipno = db.Column(db.String(50))
    grosswbid = db.Column(db.Integer)
    tarewbid = db.Column(db.Integer)
    usergross = db.Column(db.String(50))
    usertare = db.Column(db.String(50))
    userexit = db.Column(db.String(50))
    wbdatetime = db.Column(db.DateTime, default=datetime.datetime.now())

    @property
    def password(self):
        raise AttributeError('password: write-only field')

# a setter for the field password_hash and it uses flask-bcryptto generate a hash using the provided password.
    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

#compares a given password with already savedpassword_hash.
    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<Railwaysiding '{}'>".format(self.vehicleno)

# Encoding tokens
def encode_auth_token(self, entryid):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': entryid
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