import os
import unittest
import psycopg2
from psycopg2 import Error

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

#importing blueprint and registering it with the Flask application instance.
from main import blueprint
## create_app function we created initially to create the application instance with the required parameter from the environment variable which can be either of the following - dev, prod, test. If none is set in the environment variable
from main import create_app, db
#importing filers to communicate each other.
from main.model import users
from main.model import railwaysiding
from main.model import owners
from main.model import ingate
from main.model import vehicles
from main.model import weighbridge
from main.model import locations
from main.model import fuelgate
from main.model import userpermissions
from main.model import assets
from main.model import category
from main.model import rfidtag
from main.model import outgate
from main.model import company
from main.model import fuelmaster
from main.model import Languages

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()
app.config['SQLALCHEMY_DATABSE_URI'] = "postgres://postgres:postgres@localhost:5432/1006"

#instantiates the manager classes by passing the app instance to their respective constructors.
manager = Manager(app)

#instantiates the  migrate classes by passing the app instance to their respective constructors.
migrate = Migrate(app, db)

#we pass the db and MigrateCommandinstances to the add_command interface of the managerto expose all the database migration commands through Flask-Script
manager.add_command('db', MigrateCommand)

#marks the two functions as executable from the command line.
@manager.command
def run():
    app.run()

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()