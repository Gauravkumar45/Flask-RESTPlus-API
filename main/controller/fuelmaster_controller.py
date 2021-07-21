#imports all the required resources for the fuelmaster controller.
#We defined two concrete classes in our fuelmaster controller which are
#fuelmasterList and fuelmaster. These two classes extends the abstract flask-restplus resource.

from flask import request
from flask_restplus import Resource

from ..util.dto import fuelmasterDto
from ..service.fuelmaster_service import get_a_fuelmaster, get_all_fuelmaster, save_new_fuelmaster , complete_fuelmaster, delete_fuelmaster

api = fuelmasterDto.api
_fuelmaster = fuelmasterDto.fuelmaster


@api.route('/')
class fuelmasterList(Resource):
    # get method using for get all user in fuelmaster table
    @api.doc('list_of_registered_fuelmaster')
    @api.marshal_list_with(_fuelmaster, envelope='data')
    def get(self):
        """List all registered fuelmaster"""
        return get_all_fuelmaster()
    # post method using for craete the new user in fuelmaster table
    @api.response(201, 'fuelmaster successfully created.')
    @api.doc('create a new fuelmaster')
    @api.expect(_fuelmaster, validate=True)
    def post(self):
        """Creates a new fuelmaster """
        data = request.json
        return save_new_fuelmaster(data=data)


@api.route('/<fuelid>')
@api.param('fuelid', 'The fuelmaster identifier') # A decorator to specify one of the expected parameters
@api.response(404, 'fuelmaster not found.')
class Fuelmaster(Resource):
    # get method using for get one data in fuelmaster table 
    @api.doc('get a fuelmaster')
    @api.marshal_with(_fuelmaster)
    def get(self, fuelid):
        """get a fuelmaster given its identifier"""
        user = get_a_fuelmaster(fuelid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return get_a_fuelmaster(data=data)
    # put method using in the fuelmaster table 
    @api.response(201, 'fuelmaster successfully update.')
    @api.doc('successfully update new fuelmaster')
    @api.expect(_fuelmaster, validate=True)
    def put(self, fuelid):
        """fuelmaster Updated"""
        user = complete_fuelmaster(fuelid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return complete_fuelmaster(data=data)
    # delete method using for the delete elements the fuelmaster table 
    @api.response(201, 'fuelmastersuccessfully Deleted.')
    @api.doc('Delete fuelmaster')
    @api.expect(_fuelmaster, validate=True)
    def delete(self, fuelid):
        """fuelmaster Deleted"""
        user = delete_fuelmaster(fuelid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return delete_fuelmaster(data=data)