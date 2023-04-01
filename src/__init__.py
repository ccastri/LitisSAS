from flask import Flask
import os
from src.database import db
from src.auth import auth
from src.plans import plans
from flask_jwt_extended import JWTManager
from flask_cors import CORS, cross_origin


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    if test_config is None:

        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DB_URI"),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            JWT_SECRET_KEY=os.environ.get("JWT_SECRET_KEY")
        )

    #!Test config defined
    else:
        app.config.from_mapping(test_config)
    #!Blueprint for url pointing (RouterModule):
    app.register_blueprint(auth)
    app.register_blueprint(plans)
    #!JWT Middleware connection:
    JWTManager(app)
    #!Database extension and initialization
    db.app = app
    db.init_app(app)

    return app
