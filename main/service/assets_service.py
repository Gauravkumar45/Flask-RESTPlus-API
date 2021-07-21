from flask import  request, jsonify
from main import db
from main.model.assets import Assets

# insert the data from assest table
def save_new_user(data):
    user = Assets.query.filter_by(assetname=data['assetname']).first()
    if not user:
        new_user = Assets(
            assetname=data['assetname'],category=data['category'], make=data['make'],model=data['model'],serialno=data['serialno'],location=data['location'],
            assetcode=data['assetcode'],status=data['status'],categoryid=data['categoryid'],locationid=data['locationid']
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Asssets Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Asssets already exists. Please Log in.',
        }
        return response_object, 409

# get all data from asset table
def get_all_users():
    return Assets.query.all()

# get one data from asset table
def get_a_user(assetid):
    return Assets.query.filter_by(assetid=assetid).first()

# update the data from asset table
def complete_users(assetid):
  user = Assets.query.filter_by(assetid=assetid).first()

  if not user:
    return jsonify({'message' : 'No Asssets found!'})

  assetname = request.json['assetname']
  category = request.json['category']
  make = request.json['make']
  model = request.json['model']
  serialno = request.json['serialno']
  location = request.json['location']
  assetcode = request.json['assetcode']
  status = request.json['status']
  categoryid = request.json['categoryid']
  locationid = request.json['locationid']
  
  user.assetname = assetname
  user.category = category
  user.make = make
  user.model = model
  user.serialno = serialno
  user.location = location
  user.assetcode = assetcode
  user.status = status
  user.categoryid = categoryid
  user.locationid = locationid
  db.session.commit()
  return jsonify('Asssets update completed')

# delete the asset data from assets table
def delete_user(assetid):  
    user = Assets.query.filter_by(assetid=assetid).first()   
    if not user:   
       return jsonify({'message': 'Asssets does not exist'})   

    db.session.delete(user)  
    db.session.commit()   

    return jsonify({'message': 'Asssets Successfully deleted'})

#commits the changes to database.
def save_changes(data):
    db.session.add(data)
    db.session.commit()

def generate_token(Assets):
    try:
        # generate the auth token
        auth_token = Assets.encode_auth_token(Assets.assetid)
        response_object = {
            'status': 'success',
            'message': 'Asssets Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return generate_token(Assets)
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401
