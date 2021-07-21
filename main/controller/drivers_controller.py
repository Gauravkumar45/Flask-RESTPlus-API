#imports all the required resources for the drivers controller.
#We defined two concrete classes in our drivers controller which are
#driversList and drivers. These two classes extends the abstract flask-restplus resource.

from flask import request
from flask_restplus import Resource

from ..util.dto import DriversDto
from ..service.drivers_service import save_new_user, get_all_users, get_a_user, complete_drivers, delete_drivers

api = DriversDto.api
_drivers = DriversDto.drivers


@api.route('/')
class DriversList(Resource):
    # get method using for get all user in drivers table
    @api.doc('list_of_registered_Drivers')
    @api.marshal_list_with(_drivers, envelope='data')
    def get(self):
        """List all registered Drivers"""
        return get_all_users()

    # post method using for craete the new user in drivers table
    @api.response(201, 'Drivers successfully created.')
    @api.doc('create a new Drivers')
    @api.expect(_drivers, validate=True)
    def post(self):
        """Creates a new Drivers """
        data = request.json
        return save_new_user(data=data)

@api.route('/<driverid>')
@api.param('driverid', 'The Drivers identifier') #A decorator to specify one of the expected parameters
@api.response(404, 'Drivers not found.')
class Drivers(Resource):
    # get method using for get one data in drivers table 
    @api.doc('get a Drivers')
    @api.marshal_with(_drivers)
    def get(self, driverid):
        """get a Drivers given its identifier"""
        user = get_a_user(driverid)
        if not user:
            api.abort(404)
        else:
            return user

    # put method using in the drivers table
    @api.response(201, 'Drivers successfully updated.')
    @api.doc('update drivers successfully')
    @api.expect(_drivers, validate=True)
    def put(self, driverid):
        """Drivers Update"""
        user = complete_drivers(driverid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return complete_drivers(data=data)

    # delete method using for the delete elements the drivers table
    @api.response(201, 'drivers successfully deleted.')
    @api.doc('deleted drivers successfully')
    @api.expect(_drivers, validate=True)
    def delete(self, driverid):
        """Drivers Deleted"""
        user = delete_drivers(driverid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return delete_drivers(data=data)