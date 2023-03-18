from src.database import User, Plan


def test_new_plan():
    """
    GIVEN a User model
    WHEN a new user is created
    THEN check the email and password fields are defined correctly
    """

    plan = Plan('Fullyplannnn', 'lorem ipsum blablabla',
                '190000', 'nice img plan', 1)

    assert plan.name == 'Fullyplannnn'
    assert plan.description == 'lorem ipsum blablabla'
    assert plan.price == '190000'
    assert plan.img == 'nice img plan'
    assert plan.user_id == 1


def test_new_user():
    """
    GIVEN a User model
    WHEN a new user is created
    THEN check the email and password fields are defined correctly
    """

    user = User(1, 'camilo', 'castrillon', '3107282539', 'camiloc@gmail.com', 'ccastrrri',
                'Holaporque1312', 'olimpico', 'cali', 'valle', 'a nice picture')
    assert user.id == 1
    assert user.first_name == 'camilo'
    assert user.last_name == 'castrillon'
    assert user.phone_number == '3107282539'
    assert user.email == 'camiloc@gmail.com'
    assert user.username == 'ccastrrri'
    assert user.password == 'Holaporque1312'
    assert user.neighborhood == 'olimpico'
    assert user.department == 'valle'
    assert user.city == 'cali'
    assert user.img == 'a nice picture'


# def test_new_user_with_fixture(new_user):
#     """
#     GIVEN a User model
#     WHEN a new user is created
#     THEN check the email and password fields are defined correctly
#     """

#     assert new_user.first_name == 'camilo'
#     assert new_user.last_name == 'castrillon'
#     assert new_user.phone_number == '3107282539'
#     assert new_user.email == 'camiloc@gmail.com'
#     assert new_user.username == 'ccastrrri'
#     assert new_user.password != 'Holaporque1312'
#     assert new_user.neighborhood == 'olimpico'
#     assert new_user.department == 'valle'
#     assert new_user.city == 'cali'
#     assert new_user.img == 'a nice picture'
