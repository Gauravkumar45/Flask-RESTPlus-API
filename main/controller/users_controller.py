#imports all the required resources for the users controller.
#We defined two concrete classes in our user controller which are
#usersList and users. These two classes extends the abstract flask-restplus resource.

from flask import request
from flask_restplus import Resource

from ..util.dto import UsersDto
from ..service.users_service import get_a_user, get_all_users, save_new_user , complete_users, delete_user

api = UsersDto.api
_users = UsersDto.users


@api.route('/')
class UsersList(Resource):
    # get method using for get all user in users table
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_users, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()
    # post method using for craete the new user in users table
    @api.response(201, 'User successfully created.')
    @api.doc('create a new users')
    @api.expect(_users, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/<UserId>')
@api.param('UserId', 'The User identifier') # A decorator to specify one of the expected parameters
@api.response(404, 'User not found.')
class Users(Resource):
    # get method using for get one data in users table 
    @api.doc('get a user')
    @api.marshal_with(_users)
    def get(self, UserId):
        """get a user given its identifier"""
        user = get_a_user(UserId)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return get_a_user(data=data)
    # put method using in the users table 
    @api.response(201, 'Users successfully update.')
    @api.doc('successfully update new user')
    @api.expect(_users, validate=True)
    def put(self, UserId):
        """Users Updated"""
        user = complete_users(UserId)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return complete_users(data=data)
    # delete method using for the delete elements the users table 
    @api.response(201, 'User successfully Deleted.')
    @api.doc('Delete users successfully')
    @api.expect(_users, validate=True)
    def delete(self, UserId):
        """Users Deleted"""
        user = delete_user(UserId)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return delete_user(data=data)