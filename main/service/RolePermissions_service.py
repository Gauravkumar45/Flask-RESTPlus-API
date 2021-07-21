from flask import  request, jsonify
from main import db
import uuid
from main.model.RolePermissions import RolePermissions

# insert the data from the RolePermissions table
def save_new_RolePermissions(data):
    user = RolePermissions.query.filter_by(RolePermissionId=data['RolePermissionId']).first()
    if not user:
        new_user = RolePermissions(
            RoleId=data['RoleId'], 
            PermissionKey=data['PermissionKey']
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'RolePermissions Successfully registered.'
        }
        return response_object, 201
        
    else:
        response_object = {
            'status': 'fail',
            'message': 'RolePermissions already exists. Please Log in.',
        }
        return response_object, 409

# get the all data from the RolePermissions table
def get_all_RolePermissions():
    return RolePermissions.query.all()

# get the one data from the RolePermissions table
def get_a_RolePermissions(RolePermissionId):
    return RolePermissions.query.filter_by(RolePermissionId=RolePermissionId).first()
    
# update the data from the RolePermissions table
def complete_RolePermissions(RolePermissionId):
  user = RolePermissions.query.filter_by(RolePermissionId=RolePermissionId).first()

  if not user:
    return jsonify({'message' : 'No RolePermissions found!'})

  RoleId = request.json['RoleId']
  PermissionKey = request.json['PermissionKey']

  user.RoleId = RoleId
  user.PermissionKey = PermissionKey
  db.session.commit()
  return jsonify('RolePermissions update completed')

# delete the data from the RolePermissions table
def delete_RolePermissions(RolePermissionId):  
    user = RolePermissions.query.filter_by(RolePermissionId=RolePermissionId).first()   
    if not user:   
       return jsonify({'message': 'RolePermissions does not exist'})   

    db.session.delete(user)  
    db.session.commit()   

    return jsonify({'message': 'RolePermissions Successfully deleted'})

# commits the changes to database.
def save_changes(data):
    db.session.add(data)
    db.session.commit()


def generate_token(RolePermissions):
    try:
        # generate the auth token
        auth_token = RolePermissions.encode_auth_token(RolePermissions.RolePermissionId)
        response_object = {
            'status': 'success',
            'message': 'User Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return generate_token(RolePermissions)
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401
