import uuid
import datetime
from flask import request, jsonify
from main import db
from main.model.locations import Locations

# insert the data in locations table 
def save_new_user(data):
    user = Locations.query.filter_by(location=data['location']).first()
    if not user:
        new_user = Locations(
            location=data['location'],
            locationcode=data['locationcode']
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Location Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Location already exists. Please Log in.',
        }
        return response_object, 409

# get the all data in loacations table
def get_all_users():
    return Locations.query.all()

# get the one data in locations table 
def get_a_user(locationid):
    return Locations.query.filter_by(locationid=locationid).first()

# update the data in locations table
def complete_locations(locationid):
  user = Locations.query.filter_by(locationid=locationid).first()

  location = request.json['location']
  locationcode = request.json['locationcode']
 
  user.location = location
  user.locationcode = locationcode
  db.session.commit()
  return jsonify('Location Update completed')

# delete the data in locations table
def delete_locations(locationid):  
    user = Locations.query.filter_by(locationid=locationid).first()   
    if not user:   
       return jsonify({'message': 'Location does not exist'})   

    db.session.delete(user)  
    db.session.commit()  
    return jsonify({'message': 'Location Successfully deleted'})

def save_changes(data):
    db.session.add(data)
    db.session.commit()

def generate_token(locations):
    try:
        # generate the auth token
        auth_token = locations.encode_auth_token(locations.locationid)
        response_object = {
            'status': 'success',
            'message': 'Locations Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return generate_token(locations)
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401