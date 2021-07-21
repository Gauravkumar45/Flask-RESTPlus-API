from flask import  request, jsonify
from main import db
import uuid
from main.model.Roles import Roles

# insert the data from the Roles table
def save_new_Roles(data):
    user = Roles.query.filter_by(RoleName=data['RoleName']).first()
    if not user:
        new_user = Roles(
            RoleName=data['RoleName']
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Roles Successfully registered.'
        }
        return response_object, 201
        
    else:
        response_object = {
            'status': 'fail',
            'message': 'Roles already exists. Please Log in.',
        }
        return response_object, 409

# get the all data from the Roles table
def get_all_Roles():
    return Roles.query.all()

# get the one data from the Roles table
def get_a_Roles(RoleId):
    return Roles.query.filter_by(RoleId=RoleId).first()
    
# update the data from the Roles table
def complete_Roles(RoleId):
  user = Roles.query.filter_by(RoleId=RoleId).first()

  if not user:
    return jsonify({'message' : 'No Roles found!'})

  RoleName = request.json['RoleName']

  user.RoleName = RoleName
  db.session.commit()
  return jsonify('Roles update completed')

# delete the data from the Roles table
def delete_Roles(RoleId):  
    user = Roles.query.filter_by(RoleId=RoleId).first()   
    if not user:   
       return jsonify({'message': 'Roles does not exist'})   

    db.session.delete(user)  
    db.session.commit()   

    return jsonify({'message': 'Roles Successfully deleted'})

# commits the changes to database.
def save_changes(data):
    db.session.add(data)
    db.session.commit()


def generate_token(Roles):
    try:
        # generate the auth token
        auth_token = Roles.encode_auth_token(Roles.RoleId)
        response_object = {
            'status': 'success',
            'message': 'Roles Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return generate_token(Roles)
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401
