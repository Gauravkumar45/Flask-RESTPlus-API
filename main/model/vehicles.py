import datetime
import jwt
from main.model.blacklist import BlacklistToken
from ..config import key
import os
from .. import db, flask_bcrypt

basedir = os.path.abspath(os.path.dirname(__file__))

#The vehicles class inherits from db.Model class which declares the class as a model for sqlalchemy.
class Vehicles(db.Model):
    """ vehicles Model for storing vehicles related details """
    __tablename__ = "vehicles"
    #line 15 through 51 creates the required columns for the vehicles table.
    vehicleid = db.Column(db.Integer,primary_key=True,nullable=False,autoincrement=True )
    vehicleno = db.Column(db.String(50))
    compliant = db.Column(db.Integer)
    ownerid = db.Column(db.Integer)
    ownername = db.Column(db.String(50))
    ownermobile = db.Column(db.String(50))
    rcno = db.Column(db.String(50))
    tempno = db.Column(db.String(50))
    chasisno = db.Column(db.String(50))
    fitnessexpiry = db.Column(db.DateTime, default=datetime.datetime.now())
    insuranceexpiry = db.Column(db.DateTime, default=datetime.datetime.now())
    permitexpiry = db.Column(db.DateTime, default=datetime.datetime.now())
    pollutionexpiry = db.Column(db.DateTime, default=datetime.datetime.now())
    permittype = db.Column(db.String(50))
    status = db.Column(db.String(50))
    statuschangedate = db.Column(db.DateTime, default=datetime.datetime.now())
    createdate = db.Column(db.DateTime, default=datetime.datetime.now())
    ownerpan = db.Column(db.String(50))
    rfno = db.Column(db.String(50))
    permit = db.Column(db.String(50))
    insurance = db.Column(db.String(50))
    pollution = db.Column(db.String(50))
    fitness = db.Column(db.String(50))
    isactive = db.Column(db.Boolean,  default=True, server_default="true")
    roadtax = db.Column(db.String(50))
    roadtaxexpiry = db.Column(db.DateTime, default=datetime.datetime.now())
    rcdate = db.Column(db.DateTime, default=datetime.datetime.now())
    wheeler = db.Column(db.Integer)
    vowner = db.Column(db.String(50))
    vcontact = db.Column(db.String(50))
    vaddress = db.Column(db.String(50))
    vownership = db.Column(db.Boolean, default=False, server_default="false")
    gpsdate = db.Column(db.DateTime, default=datetime.datetime.now())
    gpsno = db.Column(db.String(50))
    imeino = db.Column(db.String(50))
    modelno = db.Column(db.String(50))
    engine = db.Column(db.String(50))

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
        return "<Vehicles '{}'>".format(self.username)

# Encoding tokens
def encode_auth_token(self, vehicleid):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': vehicleid
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