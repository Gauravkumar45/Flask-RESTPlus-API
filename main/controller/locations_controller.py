#imports all the required resources for the locations controller.
#We defined two concrete classes in our locations controller which are
#locationsList and locations. These two classes extends the abstract flask-restplus resource.

from flask import request
from flask_restplus import Resource

from ..util.dto import LocationsDto
from ..service.locations_service import save_new_user, get_a_user, get_all_users, complete_locations, delete_locations

api = LocationsDto.api
_locations = LocationsDto.locations


@api.route('/')
class LocationsList(Resource):
    # get method using for get all user in locations table
    @api.doc('list_of_registered_locations')
    @api.marshal_list_with(_locations, envelope='data')
    def get(self):
        """List all registered locations"""
        return get_all_users()

    # post method using for craete the new user in locations table
    @api.response(201, 'locations successfully created.')
    @api.doc('create a new locations')
    @api.expect(_locations, validate=True)
    def post(self):
        """Creates a new locations """
        data = request.json
        return save_new_user(data=data)


@api.route('/<locationid>')
@api.param('locationid', 'The locations identifier') #A decorator to specify one of the expected parameters
@api.response(404, 'locations not found.')
class Locations(Resource):
    # get method using for get one data in locations table 
    @api.doc('get a locations')
    @api.marshal_with(_locations)
    def get(self, locationid):
        """get a locations given its identifier"""
        user = get_a_user(locationid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return get_a_user(data=data)

    # put method using in the locations table 
    @api.response(201, 'locations successfully updated.')
    @api.doc('update locations')
    @api.expect(_locations, validate=True)
    def put(self, locationid):
        """locations Update"""
        user = complete_locations(locationid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return complete_locations(data=data)

    # delete method using for the delete elements the locations table
    @api.response(201, 'locations successfully deleted.')
    @api.doc('deleted locations')
    @api.expect(_locations, validate=True)
    def delete(self, locationid):
        """locations Deleted"""
        user = delete_locations(locationid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return delete_locations(data=data)