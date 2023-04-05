from flask_marshmallow import Marshmallow, Schema
from marshmallow import fields, validate


class UserSchema(Schema):
    firstName = fields.Str(
        required=True, validate=validate.Length(min=2, max=20))
    lastName = fields.Str(required=True)
    phoneNumber = fields.Str(required=True)
    email = fields.Str(required=True)
    # username = fields.List(fields.Int(), required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    confirmPassword = fields.Str(required=True)
    city = fields.Str(required=True)
    department = fields.Str(required=True)
    neighborhood = fields.Str(required=True)
    # img = fields.Str(required=False)
    tos_is_clicked = fields.Bool(required=True)
    # created_at = fields.Str(required=False)

    class Meta:
        fields = ('firstName', 'lastName', 'phoneNumber', 'email', 'username',
                  'password', 'confirmPassword', 'neighborhood', 'city', 'department', 'tos_is_clicked',)


#! For one article
user_schema = UserSchema()
#! For a set of articles
users_schema = UserSchema(many=True)

# def __init__(self, first_name: str, last_name: str, phone_number: str, email: str, username: str, password: str, confirm_password: str, neighborhood: str, city: str, department: str, tos_is_clicked: bool, ):
#     # img: str,
#     # tos_is_clicked: bool,
#     # self.id = id
#     self.first_name = first_name
#     self.last_name = last_name
#     self.phone_number = phone_number
#     self.email = email
#     self.username = username
#     self.password = password
#     self.confirm_password = confirm_password
#     self.neighborhood = neighborhood
#     self.city = city
#     self.department = department
#     # self.img = img
#     self.tos_is_clicked = tos_is_clicked
#     # self.created_at = created_at

# def __repr__(self) -> str:
#     return f'User>>> {self.username}'

#! Pending for testing


# class UserSchema(Schema):
#     first_name = fields.Str(
#         required=True, validate=validate.Length(min=2, max=20))
#     last_name = fields.Str(required=True)
#     phone_number = fields.Str(required=True)
#     email = fields.Str(required=True)
#     # username = fields.List(fields.Int(), required=True)
#     username = fields.Str(required=True)
#     password = fields.Str(required=True)
#     confirm_password = fields.Str(required=True)
#     city = fields.Str(required=True)
#     department = fields.Str(required=True)
#     neighborhood = fields.Str(required=True)
#     # img = fields.Str(required=False)
#     tos_is_clicked = fields.Str(required=True)
#     # created_at = fields.Str(required=False)

#     class Meta:
#         fields = ('first_name', 'last_name', 'phone_number', 'email', 'username',
#                   'password', 'confirm_password', 'neighborhood', 'city', 'department', 'tos_clicked',)
# 'tos_is_clicked'
#  'img',


# #! For one article
# user_schema = UserSchema()
# #! For a set of articles
# users_schema = UserSchema(many=True)
