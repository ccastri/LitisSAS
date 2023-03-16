from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
import validators
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity
# from src.database import Users

from src.database import User, db
auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


@auth.post('/register')
def register():

    first_name = request.json['first_name']
    last_name = request.json['last_name']
    phone_number = request.json['phone_number']
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    # password2 = request.json['password2']
    confirm_password = request.json['password']
    neighborhood = request.json['neighborhood']
    city = request.json['city']
    department = request.json['department']
    img = request.json['img']
    plan_id = request.json['plan']
    created_at = request.json['created_at']


#! Validaciones:

    #! first_name:
    if " " in first_name:
        return jsonify({
            "error": "Por favor ingrese su nombre"
        })
    if len(last_name) < 2:
        return jsonify({
            "error": 'Nombre invalido'
        })
    #! Apellidos:
    if " " in last_name:
        return jsonify({
            "error": "Por favor ingrese su apellido"
        })
    if len(last_name) < 2:
        return jsonify({
            "error": 'Apellido invalido'
        })
    #! Numero de telefono:
    if " " in phone_number:
        return jsonify({
            "error": "Por favor ingrese un numero de telefono"
        })
    if len(phone_number) != 10:
        return jsonify({
            "error": "Por favor ingrese un numero de telefono valido"
        })
    if len(phone_number) != 10:
        return jsonify({
            "error": "Por favor ingrese un numero de telefono valido"
        })

    if User.query.filter_by(phone_number=phone_number).first() is not None:
        return jsonify({"error": "Phone number is taken already"})
    #! neighborhood:
    if " " in neighborhood:
        return jsonify({
            "error": "Por favor ingrese el barrio (sector) de residencia"
        })
    #!Ciudad:
    if " " in city:
        return jsonify({
            "error": "Por favor seleccione su departamento de residencia"
        })
    #! Departamento:
    if " " in department:
        return jsonify({
            "error": "Por favor seleccione su departamento de residencia"
        })
    #!Password:
    if len(password) < 6:
        return jsonify({
            'Password too short'
        })
    # TODO: REGEX para el password
    # if password != password2:
    # return "error 401  passwords dont match":
    # else
        # return confirm_password
    #     return jsonify({
    #         "Passwords dont match"
    #     })
    # if password != password2:
    #     return jsonify({
    #         "error": "passwords dont match"
    #     })
    #!Username:
    if len(username) < 3:
        return jsonify({
            "error": 'username is too short'
        })

    if not username.isalnum() or " " in username:
        return jsonify({
            "error": 'Nombre de usuario debe contener numeros y letras, sin espacios spaces'
        })
    #! Email:
    if not validators.email(email):
        return jsonify({
            'error': "Email is not valid"
        })
    #!Email y usuario unicos en la BB.DD.:
    if User.query.filter_by(email=email).first() is not None:
        return jsonify({"error": "Email is taken already"})
    if User.query.filter_by(username=email).first() is not None:
        return jsonify({"error": "username is taken already"})
    # First hast
        # hash_this = password

    password_hash = generate_password_hash(password)
    # user = User(username=username, password=pwd_hash, email=email)
    user = User(first_name=first_name, last_name=last_name, phone_number=phone_number, confirm_password=password_hash,
                username=username, password=password_hash, email=email, neighborhood=neighborhood, city=city, department=department, img=img, plan_id=plan_id, created_at=created_at)
    print(user.password)

    db.session.add(user)
    db.session.commit()

    return jsonify({
        'message': "User created. Status code: 200",
        'user': {
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': phone_number,
            'username': username,
            'email': email,
            'password': password_hash,
            'neighborhood': neighborhood,
            'city': city,
            'department': department
        }
    })


@auth.post('/login')
def login():
    email = request.json.get('email', '')
    password = request.json.get('password', '')

    # print(email, password)

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
    return jsonify({'error': 'wrong credentials'})


@auth.get('/me')
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
