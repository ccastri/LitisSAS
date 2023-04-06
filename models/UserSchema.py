from flask_marshmallow import Marshmallow, Schema
from marshmallow import fields, validate


class UserSchema(Schema):
    firstName = fields.Str(
        required=True, validate=validate.Length(min=2, max=20))
    lastName = fields.Str(required=True)
    phoneNumber = fields.Str(required=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    confirmPassword = fields.Str(required=True)
    city = fields.Str(required=True)
    department = fields.Str(required=True)
    neighborhood = fields.Str(required=True)
    # img = fields.Str(required=False)
    tos_is_clicked = fields.Bool(required=True, default=False)
    # created_at = fields.Str(required=False)
    # updated_at = fields.Str(required=False)

    class Meta:
        fields = ('firstName', 'lastName', 'phoneNumber', 'email', 'username',
                  'password', 'confirmPassword', 'neighborhood', 'city', 'department', 'tos_is_clicked',)


#! For one article
user_schema = UserSchema()
#! For a set of articles
users_schema = UserSchema(many=True)
