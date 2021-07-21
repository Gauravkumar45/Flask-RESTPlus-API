#imports all the required resources for the owner controller.
#We defined two concrete classes in our owner controller which are
#ownerList and owner. These two classes extends the abstract flask-restplus resource.

from flask import request
from flask_restplus import Resource

from ..util.dto import OwnersDto
from ..service.owners_service import save_new_user, get_a_user,get_all_users, complete_owner, delete_owner

api = OwnersDto.api
_owners = OwnersDto.owners

@api.route('/')
class  OwnersList(Resource):
    # get method using for get all user in owner table
    @api.doc('list_of_registered_Owners')
    @api.marshal_list_with(_owners, envelope='data')
    def get(self):
        """List all registered Owners"""
        return get_all_users()

    # post method using for craete the new user in owner table
    @api.response(201, 'owner successfully created.')
    @api.doc('create a new owner')
    @api.expect(_owners, validate=True)
    def post(self):
        """Creates a new owners """
        data = request.json
        return save_new_user(data=data)

@api.route('/<ownerid>')
@api.param('ownerid', 'The User identifier') # A decorator to specify one of the expected parameters
@api.response(404, 'User not found.')
class Owner(Resource):
    # get method using for get one data in owner table
    @api.doc('get a owner')
    @api.marshal_with(_owners)
    def get(self, ownerid):
        """get a user given its identifier"""
        user = get_a_user(ownerid)
        if not user:
            api.abort(404)
        else:
            return user

    # put method using in the owner table
    @api.response(201, 'owner successfully update.')
    @api.doc('update owner')
    @api.expect(_owners, validate=True)
    def put(self, ownerid):
        """update owner """
        user = complete_owner(ownerid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return complete_owner(data=data)

    # delete method using for the delete elements the owner table
    @api.response(201, 'owner successfully delete.')
    @api.doc('delete owner')
    @api.expect(_owners, validate=True)
    def delete(self, ownerid):
        """delete owner """
        user = delete_owner(ownerid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return delete_owner(data=data)