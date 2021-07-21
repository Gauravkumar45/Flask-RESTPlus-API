from flask import  request, jsonify
from main import db
from main.model.outgate import Outgate

# insert the data in outgate table
def save_new_user(data):
    user = Outgate.query.filter_by(slipno=data['slipno']).first()
    if not user:
        new_user = Outgate(
            slipno=data['slipno'],slipid=data['slipid'], vehicleno=data['vehicleno'],driver=data['driver'],driverid=data['driverid'],loading=data['loading'],
            destination=data['destination'],challanno=data['challanno'],gross=data['gross'],tare=data['tare'],net=data['net'],passgate=data['passgate'],
            material=data['material'],weighbridge=data['weighbridge'],vehicleid=data['vehicleid'],locationid=data['locationid'],username=data['username'],
            transporterid=data['transporterid'],transporter=data['transporter'],challannet=data['challannet'],grosswbid=data['grosswbid'],grosswb=data['grosswb'],
            tarewbid = data['tarewbid'],tarewb = data['tarewb'],passusername = data['passusername'],wbdatetime= data['wbdatetime']
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Outgate Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Outgate already exists. Please Log in.',
        }
        return response_object, 409

# get the data in outgate table 
def get_all_users():
    return Outgate.query.all()

# get the one data in outgate table
def get_a_user(challanid):
    return Outgate.query.filter_by(challanid=challanid).first()

# update the data in outgATE table    
def complete_users(challanid):
  user = Outgate.query.filter_by(challanid=challanid).first()

  if not user:
    return jsonify({'message' : 'No user found!'})

  slipno = request.json['slipno']
  slipid = request.json['slipid']
  vehicleno = request.json['vehicleno']
  driver = request.json['driver']
  driverid = request.json['driverid']
  loading = request.json['loading']
  destination = request.json['destination']
  challanno = request.json['challanno']
  gross = request.json['gross']
  tare= request.json['tare']
  net = request.json['net']
  passgate = request.json['passgate']
  material = request.json['material']
  weighbridge = request.json['weighbridge']
  vehicleid = request.json['vehicleid']
  locationid = request.json['locationid']
  username = request.json['username']
  tranporterid = request.json['tranporterid']
  transporter = request.json['transporter']
  challannet = request.json['challannet']
  grosswbid = request.json['grosswbid']
  grosswb = request.json['grosswb']
  tarewbid = request.json['tarewbid']
  tarewb = request.json['tarewb']
  passusername = request.json['passusername']
  wbdatetime = request.json['wbdatetime']

  user.slipno = slipno
  user.slipid = slipid
  user.vehicleno = vehicleno
  user.driver = driver
  user.driverid = driverid
  user.loading = loading
  user.destination = destination
  user.challanno = challanno
  user.gross = gross
  user.tare = tare
  user.net = net
  user.passgate = passgate
  user.material = material
  user.weighbridge = weighbridge
  user.vehicleid = vehicleid
  user.locationid= locationid
  user.username = username
  user.tranporterid = tranporterid
  user.transporter = transporter
  user.cchallannet = challannet
  user.grosswbid = grosswbid
  user.grosswb = grosswb
  user.tarewbid = tarewbid
  user.tarewb = tarewb
  user.passusername = passusername
  user.wbdatetime = wbdatetime
  db.session.commit()
  return jsonify('outgate update completed')

# delete the data in outgate table
def delete_user(challanid):  
    user = Outgate.query.filter_by(challanid=challanid).first()   
    if not user:   
       return jsonify({'message': 'outgate does not exist'})   

    db.session.delete(user)  
    db.session.commit()   

    return jsonify({'message': 'Outgate Successfully deleted'})

# commits the changes to database.
def save_changes(data):
    db.session.add(data)
    db.session.commit()


def generate_token(outgate):
    try:
        # generate the auth token
        auth_token = outgate.encode_auth_token(outgate.challanid)
        response_object = {
            'status': 'success',
            'message': 'Outgate Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return generate_token(outgate)
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401
