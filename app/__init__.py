from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from config import *

db = SQLAlchemy()

def create_app(config_class = DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    from app.controller.cbas_api import bp as cbasapi_bp
    from app.controller.cbas_api.cbas_controller import tot

    api = Api(cbasapi_bp, title='CBAS API', version='1.0', description='Uji Coba Awal')
    api.add_namespace(tot)
    app.register_blueprint(cbasapi_bp)

    from app.controller.pdmodel import bp as pdmodel_bp
    from app.controller.pdmodel.slik_controller import pd

    api2 = Api(pdmodel_bp, title='PD Model API', version='12.0', description='Uji Coba Awal')
    api2.add_namespace(pd)
    app.register_blueprint(pdmodel_bp)

    return app

from app import db_models