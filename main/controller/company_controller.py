#imports all the required resources for the Company controller.
#We defined two concrete classes in our Company controller which are
#CompanyList and Company. These two classes extends the abstract flask-restplus resource.

from flask import request
from flask_restplus import Resource

from ..util.dto import CompanyDto
from ..service.company_service import get_a_Company, get_all_Company, save_new_Company, complete_Company, delete_Company

api = CompanyDto.api
_Company = CompanyDto.Company


@api.route('/')
class CompanyList(Resource):
    # get method using for get all Company in Company table
    @api.doc('list_of_registered_Company')
    @api.marshal_list_with(_Company, envelope='data')
    def get(self):
        """List all registered Company"""
        return get_all_Company()
    # post method using for craete the new Company in Company table
    @api.response(201, 'Company successfully created.')
    @api.doc('create a new Company')
    @api.expect(_Company, validate=True)
    def post(self):
        """Creates a new Company"""
        data = request.json
        return save_new_Company(data=data)


@api.route('/<cid>')
@api.param('cid', 'The Company identifier') # A decorator to specify one of the expected parameters
@api.response(404, 'Company not found.')
class Company(Resource):
    # get method using for get one data in Company table 
    @api.doc('get a Company')
    @api.marshal_with(_Company)
    def get(self, cid):
        """get a Company given its identifier"""
        user = get_a_Company(cid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return get_a_Company(data=data)
    # put method using in the Company table 
    @api.response(201, 'Company successfully update.')
    @api.doc('successfully update new Company')
    @api.expect(_Company, validate=True)
    def put(self, cid):
        """Company Updated"""
        user = complete_Company(cid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return complete_Company(data=data)
    # delete method using for the delete elements the Company table 
    @api.response(201, 'Company successfully Deleted.')
    @api.doc('Delete Company successfully')
    @api.expect(_Company, validate=True)
    def delete(self, cid):
        """Company Deleted"""
        user = delete_Company(cid)
        if not user:
            api.abort(404)
        else:
            return user
        data = request.json
        return delete_Company(data=data)