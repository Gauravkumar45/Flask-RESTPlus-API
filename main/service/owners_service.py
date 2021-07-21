import datetime
from flask import request, jsonify
from main import db
from main.model.owners import Owners

# insert the data in owner table
def save_new_user(data):
    user = Owners.query.filter_by(ownername=data['ownername']).first()
    if not user:
        new_user = Owners(
            ownername=data['ownername'], address1=data['address1'],address2=data['address2'],pan=data['pan'],aadhar=data['aadhar'],mobile=data['mobile'],
            gst=data['gst'],startdate=datetime.datetime.utcnow(),enddate=datetime.datetime.utcnow(),dlno=data['dlno'],status=data['status'],
            statuschangedate=datetime.datetime.utcnow(),stateid=data['stateid'],state=data['state'],pincode=data['pincode'],
            bankname=data['bankname'],accountno=data['accountno'],ifsc=data['ifsc'],transportercode=data['transportercode']
            
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Owner Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'owner already exists. Please Log in.',
        }
        return response_object, 409

# get the all data in owner table
def get_all_users():
    return Owners.query.all()

#get the one data in owner table
def get_a_user(ownerid):
    return Owners.query.filter_by(ownerid=ownerid).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()

# update the data in locations table
def complete_owner(ownerid):
  user = Owners.query.filter_by().first()

  if not user:
    return jsonify({'message' : 'No owner found!'})

  ownername = request.json['ownername']
  address1 = request.json['address1']
  address2 = request.json['address2']
  pan = request.json['pan']
  aadhar = request.json['aadhar']
  mobile = request.json['mobile']
  gst = request.json['gst']
  dlno = request.json['dlno']
  status = request.json['status']
  stateid = request.json['stateid']
  state = request.json['state']
  pincode = request.json['pincode']
  bankname = request.json['bankname']
  accountno = request.json['accountno']
  ifsc = request.json['ifsc']
  transportercode = request.json['transportercode']

  user.ownername = ownername
  user.address1 = address1
  user.address2 = address2
  user.pan = pan
  user.aadhar = aadhar
  user.mobile = mobile
  user.gst = gst
  user.dlno = dlno
  user.status = status
  user.stateid = stateid
  user.state = state
  user.pincode = pincode
  user.bankname = bankname
  user.accountno = accountno
  user.ifsc = ifsc
  user.transportercode = transportercode
  db.session.commit()
  return jsonify('Owner Successfully Updated')

# delete the data from the owner table
def delete_owner(ownerid):  
    user = Owners.query.filter_by(ownerid=ownerid).first()   
    if not user:   
       return jsonify({'message': 'owner does not exist'})   

# commits the changes to database.
    db.session.delete(user)  
    db.session.commit()   

    return jsonify({'message': 'Owner Successfully Deleted'})


def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return generate_token(user)
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401