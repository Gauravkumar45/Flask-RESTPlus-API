from flask import  request, jsonify
from main import db
import uuid
from main.model.userpermissions import UserPermissions

# insert the data from the userpermissions table
def save_new_user(data):
    user = UserPermissions.query.filter_by(UserPermissionId=data['UserPermissionId']).first()
    if not user:
        new_user = UserPermissions(
            UserId=data['UserId'],
            PermissionKey=data['PermissionKey'],
            Granted=data['Granted']
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'UserPermissions Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'UserPermissions already exists. Please Log in.',
        }
        return response_object, 409

#get the all data from the userpermissions tables
def get_all_users():
    return UserPermissions.query.all()

# get the one data from the userpermisssions tables
def get_a_user(UserPermissionId):
    return UserPermissions.query.filter_by(UserPermissionId=UserPermissionId).first()

# update the data from the userpermissions table   
def complete_users(UserPermissionId):
  user = UserPermissions.query.filter_by(UserPermissionId=UserPermissionId).first()

  if not user:
    return jsonify({'message' : 'No user found!'})

  UserId = request.json['UserId']
  PermissionKey = request.json['PermissionKey']
  Granted = request.json['Granted']

  user.UserId = UserId
  user.PermissionKey = PermissionKey
  user.Granted = Granted
  db.session.commit()
  return jsonify('UserPermissions update completed')

# delete the data from the userpermissions table
def delete_user(UserPermissionId):  
    user = UserPermissions.query.filter_by(UserPermissionId=UserPermissionId).first()   
    if not user:   
       return jsonify({'message': 'UserPermissions does not exist'})   

    db.session.delete(user)  
    db.session.commit()   

    return jsonify({'message': 'UserPermissions Successfully deleted'})

# commits the changes to database.
def save_changes(data):
    db.session.add(data)
    db.session.commit()


def generate_token(UserPermissions):
    try:
        # generate the auth token
        auth_token = UserPermissions.encode_auth_token(UserPermissions.userpermissionid)
        response_object = {
            'status': 'success',
            'message': 'UserPermissions Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return generate_token(UserPermissions)
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401
