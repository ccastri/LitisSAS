from wtforms import Form, BooleanField, StringField, PasswordField, validators


class RegisterForm(Form):
    first_name = StringField('First Name', [
        validators.required(),
        validators.Length(min=2, max=25)])
    last_name = StringField('Last Name', [
        validators.required(),
        validators.Length(min=2, max=25)])
    phone_number = StringField(
        'Phone Number', [
            validators.required(),
            validators.Length(min=2, max=25)])
    username = StringField('Username', [
        validators.required(),
        validators.Length(min=2, max=25)])
    email = StringField('Email', [
        validators.required(),
        validators.Length(min=2, max=25)])
    password = PasswordField('Password', [
        validators.required(),
        validators.Length(min=2, max=25),
        validators.Equals('confirm_password',
                          message="Confirm Password didn't match")
    ])
    confirm_password = PasswordField('Confirm Password', [
        validators.required(),
        validators.Length(min=2, max=25)])
    neighborhood = StringField(
        'neighborhood', [
            validators.required(),
            validators.Length(min=2, max=25)])
    city = StringField('city', [
        validators.required(),
        validators.Length(min=2, max=25)])
    department = StringField('department', [
        validators.required(),
        validators.Length(min=2, max=25)])
    img = StringField('img', [
        validators.required(),
        validators.Length(min=2, max=25)])
