#imports all the required resources for the userpermissions controller.
#We defined two concrete classes in our userpermissions controller which are
#userpermissionsList and userpermissions. These two classes extends the abstract flask-restplus resource.

from flask import request
from flask_restplus import Resource

from ..util.dto import UserPermissionsDto
from ..service.userpermissions_service import get_a_user, get_all_users, save_new_user , complete_users, delete_user

api = UserPermissionsDto.api
_userpermission = UserPermissionsDto.userpermissions


@api.route('/')
class UserPermissionsList(Resource):
    # get method using for get all user in userpermissions table
    @api.doc('list_of_registered_UserPermissions')
    @api.marshal_list_with(_userpermission, envelope='data')
    def get(self):
        """List all registered UserPermissions"""
        return get_all_users()

    # post method using for craete the new user in userpermissions table
    @api.response(201, 'UserPermissions successfully created.')
    @api.doc('create a new UserPermissions')
    @api.expect(_userpermission, validate=True)
    def post(self):
        """Creates a new UserPermissions """
        data = request.json
        return save_new_user(data=data)


@api.route('/<userpermissionid>')
@api.param('userpermissionid', 'The UserPermissions identifier') # A decorator to specify one of the expected parameters
@api.response(404, 'UserPermissions not found.')
class UserPermissions(Resource):
    @api.doc('get a UserPermissions')
    @api.marshal_with(_userpermission)
    def get(self, userpermissionid):
        # get method using for get one data in userpermissions table 
        """get a UserPermissions given its identifier"""
        user = get_a_user(userpermissionid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return get_a_user(data=data)

    # put method using in the userpermissions table
    @api.response(201, 'UserPermissions successfully update.')
    @api.doc('update new user')
    @api.expect(_userpermission, validate=True)
    def put(self, userpermissionid):
        """UserPermissions updated"""
        user = complete_users(userpermissionid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return complete_users(data=data)

     # delete method using for the delete elements the userpermissions table
    @api.response(201, 'UserPermissions successfully Deleted.')
    @api.doc('Delete UserPermissions')
    @api.expect(_userpermission, validate=True)
    def delete(self, userpermissionid):
        """UserPermissions deleted"""
        user = delete_user(userpermissionid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return delete_user(data=data)