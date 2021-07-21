#imports all the required resources for the Roles controller.
#We defined two concrete classes in our Roles controller which are
#RolesList and Roles. These two classes extends the abstract flask-restplus resource.

from flask import request
from flask_restplus import Resource

from ..util.dto import RolesDto
from ..service.Roles_service import get_a_Roles, get_all_Roles, save_new_Roles , complete_Roles, delete_Roles

api = RolesDto.api
_Roles = RolesDto.Roles


@api.route('/')
class RolesList(Resource):
    # get method using for get all Roles in Roles table
    @api.doc('list_of_registered_Roles')
    @api.marshal_list_with(_Roles, envelope='data')
    def get(self):
        """List all registered Roles"""
        return get_all_Roles()
    # post method using for craete the new Roles in Roles table
    @api.response(201, 'Roles successfully created.')
    @api.doc('create a new Roles')
    @api.expect(_Roles, validate=True)
    def post(self):
        """Creates a new Roles """
        data = request.json
        return save_new_Roles(data=data)


@api.route('/<RoleId>')
@api.param('RoleId', 'The Roles identifier') # A decorator to specify one of the expected parameters
@api.response(404, 'Roles not found.')
class Roles(Resource):
    # get method using for get one data in Roles table 
    @api.doc('get a Roles')
    @api.marshal_with(_Roles)
    def get(self, RoleId ):
        """get a Roles given its identifier"""
        user = get_a_Roles(RoleId )
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return get_a_Roles(data=data)
    # put method using in the users table 
    @api.response(201, 'Roles successfully update.')
    @api.doc('successfully update new Roles')
    @api.expect(_Roles, validate=True)
    def put(self, RoleId ):
        """Roles Updated"""
        user = complete_Roles(RoleId )
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return complete_Roles(data=data)
    # delete method using for the delete elements the users table 
    @api.response(201, 'Roles successfully Deleted.')
    @api.doc('Delete Roles successfully')
    @api.expect(_Roles, validate=True)
    def delete(self, RoleId ):
        """Roles Deleted"""
        user = delete_Roles(RoleId )
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return delete_Roles(data=data)