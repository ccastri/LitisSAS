import pytest
from src import create_app
from src.database import User


# @pytest.fixture(scope="session")
# def flask_app():
#     app = create_app()
#     client = app.test_client
#     ctx = app.test_request_context()
#     ctx.push()

#     yield client
#     ctx.pop()


@pytest.fixture(scope='module')
def new_user():
    user = User('camilo', 'castrillon', 'camiloc@gmail.com', 'Holaporque1312',
                'ccastrrri', '3107282539', 'olimpico', 'valle', 'cali', 'a nice picture')
    return user
