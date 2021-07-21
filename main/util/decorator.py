from functools import wraps
from flask import request

from main.service.users_service import Users


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Users.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status

        return f(*args, **kwargs)

    return decorated


def admin_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Users.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status

        admin = token.get('admin')
        if not admin:
            response_object = {
                'status': 'fail',
                'message': 'user token required'
            }
            return response_object, 401

        return f(*args, **kwargs)

    return decorated