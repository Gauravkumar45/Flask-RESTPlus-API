import uuid
import datetime
from flask import request, jsonify
from main import db
from main.model.drivers import Drivers

# insert the data in drivers table
def save_new_user(data):
    user = Drivers.query.filter_by(driverid=data['driverid']).first()
    if not user:
        new_user = Drivers(
            drivername=data['drivername'],
            dlno=data['dlno'],
            dltype=data['dltype'],
            dlexpiry=datetime.datetime.utcnow(),
            isactive=data['isactive'],
            drivermobile=data['drivermobile'],
            fingerprint=data['fingerprint'],
            faceprint=data['faceprint'],
            status=data['status'],
            statuschangedate=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Drivers Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'drivers already exists. Please Log in.',
        }
        return response_object, 409

# get the all data in drivers table
def get_all_users():
    return Drivers.query.all()

# get the one data in drivers table
def get_a_user(driverid):
    return Drivers.query.filter_by(driverid=driverid).first()

# update the data in drivers table
def complete_drivers(driverid):
  user = Drivers.query.filter_by(driverid=driverid).first()

  if not user:
    return jsonify({'message' : 'No drivers found!'})

  drivername = request.json['drivername']
  dlno = request.json['dlno']
  dltype = request.json['dltype']
  address = request.json['address']
  drivermobile = request.json['drivermobile']
  fingerprint = request.json['fingerprint']
  faceprint = request.json['faceprint']
  status = request.json['status']

  user.drivername = drivername
  user.dlno = dlno
  user.dltype = dltype
  user.address = address
  user.drivermobile = drivermobile
  user.fingerprint = fingerprint
  user.faceprint = faceprint
  user.status = status
  db.session.commit()
  return jsonify('Drivers Successfully Update')

# delete the data in drivers table
def delete_drivers(driverid):  
    user = Drivers.query.filter_by(driverid=driverid).first()   
    if not user:   
      return jsonify({'message': 'drivers does not exist'})   

    db.session.delete(user)  
    db.session.commit()   

    return jsonify({'message': 'Drivers Successfully Deleted'})

#commits the changes to database.
def save_changes(data):
    db.session.add(data)
    db.session.commit()


def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Drivers Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return generate_token(user)
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401