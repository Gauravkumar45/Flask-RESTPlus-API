#imports all the required resources for the outgate controller.
#We defined two concrete classes in our outgate controller which are
#outgateList and outgate. These two classes extends the abstract flask-restplus resource.

from flask import request
from flask_restplus import Resource

from ..util.dto import OutgateDto
from ..service.outgate_service import get_a_user, get_all_users, save_new_user , complete_users, delete_user

api = OutgateDto.api
_outgate = OutgateDto.outgate


@api.route('/')
class OutgateList(Resource):
    # get method using for get all user in outgate table
    @api.doc('list_of_registered_outgate')
    @api.marshal_list_with(_outgate, envelope='data')
    def get(self):
        """List all registered outgate"""
        return get_all_users()

    # post method using for craete the new user in outgate table
    @api.response(201, 'Outgate successfully created.')
    @api.doc('create a new outgate')
    @api.expect(_outgate, validate=True)
    def post(self):
        """Creates a new outgate """
        data = request.json
        return save_new_user(data=data)


@api.route('/<challanid>')
@api.param('challanid', 'The outgate identifier') #A decorator to specify one of the expected parameters
@api.response(404, 'outgate not found.')
class Outgate(Resource):
    # get method using for get one data in outgate table 
    @api.doc('get a outgate')
    @api.marshal_with(_outgate)
    def get(self, challanid):
        """get a user given its identifier"""
        user = get_a_user(challanid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return get_a_user(data=data)

    # put method using in the outgate table
    @api.response(201, 'outgate successfully update.')
    @api.doc('update new outgate')
    @api.expect(_outgate, validate=True)
    def put(self, challanid):
        """outgate updated"""
        user = complete_users(challanid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return complete_users(data=data)

    # delete method using for the delete elements the outgate table
    @api.response(201, 'outgate successfully Deleted.')
    @api.doc('Delete outgate')
    @api.expect(_outgate, validate=True)
    def delete(self, challanid):
        """outgate deleted"""
        user = delete_user(challanid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return delete_user(data=data)