from flask import Flask
import os
from src.database import db
from src.auth import auth
from src.plans import plans
from datetime import timedelta
# from routes.userRoutes import dashboard
from flask_jwt_extended import JWTManager
from flask_cors import CORS


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app, resources={
         r"/*": {"origins": "http://localhost:3000"}})

    if test_config is None:

        app.config.from_mapping(
            DEBUG=True,
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DB_URI"),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            JWT_SECRET_KEY=os.environ.get("JWT_SECRET_KEY"),
            JWT_ACCESS_TOKEN_EXPIRES=timedelta(hours=1),
        )

    #!Test config defined
    else:
        app.config.from_mapping(test_config)
    #!Blueprint for url pointing (RouterModule):
    app.register_blueprint(auth)
    # app.register_blueprint(dashboard)
    app.register_blueprint(plans)
    #!JWT Middleware connection:
    JWTManager(app)
    #!Database extension and initialization
    db.app = app
    db.init_app(app)

    return app
