import pytest
from src import create_app
from src.database import User, db


@pytest.fixture()
# def test_client():
def app():
    app = create_app(
        {"TESTING": True, "SQLALCHEMY_DATABASE_URI": "mysql://root:ccastri@localhost/litis"})
    # app.config.update({
    #     "TESTING": True,
    # })
# app.config[]

    with app.app_context():
        db.create_all()
    yield app

    # client = app.test_client
    # ctx = app.test_request_context()
    # ctx.push()

    # yield client
    # ctx.pop()


@pytest.fixture()
def client(app):

    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


@pytest.fixture(scope='module')
def new_user():
    user = User('camilo', 'castrillon', 'camiloc@gmail.com', 'Holaporque1312',
                'ccastrrri', '3107282539', 'olimpico', 'valle', 'cali', 'a nice picture')
    return user
