#imports all the required resources for the RolePermissions controller.
#We defined two concrete classes in our RolePermissions controller which are
#RolePermissionsList and RolePermissions. These two classes extends the abstract flask-restplus resource.

from flask import request
from flask_restplus import Resource

from ..util.dto import RolePermissionsDto
from ..service.RolePermissions_service import get_a_RolePermissions, get_all_RolePermissions, save_new_RolePermissions , complete_RolePermissions, delete_RolePermissions

api = RolePermissionsDto.api
_RolePermissions = RolePermissionsDto.RolePermissions


@api.route('/')
class RolePermissionsList(Resource):
    # get method using for get all RolePermissions in RolePermissions table
    @api.doc('list_of_registered_RolePermissions')
    @api.marshal_list_with(_RolePermissions, envelope='data')
    def get(self):
        """List all registered RolePermissions"""
        return get_all_RolePermissions()
    # post method using for craete the new RolePermissions in RolePermissions table
    @api.response(201, 'RolePermissions successfully created.')
    @api.doc('create a new RolePermissions')
    @api.expect(_RolePermissions, validate=True)
    def post(self):
        """Creates a new RolePermissions """
        data = request.json
        return save_new_RolePermissions(data=data)


@api.route('/<RolePermissionId>')
@api.param('RolePermissionId', 'The RolePermissions identifier') # A decorator to specify one of the expected parameters
@api.response(404, 'RolePermissions not found.')
class RolePermissions(Resource):
    # get method using for get one data in RolePermissions table 
    @api.doc('get a RolePermissions')
    @api.marshal_with(_RolePermissions)
    def get(self, RolePermissionId):
        """get a RolePermissions given its identifier"""
        user = get_a_RolePermissions(RolePermissionId)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return get_a_RolePermissions(data=data)
    # put method using in the RolePermissions table 
    @api.response(201, 'RolePermissions successfully update.')
    @api.doc('successfully update new RolePermissions')
    @api.expect(_RolePermissions, validate=True)
    def put(self, RolePermissionId):
        """RolePermissions Updated"""
        user = complete_RolePermissions(RolePermissionId)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return complete_RolePermissions(data=data)
    # delete method using for the delete elements the RolePermissions table 
    @api.response(201, 'RolePermissions successfully Deleted.')
    @api.doc('Delete RolePermissions successfully')
    @api.expect(_RolePermissions, validate=True)
    def delete(self, RolePermissionId):
        """RolePermissions Deleted"""
        user = delete_RolePermissions(RolePermissionId)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return delete_RolePermissions(data=data)