from wtforms import Form, StringField, PasswordField, BooleanField, validators
from wtforms.validators import DataRequired
# from flask_wtf import Form

PASSWORD_REGEX = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+~`\-={}[\]:;\'\"<>,.?\\/])(?=.*[^\da-zA-Z]).{8,16}$'


class RegisterForm(Form):
    firstName = StringField('Nombre', [
        validators.DataRequired(),
        validators.Length(min=2, max=20)])
    lastName = StringField('Apellido', [
        validators.DataRequired(),
        validators.Length(min=3, max=20)
    ])
    phoneNumber = StringField(
        'Numero telefonico', [
            validators.DataRequired(),
            validators.Length(min=10, max=10),
            validators.Regexp(
                '^[0-9]*$', message='Phone number must only contain digits')
        ])
    username = StringField('Usuario', [
        validators.DataRequired(),
        validators.Length(min=8, max=16)
    ])
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
        validators.EqualTo('confirmPassword',
                           message='Las contraseñas no coinciden')
    ])
    confirmPassword = PasswordField('confirmar contraseña', [
        validators.DataRequired(),
        validators.Length(min=8, max=50),
        validators.Regexp(
            PASSWORD_REGEX,
            message="La contraseña debe tener de 8 a 16 caracteres, al menos una letra mayúscula, una letra minúscula, un dígito, un carácter especial y ningún espacio en blanco."
        ), ])
    city = StringField('ciudad', [
        validators.DataRequired(),
        validators.Length(min=3, max=50)
    ])
    department = StringField('Departmento', [
        validators.Length(min=3, max=50)])
    neighborhood = StringField(
        'Barrio', [validators.Length(min=3, max=50)])
    tos_is_clicked = BooleanField(
        'Terminos y condiciones',)
