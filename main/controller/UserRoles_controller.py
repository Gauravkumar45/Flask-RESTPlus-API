#imports all the required resources for the UserRoles controller.
#We defined two concrete classes in our UserRoles controller which are
#UserRolesList and UserRoles. These two classes extends the abstract flask-restplus resource.

from flask import request
from flask_restplus import Resource

from ..util.dto import UserRolesDto
from ..service.UserRoles_service import get_a_UserRoles, get_all_UserRoles, save_new_UserRoles , complete_UserRoles, delete_UserRoles

api = UserRolesDto.api
_UserRoles = UserRolesDto.UserRoles


@api.route('/')
class UserRolesList(Resource):
    # get method using for get all UserRoles in users table
    @api.doc('list_of_registered_UserRoles')
    @api.marshal_list_with(_UserRoles, envelope='data')
    def get(self):
        """List all registered UserRoles"""
        return get_all_UserRoles()
    # post method using for craete the new UserRoles in users table
    @api.response(201, 'UserRoles successfully created.')
    @api.doc('create a new UserRoles')
    @api.expect(_UserRoles, validate=True)
    def post(self):
        """Creates a new UserRoles """
        data = request.json
        return save_new_UserRoles(data=data)


@api.route('/<UserRoleId>')
@api.param('UserRoleId', 'The UserRoles identifier') # A decorator to specify one of the expected parameters
@api.response(404, 'UserRoles not found.')
class UserRoles(Resource):
    # get method using for get one data in UserRoles table 
    @api.doc('get a UserRoles')
    @api.marshal_with(_UserRoles)
    def get(self, UserRoleId):
        """get a UserRoles given its identifier"""
        user = get_a_UserRoles(UserRoleId)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return get_a_UserRoles(data=data)
    # put method using in the users table 
    @api.response(201, 'UserRoles successfully update.')
    @api.doc('update new UserRoles')
    @api.expect(_UserRoles, validate=True)
    def put(self, UserRoleId):
        """UserRoles updated """
        user = complete_UserRoles(UserRoleId)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return complete_UserRoles(data=data)
    # delete method using for the delete elements the users table 
    @api.response(201, 'UserRoles successfully Deleted.')
    @api.doc('successfully Delete UserRoles')
    @api.expect(_UserRoles, validate=True)
    def delete(self, UserRoleId):
        """ UserRoles deleted"""
        user = delete_UserRoles(UserRoleId)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return delete_UserRoles(data=data)