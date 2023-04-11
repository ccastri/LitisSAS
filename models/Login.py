from wtforms import Form, StringField, PasswordField, BooleanField, validators
from wtforms.validators import DataRequired
# from flask_wtf import Form

PASSWORD_REGEX = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+~`\-={}[\]:;\'\"<>,.?\\/])(?=.*[^\da-zA-Z]).{8,16}$'


class LoginForm(Form):

    # username = StringField('Usuario', [
    #     validators.DataRequired(),
    #     validators.Length(min=8, max=16)
    # ])
    email = StringField('email', [
                        validators.Email(),
                        validators.Length(min=15, max=50)])
    password = PasswordField('contraseña', [
        validators.DataRequired(),
        validators.Length(min=8, max=16),
        validators.Regexp(
            PASSWORD_REGEX,
            message="La contraseña debe tener de 8 a 16 caracteres, al menos una letra mayúscula, una letra minúscula, un dígito, un carácter especial y ningún espacio en blanco."
        ),
    ])
