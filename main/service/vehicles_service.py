import uuid
import datetime
from flask import  request, jsonify
from main import db
from main.model.vehicles import Vehicles

# insert the data from the vehicles table
def save_new_user(data):
    user = Vehicles.query.filter_by(vehicleno=data['vehicleno']).first()
    if not user:
        new_user = Vehicles(
            vehicleno=data['vehicleno'], compliant=data['compliant'],ownerid=data['ownerid'],ownername=data['ownername'],ownermobile=data['ownermobile'],
            rcno=data['rcno'],tempno=data['tempno'],chasisno=data['chasisno'],fitnessexpiry=datetime.datetime.utcnow(),
            insuranceexpiry=datetime.datetime.utcnow(),permitexpiry=datetime.datetime.utcnow(),pollutionexpiry=datetime.datetime.utcnow(),
            permittype=data['permittype'],status=data['status'],statuschangedate=datetime.datetime.utcnow(),createdate=datetime.datetime.utcnow(),
            ownerpan=data['ownerpan'],rfno=data['rfno'],permit=data['permit'],insurance=data['insurance'],pollution=data['pollution'],
            fitness=data['fitness'],roadtax=data['roadtax'],roadtaxexpiry=datetime.datetime.utcnow(),rcdate=datetime.datetime.utcnow(),
            wheeler=data['wheeler'],vowner=data['vowner'],vcontact=data['vcontact'],vaddress=data['vaddress'],vownership=data['vownership'],
            gpsdate=data['gpsdate'],gpsno=data['gpsno'],imeino=data['imeino'],modelno=data['modelno'],engine=data['engine']
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Vehicles Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409

# get the all data from the vehilces table
def get_all_users():
    return Vehicles.query.all()

# get the one data from the vehicles table
def get_a_user(vehicleid):
    return Vehicles.query.filter_by(vehicleid=vehicleid).first()

# update the data from the vehicles table
def complete_vehicles(vehicleid):
  user = Vehicles.query.filter_by(vehicleid=vehicleid).first()

  if not user:
    return jsonify({'message' : 'No vehicles found!'})

  vehicleno = request.json['vehicleno']
  compliant = request.json['compliant']
  ownerid = request.json['ownerid']
  ownername = request.json['ownername']
  ownermobile = request.json['ownermobile']
  rcno = request.json['rcno']
  tempno = request.json['tempno']
  chasisno = request.json['chasisno']
  permittype = request.json['permittype']
  status = request.json['status']
  ownerpan = request.json['ownerpan']
  rfno = request.json['rfno']
  permit = request.json['permit']
  insurance = request.json['insurance']
  pollution = request.json['pollution']
  fitness = request.json['fitness']
  roadtax = request.json['roadtax']
  wheeler = request.json['wheeler']
  vowner = request.json['vowner']
  vcontact = request.json['vcontact']
  vaddress = request.json['vaddress']
  vownership = request.json['vownership']
  gpsdate = request.json['gpsdate']
  gpsno = request.json['gpsno']
  imeino = request.json['imeino']
  modelno = request.json['modelno']
  engine = request.json['engine']

  user.vehicleno = vehicleno
  user.compliant = compliant
  user.ownerid = ownerid
  user.ownername = ownername
  user.ownermobile = ownermobile
  user.rcno = rcno
  user.tempno = tempno
  user.chasisno = chasisno
  user.permittype = permittype
  user.status = status
  user.ownerpan = ownerpan
  user.rfno = rfno
  user.permit = permit
  user.insurance = insurance
  user.pollution = pollution
  user.fitness = fitness
  user.roadtax = roadtax
  user.wheeler = wheeler
  user.vowner = vowner
  user.vcontact = vcontact
  user.vaddress = vaddress
  user.vownership = vownership
  user.gpsdate = gpsdate
  user.gpsno = gpsno
  user.imeino = imeino
  user.modelno = modelno
  user.engine = engine
  db.session.commit()
  return jsonify('Vehicles Successfully Update')

# delete the data from the vehilces table 
def delete_vehicles(vehicleid):  
    user = Vehicles.query.filter_by(vehicleid=vehicleid).first()
    if not user:   
      return jsonify({'message': 'vehicles does not exist'})   

    db.session.delete(user)  
    db.session.commit()   

    return jsonify({'message': 'Vehicles Successfully deleted'})

# commits the changes to database.
def save_changes(data):
    db.session.add(data)
    db.session.commit()


def generate_token(vehicles):
    try:
        # generate the auth token
        auth_token = vehicles.encode_auth_token(vehicles.vehicleid)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return generate_token(vehicles)
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401