from src.database import User


def test_home(client, app):
    response = client.post("/register", data={"first_name": 'camilo', "last_name": 'castrillon', "phone_number": '3107282539', "email": 'camilo111@gmail.com',
                           "username": 'ccastrrr', "password": 'Holaporque1312', "neighborhood": 'olimpico', "city": 'Barrio',  "department": 'valle', "img": 'a nice picture'})

    with app.app_context():
        # user = User()
        # assert user.id == 1
        assert User.query.first().first_name == 'camilo'
        assert User.query.first().last_name == 'castrillon'
        assert User.query.first().phone_number == '3107282539'
        assert User.query.first().email == 'camilo111@gmail.com'
        assert User.query.first().username == 'ccastrrr'
        assert User.query.first().password != 'Holaporque1312'
        assert User.query.first().neighborhood == 'olimpico'
        assert User.query.first().department == 'valle'
        assert User.query.first().city == 'Barrio'
        assert User.query.first().img == 'a nice picture'
