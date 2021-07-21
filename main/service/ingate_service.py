import uuid
import datetime
from flask import Flask, request, jsonify
from main import db
from main.model.ingate import Ingate

# insert the data from ingate table 
def save_new_ingate(data):
    user = Ingate.query.filter_by(vehicleno=data['vehicleno']).first()
    if not user:
        new_user = Ingate(
           vehicleno=data['vehicleno'],sliptime=datetime.datetime.utcnow(),destination=data['destination'],loading=data['loading'],dlno=data['dlno'],transporter=data['transporter'],
            gate=data['gate'],currentlogin=data['currentlogin'],driver=data['driver'],controlno=data['controlno'],driverid=data['driverid'],
            tare=data['tare'],rfid=data['rfid'],rfno=data['rfno'],locationid=data['locationid'],transporterid=data['transporterid'],vehicleid=data['vehicleid'],
            slipno=data['slipno'],quantity=data['quantity'],fueltime=datetime.datetime.utcnow(),fueloperator=data['fueloperator'],wheeler=data['wheeler']
            
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Ingate Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Ingate already exists. Please Log in.',
        }
        return response_object, 409

# get the all data from ingate table
def get_all_ingate():
    return Ingate.query.all()

# get the one data from inagte table
def get_a_ingate(slipid):
    return Ingate.query.filter_by(slipid=slipid).first()

# update the data from ingate table 
def complete_ingate(slipid):
  user = Ingate.query.filter_by(slipid=slipid).first()

  if not user:
        return jsonify({'message' : 'No ingate-user found!'})

  vehicleno = request.json['vehicleno']
  destination = request.json['destination']
  loading = request.json['loading']
  dlno = request.json['dlno']
  transporter = request.json['transporter']
  gate = request.json['gate']
  currentlogin = request.json['currentlogin']
  driver = request.json['driver']
  controlno = request.json['controlno']
  driverid = request.json['driverid']
  tare = request.json['tare']
  rfid = request.json['rfid']
  rfno = request.json['rfno']
  locationid = request.json['locationid']
  transporterid = request.json['transporterid']
  vehicleid = request.json['vehicleid']
  slipno = request.json['slipno']
  quantity = request.json['quantity']
  fueloperator = request.json['fueloperator']
  wheeler = request.json['wheeler']

  user.vehicleno = vehicleno
  user.destination = destination
  user.loading = loading
  user.dlno = dlno
  user.transporter = transporter
  user.gate = gate
  user.currentlogin = currentlogin
  user.driver = driver
  user.controlno = controlno
  user.driverid = driverid
  user.tare = tare
  user.rfid = rfid
  user.rfno = rfno
  user.locationid = locationid
  user.transporterid = transporterid
  user.vehicleid = vehicleid
  user.slipno = slipno
  user.quantity = quantity
  user.fueloperator = fueloperator
  user.wheeler = wheeler
  db.session.commit()
  return jsonify('ingate update completed')

#$ delete the data from inagte table
def delete_ingate(slipid):  
    user = Ingate.query.filter_by(slipid=slipid).first()   
    if not user:   
      return jsonify({'message': 'ingate-user does not exist'})   

    db.session.delete(user)  
    db.session.commit()   

    return jsonify({'message': 'ingate-user Successfully deleted'})

# commits the changes to database.
def save_changes(data):
    db.session.add(data)
    db.session.commit()


def generate_token(ingate):
    try:
        # generate the auth token
        auth_token = ingate.encode_auth_token(ingate.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return generate_token(ingate)
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401
