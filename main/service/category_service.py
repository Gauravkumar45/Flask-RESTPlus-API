from flask import  request, jsonify
from main import db
import uuid
from main.model.category import Category

# insert the data from category table
def save_new_user(data):
    user = Category.query.filter_by(categoryname=data['categoryname']).first()
    if not user:
        new_user = Category(
            categoryname=data['categoryname'],
            parentid=data['parentid']
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Category Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409

# get all data from category table
def get_all_users():
    return Category.query.all()

# get only one daat category from
def get_a_user(categoryid):
    return Category.query.filter_by(categoryid=categoryid).first()

# update the data from category table
def complete_users(categoryid):
  user = Category.query.filter_by(categoryid=categoryid).first()

  if not user:
    return jsonify({'message' : 'No category found!'})

  categoryname = request.json['categoryname']
  parentid = request.json['parentid']

  user.categoryname = categoryname
  user.parentid = parentid

  db.session.commit()
  return jsonify('Category update completed')

# delete the data from category table
def delete_user(categoryid):  
    user = Category.query.filter_by(categoryid=categoryid).first()   
    if not user:   
       return jsonify({'message': 'Category does not exist'})   

    db.session.delete(user)  
    db.session.commit()   

    return jsonify({'message': 'Category Successfully deleted'})

#commits the changes to database.
def save_changes(data):
    db.session.add(data)
    db.session.commit()


def generate_token(Category):
    try:
        # generate the auth token
        auth_token = Category.encode_auth_token(Category.categoryid)
        response_object = {
            'status': 'success',
            'message': 'Category Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return generate_token(Category)
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401
