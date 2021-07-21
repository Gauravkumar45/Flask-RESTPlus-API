#imports all the required resources for the weightbridge controller.
#We defined two concrete classes in our weightbridge controller which are
#weightbridgeList and weightbridge. These two classes extends the abstract flask-restplus resource.

from flask import request
from flask_restplus import Resource

from ..util.dto import WeighbridgeDto
from ..service.weighbridge_service import save_new_user, get_all_users, get_a_user, complete_weighbridge, delete_weighbridge

api = WeighbridgeDto.api
_weighbridge = WeighbridgeDto.weighbridge

@api.route('/')
class WeighbridgeList(Resource):
    # get method using for get all user in weightbridge table
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_weighbridge, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    # post method using for craete the new user in weightbridge table
    @api.response(201, 'weighbridge successfully created.')
    @api.doc('create a new weighbridge')
    @api.expect(_weighbridge, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)

@api.route('/<wbid>')
@api.param('wbid', 'The weighbridge identifier') # A decorator to specify one of the expected parameters
@api.response(404, 'User not found.')
class Weighbridge(Resource):
    # get method using for get one data in weightbridge table
    @api.doc('get a user')
    @api.marshal_with(_weighbridge)
    def get(self, wbid):
        """get a user given its identifier"""
        user = get_a_user(wbid)
        if not user:
            api.abort(404)
        else:
            return user

    # put method using in the weighbridge table
    @api.response(201, 'Weighbridge successfully update.')
    @api.doc('Weighbridge successfully update')
    @api.expect(_weighbridge, validate=True)
    def put(self, wbid):
        """Weighbridge Update"""
        user = complete_weighbridge(wbid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return complete_weighbridge(data=data)

    # delete method using for the delete elements the weighbridge table
    @api.response(201, 'Weighbridge successfully delete.')
    @api.doc('Weighbridge successfully delete')
    @api.expect(_weighbridge, validate=True)
    def delete(self, wbid):
        """Weighbridge Delete"""
        user = delete_weighbridge(wbid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return delete_weighbridge(data=data)