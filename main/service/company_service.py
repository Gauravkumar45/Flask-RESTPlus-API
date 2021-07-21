from flask import  request, jsonify
from main import db
import uuid
from main.model.company import Company

# insert the data from the Company table
def save_new_Company(data):
    user = Company.query.filter_by(cname=data['cname']).first()
    if not user:
        new_user = Company(
            cname=data['cname'], 
            address1=data['address1'],
            address2=data['address2'],
            phone=data['phone']
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Company Successfully registered.'
        }
        return response_object, 201
        
    else:
        response_object = {
            'status': 'fail',
            'message': 'Company already exists. Please Log in.',
        }
        return response_object, 409

# get the all data from the Company table
def get_all_Company():
    return Company.query.all()

# get the one data from the Company table
def get_a_Company(cid):
    return Company.query.filter_by(cid=cid).first()
    
# update the data from the Company table
def complete_Company(cid):
  user = Company.query.filter_by(cid=cid).first()

  if not user:
    return jsonify({'message' : 'No comapany found!'})

  cname = request.json['cname']
  address1 = request.json['address1']
  address2 = request.json['address2']
  phone = request.json['phone']

  user.cname = cname
  user.address1 = address1
  user.address2 = address2
  user.phone = phone
  db.session.commit()
  return jsonify('comapany update completed')

# delete the data from the Company table
def delete_Company(cid):  
    user = Company.query.filter_by(cid=cid).first()   
    if not user:   
       return jsonify({'message': 'Company does not exist'})   

    db.session.delete(user)  
    db.session.commit()   

    return jsonify({'message': 'Company Successfully deleted'})

# commits the changes to database.
def save_changes(data):
    db.session.add(data)
    db.session.commit()


def generate_token(company):
    try:
        # generate the auth token
        auth_token = company.encode_auth_token(company.cid)
        response_object = {
            'status': 'success',
            'message': 'company Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return generate_token(company)
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401
