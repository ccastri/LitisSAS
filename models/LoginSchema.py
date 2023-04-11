from flask_marshmallow import Marshmallow, Schema
from marshmallow import fields, validate

PASSWORD_REGEX = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+~`\-={}[\]:;\'\"<>,.?\\/])(?=.*[^\da-zA-Z]).{8,16}$'


class LoginSchema(Schema):

    # username = fields.Str(required=True)
    email = fields.Str(required=True, validate=validate.Length(min=2, max=50))
    password = fields.Str(
        required=True, validate=[
            validate.Length(min=8, max=16),
            validate.Regexp(
                regex=PASSWORD_REGEX,
                error='Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one number')
        ])

    class Meta:
        fields = ('email', 'password')


#! For one article
login_schema = LoginSchema()
#! For a set of articles
# users_schema = UserSchema(many=True)
