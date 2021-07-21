from flask import  request, jsonify
from main import db
import uuid
from main.model.fuelmaster import Fuelmaster

# insert the data from the Fuelmaster table
def save_new_fuelmaster(data):
    user = Fuelmaster.query.filter_by(wheels=data['wheels']).first()
    if not user:
        new_user = Fuelmaster( 
            wheels=data['wheels'],
            fuelpermt=data['fuelpermt'],
            effectivefrom=data['effectivefrom']
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Fuelmaster Successfully registered.'
        }
        return response_object, 201
        
    else:
        response_object = {
            'status': 'fail',
            'message': 'Fuelmaster already exists. Please Log in.',
        }
        return response_object, 409

# get the all data from the Fuelmaster table
def get_all_fuelmaster():
    return Fuelmaster.query.all()

# get the one data from the Fuelmaster table
def get_a_fuelmaster(fuelid):
    return Fuelmaster.query.filter_by(fuelid=fuelid).first()
    
# update the data from the Fuelmaster table
def complete_fuelmaster(fuelid):
  user = Fuelmaster.query.filter_by(fuelid=fuelid).first()

  if not user:
    return jsonify({'message' : 'No Fuelmaster found!'})

  wheels = request.json['wheels']
  fuelpermt = request.json['fuelpermt']
  effectivefrom = request.json['effectivefrom']

  user.wheels = wheels
  user.fuelpermt = fuelpermt
  user.effectivefrom = effectivefrom
  db.session.commit()
  return jsonify('Fuelmaster update completed')

# delete the data from the Fuelmaster table
def delete_fuelmaster(fuelid):  
    user = Fuelmaster.query.filter_by(fuelid=fuelid).first()   
    if not user:   
       return jsonify({'message': 'Fuelmaster does not exist'})   

    db.session.delete(user)  
    db.session.commit()   

    return jsonify({'message': 'Fuelmaster Successfully deleted'})

# commits the changes to database.
def save_changes(data):
    db.session.add(data)
    db.session.commit()


def generate_token(fuelmaster):
    try:
        # generate the auth token
        auth_token = fuelmaster.encode_auth_token(fuelmaster.fuelid)
        response_object = {
            'status': 'success',
            'message': 'User Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return generate_token(fuelmaster)
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401
