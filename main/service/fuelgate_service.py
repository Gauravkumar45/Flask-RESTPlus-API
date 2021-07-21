from flask import  request, jsonify
from main import db
import uuid
from main.model.fuelgate import Fuelgate

# insert the data in fuelgate database
def save_new_user(data):
    user = Fuelgate.query.filter_by(vehicleno=data['vehicleno']).first()
    if not user:
        new_user = Fuelgate(
            vehicleno=data['vehicleno'],slipno=data['slipno'], challanno=data['challanno'],quantity=data['quantity'],vehicleid=data['vehicleid'],
            fuelslipno=data['fuelslipno'],username=data['username'],slipid=data['slipid'],transporter=data['transporter'],
            transporterid=data['transporterid'],location=data['location'],locationid=data['locationid'],wheeler=data['wheeler'],driver=data['driver']
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Fuelgate Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Fuelgate already exists. Please Log in.',
        }
        return response_object, 409

# get the all data from fuelgate table
def get_all_users():
    return Fuelgate.query.all()

# get the one data from fuelgate table
def get_a_user(fuelid):
    return Fuelgate.query.filter_by(fuelid=fuelid).first()

# update the data from fuelgate table
def complete_users(fuelid):
  user = Fuelgate.query.filter_by(fuelid=fuelid).first()

  if not user:
    return jsonify({'message' : 'No Fuelgate found!'})

  vehicleno = request.json['vehicleno']
  slipno = request.json['slipno']
  challanno = request.json['challanno']
  quantity = request.json['quantity']
  vehicleid = request.json['vehicleid']
  fuelslipno = request.json['fuelslipno']
  username = request.json['username']
  slipid = request.json['slipid']
  transporter = request.json['transporter']
  transporterid = request.json['transporterid']
  location = request.json['location']
  locationid = request.json['locationid']
  wheeler = request.json['wheeler']
  driver = request.json['driver']
  driverid = request.json['driverid']

  user.vehicleno = vehicleno
  user.slipno = slipno
  user.challanno = challanno
  user.quantity = quantity
  user.vehicleid = vehicleid
  user.fuelslipno = fuelslipno
  user.username = username
  user.slipid = slipid
  user.transporter = transporter
  user.location = location
  user.locationid = locationid
  user.wheeler = wheeler
  user.driver = driver
  user.driverid = driverid
  db.session.commit()
  return jsonify('Fuelgate update completed')

# delete the data from fuelgate table
def delete_user(fuelid):  
    user = Fuelgate.query.filter_by(fuelid=fuelid).first()   
    if not user:   
       return jsonify({'message': 'Fuelgate does not exist'})   

    db.session.delete(user)  
    db.session.commit()   

    return jsonify({'message': 'Fuelgate Successfully deleted'})

# commits the changes to database.
def save_changes(data):
    db.session.add(data)
    db.session.commit()


def generate_token(Fuelgate):
    try:
        # generate the auth token
        auth_token = Fuelgate.encode_auth_token(Fuelgate.fuelid)
        response_object = {
            'status': 'success',
            'message': 'Fuelgate Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return generate_token(Fuelgate)
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401
