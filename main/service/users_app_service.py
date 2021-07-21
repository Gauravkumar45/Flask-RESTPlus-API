from flask import  request, jsonify
from main import db
import uuid
from main.model.users_app import Users_app

# insert the data from the Users_app table
def save_new_users_app(data):
    user = Users_app.query.filter_by(id=data['id']).first()
    if not user:
        new_user = Users_app(
            user_name=data['user_name'], password=data['password'],is_active=data['is_active'],display_name=data['display_name'],create_date=data['create_date'],public_id=data['public_id'],admin=data['admin']
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Users_app Successfully registered.'
        }
        return response_object, 201
        
    else:
        response_object = {
            'status': 'fail',
            'message': 'Users_app already exists. Please Log in.',
        }
        return response_object, 409

# get the all data from the Users_app table
def get_all_users_app():
    return Users_app.query.all()

# get the one data from the Users_app table
def get_a_users_app(id):
    return Users_app.query.filter_by(id=id).first()
    
# update the data from the Users_app table
def complete_users_app(id):
  user = Users_app.query.filter_by(id=id).first()

  if not user:
    return jsonify({'message' : 'No user found!'})

  user_name = request.json['user_name']
  password = request.json['password']
  is_active = request.json['is_active']
  display_name = request.json['display_name']
  create_date = request.json['create_date']
  public_id = request.json['public_id']
  admin = request.json['admin']

  user.user_name = user_name
  user.password = password
  user.is_active = is_active
  user.display_name = display_name
  user.create_date = create_date
  user.public_id = public_id
  user.admin = admin
  db.session.commit()
  return jsonify('Users_app update completed')

# delete the data from the Users_app table
def delete_users_app(id):  
    user = Users_app.query.filter_by(id=id).first()   
    if not user:   
       return jsonify({'message': 'Users_app does not exist'})   

    db.session.delete(user)  
    db.session.commit()   

    return jsonify({'message': 'Users_app Successfully deleted'})

# commits the changes to database.
def save_changes(data):
    db.session.add(data)
    db.session.commit()


def generate_token(Users_app):
    try:
        # generate the auth token
        auth_token = Users_app.encode_auth_token(users.userid)
        response_object = {
            'status': 'success',
            'message': 'Users_app Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return generate_token(Users_app)
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401
