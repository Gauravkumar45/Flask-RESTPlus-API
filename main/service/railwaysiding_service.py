import uuid
import datetime
from flask import request, jsonify
from main import db
from main.model.railwaysiding import Railwaysiding

# insert the data from the railwaysiding table
def save_new_railwaysiding(data):
    user = Railwaysiding.query.filter_by(vehicleno=data['vehicleno']).first()
    if not user:
        new_user = Railwaysiding(
            vehicleno=data['vehicleno'], grosswb=data['grosswb'],gross=data['gross'],tarewb=data['tarewb'],tare=data['tare'],net=data['net'],
            entrytime=datetime.datetime.utcnow(),shortage=data['shortage'],exittime=data['exittime'],remarks=data['remarks'],vehicleid=data['vehicleid'],
            challannet=data['challannet'],challanno=data['challanno'],slipno=data['slipno'], grosswbid=data['grosswbid'],tarewbid=data['tarewbid'],
            usergross=data['usergross'],usertare=data['usertare']
            
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409

# get the all data from the railwaysiding table
def get_all_railwaysiding():
    return Railwaysiding.query.all()

# get the one data from railwaysiding table
def get_a_railwaysiding(entryid):
    return Railwaysiding.query.filter_by(entryid=entryid).first()

# update the data from the railwaysiding table
def complete_railwaysiding(entryid):
  user = Railwaysiding.query.filter_by(entryid=entryid).first()
  
  vehicleno = request.json['vehicleno']
  grosswb = request.json['grosswb']
  gross = request.json['gross']
  tarewb = request.json['tarewb']
  tare = request.json['tare']
  net = request.json['net']
  shortage = request.json['shortage']
  exittime = request.json['exittime']
  remarks = request.json['remarks']
  vehicleid = request.json['vehicleid']
  challannet = request.json['challannet']
  challanno = request.json['challanno']
  slipno = request.json['slipno']
  grosswbid = request.json['grosswbid']
  tarewbid = request.json['tarewbid']
  usergross = request.json['usergross']
  usertare = request.json['usertare']

  user.vehicleno = vehicleno
  user.grosswb = grosswb
  user.gross = gross
  user.tarewb = tarewb
  user.tare = tare
  user.net = net
  user.shortage = shortage
  user.exittime = exittime
  user.remarks = remarks
  user.vehicleid = vehicleid
  user.challannet = challannet
  user.challanno = challanno
  user.slipno = slipno
  user.grosswbid = grosswbid
  user.tarewbid = tarewbid
  user.usergross = usergross
  user.usertare = usertare
  db.session.commit()
  return jsonify('railwaysiding update completed')

# delete the data from the railwaysiding table
def delete_railwaysiding(entryid):  
    user = Railwaysiding.query.filter_by(entryid=entryid).first()   
    if not user:   
       return jsonify({'message': 'railwaysiding-user does not exist'})   

    db.session.delete(user)  
    db.session.commit()   

    return jsonify({'message': 'railwaysiding-user deleted'})

# commits the changes to database.
def save_changes(data):
    db.session.add(data)
    db.session.commit()


def generate_token(railwaysiding):
    try:
        # generate the auth token
        auth_token = railwaysiding.encode_auth_token(railwaysiding.uentryid)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return generate_token(railwaysiding)
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401