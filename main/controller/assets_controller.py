#imports all the required resources for the assets controller.
#We defined two concrete classes in our assets controller which are
#assetsList and assets. These two classes extends the abstract flask-restplus resource.

from flask import request
from flask_restplus import Resource

from ..util.dto import AssetsDto
from ..service.assets_service import get_a_user, get_all_users, save_new_user , complete_users, delete_user

api = AssetsDto.api
_assets = AssetsDto.assets


@api.route('/')
class AssetsList(Resource):
    # get method using for get all user in assets table
    @api.doc('list_of_registered_Assets')
    @api.marshal_list_with(_assets, envelope='data')
    def get(self):
        """List all registered Assets"""
        return get_all_users()
    # post method using for craete the new user in assets table
    @api.response(201, 'Assets successfully created.')
    @api.doc('create a new Assets')
    @api.expect(_assets, validate=True)
    def post(self):
        """Creates a new Assets """
        data = request.json
        return save_new_user(data=data)


@api.route('/<assetid>')
@api.param('assetid', 'The Assets identifier') #A decorator to specify one of the expected parameters
@api.response(404, 'Assets not found.')
class Assets(Resource):
    # get method using for get one data in assets table 
    @api.doc('get a Assets')
    @api.marshal_with(_assets)
    def get(self, assetid):
        """get a Assets given its identifier"""
        user = get_a_user(assetid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return get_a_user(data=data)

    # put method using in the assets table
    @api.response(201, 'Assets successfully update.')
    @api.doc('update Assets')
    @api.expect(_assets, validate=True)
    def put(self, assetid):
        """Assets Updated"""
        user = complete_users(assetid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return complete_users(data=data)

    # delete method using for the delete elements the assets table
    @api.response(201, 'Assets successfully Deleted.')
    @api.doc('Delete Assets')
    @api.expect(_assets, validate=True)
    def delete(self, assetid):
        """Assets Deleted"""
        user = delete_user(assetid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return delete_user(data=data)