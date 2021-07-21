#imports all the required resources for the fuelgate controller.
#We defined two concrete classes in our fuelgate  controller which are
#fuelgate List and fuelgate . These two classes extends the abstract flask-restplus resource.

from flask import request
from flask_restplus import Resource

from ..util.dto import FuelgateDto
from ..service.fuelgate_service import get_a_user, get_all_users, save_new_user , complete_users, delete_user

api = FuelgateDto.api
_fuelgate = FuelgateDto.fuelgate


@api.route('/')
class FuelgateList(Resource):
    # get method using for get all user in fuelgate table
    @api.doc('list_of_registered_Fuelgate')
    @api.marshal_list_with(_fuelgate, envelope='data')
    def get(self):
        """List all registered Fuelgate"""
        return get_all_users()

    # post method using for craete the new user in fuelgate table
    @api.response(201, 'Fuelgate successfully created.')
    @api.doc('create a new Fuelgate')
    @api.expect(_fuelgate, validate=True)
    def post(self):
        """Creates a new Fuelgate """
        data = request.json
        return save_new_user(data=data)


@api.route('/<fuelid>')
@api.param('fuelid', 'The Fuelgate identifier') #A decorator to specify one of the expected parameters
@api.response(404, 'Fuelgate not found.')
class Fuelgate(Resource):
    # get method using for get one data in fuelgate table
    @api.doc('get a Fuelgate')
    @api.marshal_with(_fuelgate)
    def get(self, fuelid):
        """get a Fuelgate given its identifier"""
        user = get_a_user(fuelid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return get_a_user(data=data)

    # put method using in the fuelgate  table 
    @api.response(201, 'Fuelgate successfully update.')
    @api.doc('update new Fuelgate')
    @api.expect(_fuelgate, validate=True)
    def put(self, fuelid):
        """Fuelgate Updated"""
        user = complete_users(fuelid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return complete_users(data=data)

    # delete method using for the delete elements the fuelgate table
    @api.response(201, 'Fuelgate successfully Deleted.')
    @api.doc('Delete Fuelgate')
    @api.expect(_fuelgate, validate=True)
    def delete(self, fuelid):
        """Fuelgate Deleted"""
        user = delete_user(fuelid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return delete_user(data=data)