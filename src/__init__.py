from flask import Flask
import os


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:

        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
        )

    #!Test config defined
    else:
        app.config.from_mapping(test_config)

    @app.route('/get2', methods=['GET'])
    def get_allLitisPackages():
        return {"hello": "world"}

    return app
