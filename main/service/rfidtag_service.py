from flask import  request, jsonify
import datetime
from main import db
from main.model.rfidtag import Rfidtag

# insert the data from the rfidtag table
def save_new_user(data):
    user = Rfidtag.query.filter_by(rfno=data['rfno']).first()
    if not user:
        new_user = Rfidtag(
            rfno=data['rfno'],isactive=data['isactive'], issuedate=datetime.datetime.utcnow(),vehicleno=data['vehicleno'],vehicleid=data['vehicleid']
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'rfidtag Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'rfidtag already exists. Please Log in.',
        }
        return response_object, 409

# get the all data from the rfidtag table 
def get_all_users():
    return Rfidtag.query.all()

# get the one data from the rfidtag table
def get_a_user(rfid):
    return Rfidtag.query.filter_by(rfid=rfid).first()

# update the data from the rfidtaG table   
def complete_users(rfid):
  user = Rfidtag.query.filter_by(rfid=rfid).first()

  if not user:
    return jsonify({'message' : 'No user found!'})

  rfno = request.json['rfno']
  isactive = request.json['isactive']
  vehicleno = request.json['vehicleno']
  vehicleid = request.json['vehicleid']

  user.rfno = rfno
  user.isactive = isactive
  user.vehicleno = vehicleno
  user.vehicleid = vehicleid
  db.session.commit()
  return jsonify('rfidtag update completed')

# delete the data from the rfidtag table
def delete_user(rfid):  
    user = Rfidtag.query.filter_by(rfid=rfid).first()   
    if not user:   
       return jsonify({'message': 'rfidtag does not exist'})   

    db.session.delete(user)  
    db.session.commit()   

    return jsonify({'message': 'rfidtag Successfully deleted'})
    
 #commits the changes to database.
def save_changes(data):
    db.session.add(data)
    db.session.commit()


def generate_token(rfidtag):
    try:
        # generate the auth token
        auth_token = rfidtag.encode_auth_token(rfidtag.rfid)
        response_object = {
            'status': 'success',
            'message': 'rfidtag Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return generate_token(rfidtag)
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401
