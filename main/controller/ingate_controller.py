#imports all the required resources for the ingate controller.
#We defined two concrete classes in our ingate controller which are
#ingateList and ingate. These two classes extends the abstract flask-restplus resource.

from flask import request
from flask_restplus import Resource

from ..util.dto import IngateDto
from ..service.ingate_service import save_new_ingate, get_all_ingate, get_a_ingate , complete_ingate, delete_ingate

api = IngateDto.api
_ingate = IngateDto.ingate


@api.route('/')
class IngateList(Resource):
    # get method using for get all user in ingate table
    @api.doc('list_of_registered_ingate')
    @api.marshal_list_with(_ingate, envelope='data')
    def get(self):
        """List all registered inagte"""
        return get_all_ingate()

    # post method using for craete the new user in ingate table
    @api.response(201, 'ingate successfully created.')
    @api.doc('create a new inagte')
    @api.expect(_ingate, validate=True)
    def post(self):
        """Creates a new ingate """
        data = request.json
        return save_new_ingate(data=data)

@api.route('/<slipid>')
@api.param('slipid', 'The ingate identifier') #A decorator to specify one of the expected parameters
@api.response(404, 'ingate not found.')
class Ingate(Resource):
    # get method using for get one data in ingate table 
    @api.doc('get a ingate')
    @api.marshal_with(_ingate)
    def get(self, slipid):
        """get a ingate given its identifier"""
        user = get_a_ingate(slipid)
        if not user:
            api.abort(404)
        else:
            return user

    # put method using in the ingate table 
    @api.response(201, 'ingate successfully update.')
    @api.doc('update ingate')
    @api.expect(_ingate, validate=True)
    def put(self, slipid):
        """ingate Update"""
        user = complete_ingate(slipid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return complete_ingate(data=data)

    # delete method using for the delete elements the ingate table
    @api.response(201, 'ingate successfully delete.')
    @api.doc('delete ingate')
    @api.expect(_ingate, validate=True)
    def delete(self,slipid):
        """ingate Delete"""
        user = delete_ingate(slipid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return delete_ingate(data=data)