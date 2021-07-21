#imports all the required resources for the category controller.
#We defined two concrete classes in our category controller which are
#categoryList and category. These two classes extends the abstract flask-restplus resource.

from flask import request
from flask_restplus import Resource

from ..util.dto import CategoryDto
from ..service.category_service import get_a_user, get_all_users, save_new_user , complete_users, delete_user

api = CategoryDto.api
_category = CategoryDto.category


@api.route('/')
class CategoryList(Resource):
    # get method using for get all user in category table
    @api.doc('list_of_registered_Category')
    @api.marshal_list_with(_category, envelope='data')
    def get(self):
        """List all registered Category"""
        return get_all_users()

    # post method using for craete the new user in category table
    @api.response(201, 'Category successfully created.')
    @api.doc('create a new Category')
    @api.expect(_category, validate=True)
    def post(self):
        """Creates a new Category """
        data = request.json
        return save_new_user(data=data)


@api.route('/<categoryid>')
@api.param('categoryid', 'The Category identifier') #A decorator to specify one of the expected parameters
@api.response(404, 'Category not found.')
class Category(Resource):
    # get method using for get one data in category table 
    @api.doc('get a Category')
    @api.marshal_with(_category)
    def get(self, categoryid):
        """get a Category given its identifier"""
        user = get_a_user(categoryid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return get_a_user(data=data)

    # put method using in the category table 
    @api.response(201, 'Categorysuccessfully update.')
    @api.doc('update new Category')
    @api.expect(_category, validate=True)
    def put(self, categoryid):
        """Category Updated"""
        user = complete_users(categoryid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return complete_users(data=data)

    # delete method using for the delete elements the category table
    @api.response(201, 'Category successfully Deleted.')
    @api.doc('Delete Category')
    @api.expect(_category, validate=True)
    def delete(self, categoryid):
        """Category Deleted"""
        user = delete_user(categoryid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return delete_user(data=data)