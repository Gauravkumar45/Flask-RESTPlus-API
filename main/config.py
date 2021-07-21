# the config file contains three environment setup classes which include testing, development and  production.  

import os
import psycopg2
from psycopg2 import Error

try:
    # Connect to an existing databse
    connection = psycopg2.connect(user="postgres",password="12345",host="127.0.0.1",port="5432",database="dms")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print postgresSQL detailes
    print("PostgresSQL server information")
    print(connection.get_dsn_parameters(),"\n")
    # Eexcuting a SQL query
    cursor.execute("select version();")
    #fetch results
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, Error) as error:
    print("Error while connecting to postgresSQL",error) 


# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = postgres_local_base

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY