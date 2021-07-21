from flask import  request, jsonify
from main import db
import uuid
from main.model.users import Users

# insert the data from the users table
def save_new_user(data):
    user = Users.query.filter_by(Username=data['Username']).first()
    if not user:
        new_user = Users(
            Username=data['Username'], DisplayName=data['DisplayName'],Email=data['Email'],Source=data['Source'],PasswordHash=data['PasswordHash'],
            PasswordSalt=data['PasswordSalt'],LastDirectoryUpdate=data['LastDirectoryUpdate'],UserImage=data['UserImage'],InsertDate=data['InsertDate'],
            InsertUserId=data['InsertUserId'],IsActive=data['IsActive'],UpdateUserId=data['UpdateUserId'],Password=data['Password']
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'User Successfully registered.'
        }
        return response_object, 201
        
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409

# get the all data from the users table
def get_all_users():
    return Users.query.all()

# get the one data from the users table
def get_a_user(UserId):
    return Users.query.filter_by(UserId=UserId).first()
    
# update the data from the users table
def complete_users(UserId):
  user = Users.query.filter_by(UserId=UserId).first()

  if not user:
    return jsonify({'message' : 'No user found!'})

  Username = request.json['Username']
  DisplayName = request.json['DisplayName']
  Email = request.json['Email']
  Source = request.json['Source']
  PasswordHash = request.json['PasswordHash']
  PasswordSalt = request.json['PasswordSalt']
  LastDirectoryUpdate = request.json['LastDirectoryUpdate']
  UserImage = request.json['UserImage']
  InsertUserId = request.json['InsertUserId']
  UpdateUserId = request.json['UpdateUserId']
  Password = request.json['Password']

  user.Username = Username
  user.DisplayName = DisplayName
  user.Email = Email
  user.Source = Source
  user.PasswordHash = PasswordHash
  user.PasswordSalt = PasswordSalt
  user.LastDirectoryUpdate = LastDirectoryUpdate
  user.UserImage = UserImage
  user.InsertUserId = InsertUserId
  user.UpdateUserId = UpdateUserId
  user.Password = Password
  db.session.commit()
  return jsonify('user update completed')

# delete the data from the users table
def delete_user(UserId):  
    user = Users.query.filter_by(UserId=UserId).first()   
    if not user:   
       return jsonify({'message': 'user does not exist'})   

    db.session.delete(user)  
    db.session.commit()   

    return jsonify({'message': 'User Successfully deleted'})

# commits the changes to database.
def save_changes(data):
    db.session.add(data)
    db.session.commit()


def generate_token(users):
    try:
        # generate the auth token
        auth_token = users.encode_auth_token(users.UserId)
        response_object = {
            'status': 'success',
            'message': 'User Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return generate_token(users)
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401
