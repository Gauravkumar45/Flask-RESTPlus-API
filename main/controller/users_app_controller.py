#imports all the required resources for the users_app controller.
#We defined two concrete classes in our user controller which are
#users_appList and users_app. These two classes extends the abstract flask-restplus resource.

from flask import request
from flask_restplus import Resource

from ..util.dto import users_appDto
from ..service.users_app_service import get_a_users_app, get_all_users_app, save_new_users_app , complete_users_app, delete_users_app

api = users_appDto.api
_users_app = users_appDto.users_app


@api.route('/')
class users_appList(Resource):
    # get method using for get all users_app in users table
    @api.doc('list_of_registered_users_app')
    @api.marshal_list_with(_users_app, envelope='data')
    def get(self):
        """List all registered users_app"""
        return get_all_users_app()
    # post method using for craete the new user in users table
    @api.response(201, 'users_app successfully created.')
    @api.doc('create a new users_app')
    @api.expect(_users_app, validate=True)
    def post(self):
        """Creates a new users_app """
        data = request.json
        return save_new_users_app(data=data)


@api.route('/<id>')
@api.param('id', 'The users_app identifier') # A decorator to specify one of the expected parameters
@api.response(404, 'users_app not found.')
class Users_app(Resource):
    # get method using for get one data in users_app table 
    @api.doc('get a users_app')
    @api.marshal_with(_users_app)
    def get(self, id):
        """get a users_app given its identifier"""
        user = get_a_users_app(id)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return get_a_users_app(data=data)
    # put method using in the users table 
    @api.response(201, 'users_app successfully update.')
    @api.doc(' successfully update new users_app')
    @api.expect(_users_app, validate=True)
    def put(self, id):
        """users_app Updated"""
        user = complete_users_app(id)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return complete_users_app(data=data)
    # delete method using for the delete elements the users_app table 
    @api.response(201, 'users_app successfully Deleted.')
    @api.doc(' successfully Delete users_app')
    @api.expect(_users_app, validate=True)
    def delete(self, id):
        """users_app Deleted"""
        user = delete_users_app(id)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return delete_users_app(data=data)