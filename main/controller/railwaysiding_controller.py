#imports all the required resources for the railwaysiding controller.
#We defined two concrete classes in our railwaysiding controller which are
#railwaysidingList and railwaysiding. These two classes extends the abstract flask-restplus resource.

from flask import request
from flask_restplus import Resource

from ..util.dto import RailwaysidingDto
from ..service.railwaysiding_service import save_new_railwaysiding, get_a_railwaysiding, get_all_railwaysiding, complete_railwaysiding, delete_railwaysiding

api = RailwaysidingDto.api
_railwaysiding = RailwaysidingDto.railwaysiding


@api.route('/')
class railwaysidingList(Resource):
     # get method using for get all user in railwaysiding table
    @api.doc('list_of_registered_railwaysiding')
    @api.marshal_list_with(_railwaysiding, envelope='data')
    def get(self):
        """List all registered railwaysiding"""
        return get_all_railwaysiding()

    # post method using for craete the new user in railwaysiding table
    @api.response(201, 'railwaysiding successfully created.')
    @api.doc('create a new railwaysiding')
    @api.expect(_railwaysiding, validate=True)
    def post(self):
        """Creates a new railwaysiding """
        data = request.json
        return save_new_railwaysiding(data=data)


@api.route('/<entryid>')
@api.param('entryid', 'The railwaysiding identifier') # A decorator to specify one of the expected parameters
@api.response(404, 'railwaysiding not found.')
class Railwaysiding(Resource):
    # get method using for get one data in railwaysiding table 
    @api.doc('get a railwaysiding')
    @api.marshal_with(_railwaysiding)
    def get(self, entryid):
        """get a railwaysiding given its identifier"""
        user = get_a_railwaysiding(entryid)
        if not user:
            api.abort(404)
        else:
            return user

    # put method using in the railwaysiding table
    @api.response(201, 'railwaysiding successfully update.')
    @api.doc('update railwaysiding')
    @api.expect(_railwaysiding, validate=True)
    def put(self,entryid):
        """updated railwaysiding """
        user = complete_railwaysiding(entryid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return complete_railwaysiding(data=data)

    # delete method using for the delete elements the railwaysiding table
    @api.response(201, 'railwaysiding successfully deleted.')
    @api.doc('deleted railwaysiding')
    @api.expect(_railwaysiding, validate=True)
    def delete(self, entryid):
        """deleted railwaysiding """
        user = delete_railwaysiding(entryid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return delete_railwaysiding(data=data)