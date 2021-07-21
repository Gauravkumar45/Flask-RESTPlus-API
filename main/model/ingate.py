import datetime
import jwt
from main.model.blacklist import BlacklistToken
from ..config import key
import os
from .. import db, flask_bcrypt

basedir = os.path.abspath(os.path.dirname(__file__))

#The ingate class inherits from db.Model class which declares the class as a model for sqlalchemy.
class Ingate(db.Model):
    """ User Model for storing ingate related details """
    __tablename__ = "ingate"
    #line 15 through 38 creates the required columns for the ingate table.
    slipid = db.Column(db.Integer,primary_key=True,nullable=False,autoincrement=True)
    sliptime = db.Column(db.DateTime, default=datetime.datetime.now())
    vehicleno = db.Column(db.String(50))
    destination = db.Column(db.String(50))
    loading = db.Column(db.String(50))
    dlno = db.Column(db.String(50))
    transporter = db.Column(db.String(50))
    gate = db.Column(db.String(50))
    currentlogin = db.Column(db.String(50))
    driver = db.Column(db.String(50))
    controlno = db.Column(db.Integer)
    driverid = db.Column(db.Integer)
    tare = db.Column(db.Integer)
    rfid = db.Column(db.Integer)
    rfno = db.Column(db.String(50))
    locationid = db.Column(db.Integer)
    transporterid = db.Column(db.Integer)
    vehicleid = db.Column(db.Integer)
    validslip = db.Column(db.Boolean, default=False, server_default="false")
    slipno = db.Column(db.String(50))
    quantity = db.Column(db.Integer)
    fueltime = db.Column(db.DateTime, default=datetime.datetime.now())
    fueloperator = db.Column(db.String(50))
    wheeler = db.Column(db.Integer)

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
        return "<Ingate '{}'>".format(self.username)

# Encoding tokens
def encode_auth_token(self, slipid):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': slipid
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
