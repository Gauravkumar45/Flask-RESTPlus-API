import datetime
import jwt
from main.model.blacklist import BlacklistToken
from ..config import key
import os
from .. import db, flask_bcrypt

basedir = os.path.abspath(os.path.dirname(__file__))

#The outgate class inherits from db.Model class which declares the class as a model for sqlalchemy.
class Outgate(db.Model):
    """ outgate Model for storing user related details """
    __tablename__ = "outgate"
    #line 15 through 45 creates the required columns for the outgate table.
    challanid = db.Column(db.Integer, primary_key=True, nullable=False,autoincrement=True)
    slipno = db.Column(db.String(100))
    slipid = db.Column(db.Integer)
    vehicleno = db.Column(db.String(100))
    driver = db.Column(db.String(100))
    driverid = db.Column(db.Integer)
    loading = db.Column(db.String(100))
    destination = db.Column(db.String(100))
    challanno = db.Column(db.String(100))
    gross = db.Column(db.Integer)
    tare = db.Column(db.Integer)
    net = db.Column(db.Integer)
    passdate = db.Column(db.DateTime, default=datetime.datetime.now())
    passgate = db.Column(db.String(50))
    sliptime = db.Column(db.DateTime, default=datetime.datetime.now())
    challantime = db.Column(db.DateTime, default=datetime.datetime.now())
    printtime = db.Column(db.DateTime, default=datetime.datetime.now())
    material = db.Column(db.String(50))
    weighbridge = db.Column(db.String(50))
    vehicleid = db.Column(db.Integer)
    locationid = db.Column(db.Integer)
    username = db.Column(db.String(50))
    transporterid = db.Column(db.Integer)
    transporter = db.Column(db.String(50))
    challannet = db.Column(db.Integer)
    grosswbid = db.Column(db.Integer)
    grosswb = db.Column(db.String(50))
    tarewbid = db.Column(db.Integer)
    tarewb = db.Column(db.String(50))
    passusername = db.Column(db.String(50))
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
        return "<Outgate '{}'>".format(self.slipno)

# Encoding tokens
def encode_auth_token(self, challanid):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': challanid
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