from flask import Blueprint, request, jsonify, render_template
from werkzeug.security import check_password_hash, generate_password_hash
from wtforms import Form, BooleanField, StringField, PasswordField, validators
# import validators
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity
from models.User import user_schema, users_schema
from src.database import User, db
# Serialization and data validation
from flask_marshmallow import Marshmallow
from src import app

auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")
ma = Marshmallow(app)


@auth.route('/register', methods=['POST'])
# @cross_origin()
def register():

    #! Acceso a las columnas de la BB.DD. en la tabla usuario

    # first_name = request.json['firstName']
    # last_name = request.json['lastName']
    # phone_number = request.json['phoneNumber']
    # username = request.json['username']
    # email = request.json['email']
    # password = request.json['password']
    # # password2 = request.get_json['password2']
    # confirm_password = request.json['confirmPassword']
    # neighborhood = request.json['neighborhood']
    # city = request.json['city']
    # department = request.json['department']
    # # img = request.json['img']
    # tos_is_clicked = request.json['tos_is_clicked']
    # # plan_id = request.json['plan']
    # created_at = request.json['created_at']
    # form_data = request.get_json()
    # errors = user_schema.validate(form_data)
    new_user = request.json
    print(new_user)
    errors = user_schema.validate(new_user)

    if errors:
        return jsonify({"error": errors}), 400
        # Form data is valid, process it accordingly
        # ...
        # #!Hasheo de la contraseña
    password_hash = generate_password_hash(
        new_user['password'], method='pbkdf2:sha1')
    # print(password)
    user = User(new_user['firsName'],
                new_user['lastName'],
                new_user['phoneNumber'],
                new_user['email'],
                new_user['username'],
                password_hash,
                new_user['confirmPassword'],
                new_user['neighborhood'],
                new_user['city'],
                new_user['department'],
                new_user['tos_is_clicked'], )
    #  tos_is_clicked
    print(user)
    db.session.add(user)
    db.session.commit()
    return jsonify(
        {
            "user": user,
            "message": "Form data is valid"
        }), 200

    # if not username.isalnum() or " " in username:
    #     return jsonify({
    #         "error": 'Nombre de usuario debe contener numeros y letras, sin espacios spaces'
    #     })
    # #! Email:
    # if not validators.email(email):
    #     return jsonify({
    #         'error': "Email is not valid"
    #     })
    # # !Email y usuario unicos en la BB.DD.:
    # if User.query.filter_by(email=email).first() is not None:
    #     return jsonify({"error": "Email is taken already"})
    # if User.query.filter_by(username=email).first() is not None:
    #     return jsonify({"error": "username is taken already"})


@auth.route('/login', methods={'GET': 'POST'})
def login():
    if request.method == 'GET':
        return 've el login ve'
    if request.method == 'POST':
        email = request.json.get('email', '')
        password = request.json.get('password', '')

        # print(email, password)
        # try:
        # if (email)
        user = User.query.filter_by(email=email).first()
        print(user.password)
        if user:
            is_pass_correct = check_password_hash(user.password, password)

            # print(is_pass_correct)
            if is_pass_correct:
                refresh = create_refresh_token(identity=user.id)
                access = create_access_token(identity=user.id)

                return jsonify({
                    'user': {
                        'refresh': refresh,
                        'access': access,
                        'username': user.username,
                        'email': email
                    }
                })
        # except:

        return jsonify({'error': 'wrong credentials'})


@auth.get('/dashborard/profile/id')
@jwt_required()
def auth_route():
    #! Para desplegar la informacion del perfil y completar con la seccion de docs
    #!Este metodo devuelve el id del usuario autenticado
    user_id = get_jwt_identity()

    user = User.query.filter_by(id=user_id).first()
    # ! Podria pasar el user directamente para trabajar con todos los atributos
    return jsonify({'username': user.username,
                    'email': user.email})


@auth.post('/token/refresh')
@jwt_required(refresh=True)
def refresh_users_token():
    identity = get_jwt_identity()
    access = create_access_token(identity=identity)

    return jsonify({'access': access})

    #! Validaciones:

    # #! first_name:
    # if " " in first_name:
    #     return jsonify({
    #         "error": "Por favor ingrese su nombre"
    #     })
    # if len(last_name) < 2:
    #     return jsonify({
    #         "error": 'Nombre invalido'
    #     })
    # #! Apellidos:
    # if " " in last_name:
    #     return jsonify({
    #         "error": "Por favor ingrese su apellido"
    #     })
    # if len(last_name) < 2:
    #     return jsonify({
    #         "error": 'Apellido invalido'
    #     })
    # #! Numero de telefono:
    # if " " in phone_number:
    #     return jsonify({
    #         "error": "Por favor ingrese un numero de telefono"
    #     })
    # if len(phone_number) != 10:
    #     return jsonify({
    #         "error": "Por favor ingrese un numero de telefono valido"
    #     })
    # if len(phone_number) != 10:
    #     return jsonify({
    #         "error": "Por favor ingrese un numero de telefono valido"
    #     })
    # if User.query.filter_by(phone_number=phone_number).first() is not None:
    #     return jsonify({"error": "Phone number is taken already"})
    # #! neighborhood:
    # if " " in neighborhood:
    #     return jsonify({
    #         "error": "Por favor ingrese el barrio (sector) de residencia"
    #     })
    # #!Ciudad:
    # if " " in city:
    #     return jsonify({
    #         "error": "Por favor seleccione su departamento de residencia"
    #     })
    # #! Departamento:
    # if " " in department:
    #     return jsonify({
    #         "error": "Por favor seleccione su departamento de residencia"
    #     })
    # #!Password:
    # if len(password) < 6:
    #     return jsonify({
    #         'Password too short'
    #     })
    # # TODO: REGEX para el password

    # #!Username:
    # if len(username) < 3:
    #     return jsonify({
    #         "error": 'username is too short'
    #     })
