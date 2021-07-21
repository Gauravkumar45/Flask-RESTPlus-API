#imports all the required resources for the vehicles controller.
#We defined two concrete classes in our vehicles controller which are
#vehiclesList and vehicles. These two classes extends the abstract flask-restplus resource.

from flask import request
from flask_restplus import Resource

from ..util.dto import VehiclesDto
from ..service.vehicles_service import save_new_user, get_all_users, get_a_user, complete_vehicles, delete_vehicles

api = VehiclesDto.api
_vehicles = VehiclesDto.vehicles


@api.route('/')
class VehiclesList(Resource):
    # get method using for get all user in vehicles table
    @api.doc('list_of_registered_Vehicles')
    @api.marshal_list_with(_vehicles, envelope='data')
    def get(self):
        """List all registered Vehicles"""
        return get_all_users()

    # post method using for craete the new user in vehicles table
    @api.response(201, 'Vehicles successfully created.')
    @api.doc('create a new Vehicles')
    @api.expect(_vehicles, validate=True)
    def post(self):
        """Creates a new Vehicles """
        data = request.json
        return save_new_user(data=data)

@api.route('/<vehicleid>')
@api.param('vehicleid', 'The Vehicles identifier') # A decorator to specify one of the expected parameters
@api.response(404, 'Vehicles not found.')
class Vehicles(Resource):
    # get method using for get one data in vehicles table 
    @api.doc('get a Vehicles')
    @api.marshal_with(_vehicles)
    def get(self, vehicleid):
        """get a user given its identifier"""
        user = get_a_user(vehicleid)
        if not user:
            api.abort(404)
        else:
            return user

    # put method using in the vehicles table
    @api.response(201, 'vehicles successfully update.')
    @api.doc('update vehiclesr')
    @api.expect(_vehicles, validate=True)
    def put(self, vehicleid):
        """update vehicles """
        user = complete_vehicles(vehicleid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return complete_vehicles(data=data)

    # delete method using for the delete elements the vehicles table 
    @api.response(201, 'vehicles successfully update.')
    @api.doc('delete vehicles')
    @api.expect(_vehicles, validate=True)
    def delete(self, vehicleid):
        """Deleted Vehicles """
        user = delete_vehicles(vehicleid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return delete_vehicles(data=data)