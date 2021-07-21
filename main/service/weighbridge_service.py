import uuid
import datetime
from flask import Flask, request, jsonify
from main import db
from main.model.weighbridge import Weighbridge

# insert the data from the weighbridge table
def save_new_user(data):
    user = Weighbridge.query.filter_by(wbname=data['wbname']).first()
    if not user:
        new_user = Weighbridge(
            wbname=data['wbname'],
            locationid=data['locationid'],
            location=data['location'],
            capacity=data['capacity']
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

# get the all data from the weighbridge table
def get_all_users():
    return Weighbridge.query.all()

# get the one data from the weighbridge table
def get_a_user(wbid):
    return Weighbridge.query.filter_by(wbid=wbid).first()

#  update the data from the weighbridge table
def complete_weighbridge(wbid):
  user = Weighbridge.query.filter_by(wbid=wbid).first()

  if not user:
    return jsonify({'message' : 'No weighbridge found!'})

  wbname = request.json['wbname']
  locationid = request.json['locationid']
  location = request.json['location']
  capacity = request.json['capacity']

  user.wbname = wbname
  user.locationid = locationid
  user.location = location
  user.capacity = capacity
  db.session.commit()
  return jsonify('weightbridge update completed')

# delete the data from the weighbridge table
def delete_weighbridge(wbid):  
    user = Weighbridge.query.filter_by(wbid=wbid).first()   
    if not user:   
      return jsonify({'message': 'weighbridge does not exist'})   

# commits the changes to database.
    db.session.delete(user)  
    db.session.commit()   

    return jsonify({'message': 'weighbridge deleted'})

def save_changes(data):
    db.session.add(data)
    db.session.commit()


def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return generate_token(user)
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401