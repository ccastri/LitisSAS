from flask import Flask
import os
from src.database import db
from src.auth import auth
from src.plans import plans


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:

        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DB_URI"),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
        )

    #!Test config defined
    else:
        app.config.from_mapping(test_config)

    # @app.route('/register', methods=['POST'])
    # def register_new_user():
    #     return {"hello": "world"}

    app.register_blueprint(auth)
    app.register_blueprint(plans)
    db.app = app
    db.init_app(app)

    return app
