from flask import  request, jsonify
from main import db
import uuid
from main.model.UserRoles import UserRoles

# insert the data from the UserRoles table
def save_new_UserRoles(data):
    user = UserRoles.query.filter_by(UserId=data['UserId']).first()
    if not user:
        new_user = UserRoles(
            UserId=data['UserId'], 
            RoleId=data['RoleId']
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'UserRoles Successfully registered.'
        }
        return response_object, 201
        
    else:
        response_object = {
            'status': 'fail',
            'message': 'UserRoles already exists. Please Log in.',
        }
        return response_object, 409

# get the all data from the UserRoles table
def get_all_UserRoles():
    return UserRoles.query.all()

# get the one data from the UserRoles table
def get_a_UserRoles(UserRoleId):
    return UserRoles.query.filter_by(UserRoleId=UserRoleId).first()
    
# update the data from the UserRoles table
def complete_UserRoles(UserRoleId):
  user = UserRoles.query.filter_by(UserRoleId=UserRoleId).first()

  if not user:
    return jsonify({'message' : 'No UserRoles found!'})

  UserId = request.json['UserId']
  RoleId = request.json['RoleId']

  user.UserId = UserId
  user.RoleId = RoleId
  db.session.commit()
  return jsonify('UserRoles update completed')

# delete the data from the UserRoles table
def delete_UserRoles(UserRoleId):  
    user = UserRoles.query.filter_by(UserRoleId=UserRoleId).first()   
    if not user:   
       return jsonify({'message': 'UserRoles does not exist'})   

    db.session.delete(user)  
    db.session.commit()   

    return jsonify({'message': 'UserRoles Successfully deleted'})

# commits the changes to database.
def save_changes(data):
    db.session.add(data)
    db.session.commit()


def generate_token(UserRoles):
    try:
        # generate the auth token
        auth_token = UserRoles.encode_auth_token(UserRoles.UserRoleId)
        response_object = {
            'status': 'success',
            'message': 'UserRoles Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return generate_token(UserRoles)
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401
