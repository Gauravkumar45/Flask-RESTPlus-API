#imports all the required resources for the rfidtag controller.
#We defined two concrete classes in our rfidtag controller which are
#rfidtagList and rfidtag. These two classes extends the abstract flask-restplus resource.

from flask import request
from flask_restplus import Resource

from ..util.dto import RfidtagDto
from ..service.rfidtag_service import get_a_user, get_all_users, save_new_user , complete_users, delete_user

api = RfidtagDto.api
_rfidtag = RfidtagDto.rfidtag


@api.route('/')
class RfidtagList(Resource):
    # get method using for get all user in rfidtag table
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_rfidtag, envelope='data')
    def get(self):
        """List all registered Rfidtag"""
        return get_all_users()

    # post method using for craete the new user in rfidtag table
    @api.response(201, 'rfidtag successfully created.')
    @api.doc('create a new Rfidtag')
    @api.expect(_rfidtag, validate=True)
    def post(self):
        """Creates a rfidtag """
        data = request.json
        return save_new_user(data=data)


@api.route('/<rfid>')
@api.param('rfid', 'The rfidtag identifier') # A decorator to specify one of the expected parameters
@api.response(404, 'rfidtag not found.')
class Rfidtag(Resource):
    # get method using for get one data in rfidtag table
    @api.doc('get a user')
    @api.marshal_with(_rfidtag)
    def get(self, rfid):
        """get a user given its identifier"""
        user = get_a_user(rfid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return get_a_user(data=data)

    # put method using in the rfidtag table 
    @api.response(201, 'Rfidtag successfully update.')
    @api.doc('update new rfidtag')
    @api.expect(_rfidtag, validate=True)
    def put(self, rfid):
        """rfidtag updated"""
        user = complete_users(rfid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return complete_users(data=data)

    # delete method using for the delete elements the rfidtag table
    @api.response(201, 'rfidtag successfully Deleted.')
    @api.doc('Delete rfidtag')
    @api.expect(_rfidtag, validate=True)
    def delete(self, rfid):
        """rfidtag deleted"""
        user = delete_user(rfid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return delete_user(data=data)