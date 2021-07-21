from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/dms'
    return app

from flask_restplus import Api
from flask import Blueprint

# from controllers files importing the api as user_ns
from main.controller.users_controller import api as users_ns
# from controllers files importing the api as locations_ns
from main.controller.locations_controller import api as locations_ns
# from controllers files importing the api as drivers_ns
from main.controller.drivers_controller import api as drivers_ns
# from controllers files importing the api as railwaysiding_ns
from main.controller.railwaysiding_controller import api as railwaysiding_ns
# from controllers files importing the api as owner_ns
from main.controller.owners_controller import api as owners_ns
# from controllers files importing the api as vehicles_ns
from main.controller.vehicles_controller import api as vehicles_ns
# from controllers files importing the api as weightbridge_ns
from main.controller.weighbridge_controller import api as weighbridge_ns
# from controllers files importing the api as ingate_ns
from main.controller.ingate_controller import api as ingate_ns
# from controllers files importing the api as fuelgate_ns
from main.controller.fuelgate_controller import api as fuelgate_ns
# from controllers files importing the api as userpermissions_ns
from main.controller.userpermissions_controller import api as userpermissions_ns
# from controllers files importing the api as outgate_ns
from main.controller.outgate_controller import api as outgate_ns
# from controllers files importing the api as category_ns
from main.controller.category_controller import api as category_ns
# from controllers files importing the api as rfidtag_ns
from main.controller.rfidtag_controller import api as rfidtag_ns
# from controllers files importing the api as assets_ns
from main.controller.assets_controller import api as assets_ns
# from controllers files importing the api as company_ns
from main.controller.company_controller import api as company_ns
# from controllers files importing the api as fuelmaster_ns
from main.controller.fuelmaster_controller import api as fuelmaster_ns
# from controllers files importing the api as RolePermissions_ns
from main.controller.RolePermissions_controller import api as RolePermissions_ns
# from controllers files importing the api as UserRoles_ns
from main.controller.UserRoles_controller import api as UserRoles_ns
# from controllers files importing the api as Roles_ns
from main.controller.Roles_controller import api as Roles_ns
# from controllers files importing the api as users_app_ns
from main.controller.users_app_controller import api as users_app_ns

blueprint = Blueprint('api', __name__)

#API is the main entry point for the application resources and hence needs to be initialized with the blueprint
api = Api(blueprint,
          title='DMS',
          version='',
          description=''
          )
  
#  we add the user namespace user_ns to the list of namespaces in the API instance.
api.add_namespace(users_ns, path='/users')
#  we add the locations namespace locations_ns to the list of namespaces in the API instance.
api.add_namespace(locations_ns, path='/locations')
#  we add the drivers namespace drivers_ns to the list of namespaces in the API instance.
api.add_namespace(drivers_ns, path='/drivers')
#  we add the railwaysiding namespace railwaysiding_ns to the list of namespaces in the API instance.
api.add_namespace(railwaysiding_ns, path='/railwaysiding')
#  we add the owner namespace owner_ns to the list of namespaces in the API instance.
api.add_namespace(owners_ns, path='/owners')
#  we add the vehicles namespace vehicles_ns to the list of namespaces in the API instance.
api.add_namespace(vehicles_ns, path='/vehicles')
#  we add the weightbridge namespace weightbridge_ns to the list of namespaces in the API instance.
api.add_namespace(weighbridge_ns, path='/weighbridge')
#  we add the ingate namespace ingate_ns to the list of namespaces in the API instance.
api.add_namespace(ingate_ns, path='/ingate')
#  we add the fuelgate namespace fuelgate_ns to the list of namespaces in the API instance.
api.add_namespace(fuelgate_ns, path='/fuelgate')
#  we add the userpermissions namespace userpermissions_ns to the list of namespaces in the API instance.
api.add_namespace(userpermissions_ns, path='/userpermissions')
#  we add the outgate namespace outgate_ns to the list of namespaces in the API instance.
api.add_namespace(outgate_ns, path='/outgate')
#  we add the category namespace category_ns to the list of namespaces in the API instance.
api.add_namespace(category_ns, path='/category')
#  we add the rfidtag namespace rfidtag_ns to the list of namespaces in the API instance.
api.add_namespace(rfidtag_ns, path='/rfidtag')
#  we add the assets namespace assets_ns to the list of namespaces in the API instance.
api.add_namespace(assets_ns, path='/assets')
#  we add the company namespace exceptions_ns to the list of namespaces in the API instance.
api.add_namespace(company_ns, path='/company')
#  we add the fuelmaster namespace exceptions_ns to the list of namespaces in the API instance.
api.add_namespace(fuelmaster_ns, path='/fuelmaster')
#  we add the userpermissions namespace exceptions_ns to the list of namespaces in the API instance.
api.add_namespace(userpermissions_ns, path='/userpermissions')
#  we add the RolePermissions namespace exceptions_ns to the list of namespaces in the API instance.
api.add_namespace(RolePermissions_ns, path='/RolePermissions')
#  we add the UserRoles namespace exceptions_ns to the list of namespaces in the API instance.
api.add_namespace(UserRoles_ns, path='/UserRoles')
#  we add the Roles namespace exceptions_ns to the list of namespaces in the API instance.
api.add_namespace(Roles_ns, path='/Roles')
#  we add the users_app namespace exceptions_ns to the list of namespaces in the API instance.
api.add_namespace(users_app_ns, path='/users_app')


