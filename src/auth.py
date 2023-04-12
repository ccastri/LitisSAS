from src import app
from flask_cors import cross_origin
from flask import Blueprint, request, jsonify, url_for, make_response
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity, decode_token
from flask_marshmallow import Marshmallow

from src.database import User, db
from models.User import RegisterForm
from models.UserSchema import user_schema
from models.LoginSchema import login_schema

auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")
ma = Marshmallow(app)


@auth.route('/register', methods=['POST'])
def register():
    #! Convertir el form del formato JSON de React
    #! A diccionario en Python para validarlo con Marshmallow
    new_user = request.form.to_dict()
    tos = request.form.get('tos_is_clicked')
    errors = user_schema.validate(new_user)
    #!catching user schema error here:
    if errors:
        return jsonify({"error": errors}), 400
    # Form data is valid, process it accordingly
    #! Los datos han sido deserializados
    #! WTForms validará los campos en el Backend
    form = RegisterForm(request.form)
    print(tos)
    if form.validate():
        #     #!Hasheo de la contraseña
        password_hash = generate_password_hash(
            new_user['password'], method='pbkdf2:sha1')
    #     #! Instancia de usuario usando el esquema de marshmallow
        user = User(first_name=new_user['firstName'],
                    last_name=new_user['lastName'],
                    phone_number=new_user['phoneNumber'],
                    email=new_user['email'],
                    username=new_user['username'],
                    password=password_hash,
                    confirm_password=new_user['confirmPassword'],
                    neighborhood=new_user['neighborhood'],
                    city=new_user['city'],
                    department=new_user['department'],
                    tos_is_clicked=form.tos_is_clicked.data)
    #     #! Añadir y guardar registro en la BB.DD. con SQLAlchemy
        db.session.add(user)
        db.session.commit()
    #     #!Generar token de acceso y refreshing
        refresh = create_refresh_token(identity=user.id)
        access = create_access_token(identity=user.id)

        response = make_response(jsonify(
            {
                "user": user.email,
                'access': access,
                "message": "Form data is valid"
            }))
        response.set_cookie('jwt_token', access, secure=True,
                            httponly=True, samesite='none')
        return response, 200
    else:
        # devolver errores de validación
        return jsonify({'errores': form.errors}), 400

# # !Email y usuario unicos en la BB.DD.:
# if User.query.filter_by(email=email).first() is not None:
#     return jsonify({"error": "Email is taken already"})
# if User.query.filter_by(username=email).first() is not None:
#     return jsonify({"error": "username is taken already"})


def get_jwt_token():
    # Obtén el token del encabezado de la solicitud
    token = request.headers.get('Authorization')
    # Pasa el token a Next.js en un encabezado personalizado
    response = app.make_response()
    response.headers['X-Access-Token'] = token
    return response


@auth.route('/login', methods=['POST'])
def login():
    #!Respuesta default
    response = make_response(jsonify({
        'message': 'credenciales inválidas'
    }), 401)
    new_user = request.json
    #!Seleccionar campos del login form y validar
    email = new_user['email']
    password = new_user['password']
    errors = login_schema.validate(new_user)
    if errors:
        return jsonify({"error": errors}), 400
    #!No tengo errores. Devuelvame el usuario que coincida con el email
    user = User.query.filter_by(email=email).first()
    if user:
        is_pass_correct = check_password_hash(user.password, password)
        if is_pass_correct:
            # def making_response(user):
            refresh = create_refresh_token(identity=user.id)
            access = create_access_token(identity=user.id)
            print(access)
            response = make_response(jsonify({
                'message': 'usuario autenticado'
            }), 200)
            response.set_cookie('jwt_token', access,)
            print(request.cookies.get('jwt_token'))
            return response

# response.set_cookie('jwt_token', value=refresh,
    # jsonify({'user': {
    #         'refresh': refresh,
    #         'access': access,
    #         'username': user.username,
    #         'email': email
    #         }})

    # except:

    return jsonify({'error': 'wrong credentials'})


@auth.route('/dashboard/profile/<int:id>', methods=['GET'])
@ jwt_required()
def profile(id):
    #! Para desplegar la informacion del perfil y completar con la seccion de docs
    #!Este metodo devuelve el id del usuario autenticado
    access = request.cookies.get('jwt_token')
    user_id = get_jwt_identity()
    print(access)

    if id == user_id:
        user = User.query.filter_by(id=user_id).first()
        response = make_response(jsonify({
            'message': 'usuario autenticado',
            'username': user.username,
            'email': user.email,
            # 'user.created_at': user.created_at
        }), 200)
        response.set_cookie('jwt_token', access, secure=False)
        print(request.cookies.get('jwt_token'))
    # response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response, 200
    else:
        print('this is the else right there')
    return
    return' no user found'
    # else:
    # user = User.query.filter_by(id=id).first()
    # decoded_token = decode_token(access)

    # url = url_for('profile', id=user_id)
    # access = create_access_token(identity=user.id)
    # id = User.query.get(id)
    # if id == user_id:
    # print(f'Hi! {user.username}')
    #! Confirmando que si está el token
    #! en las cookies de la respuesta a peticion
    # jwt_cached = request.cookies.get('jwt_token')
    # print(jwt_cached)
    # return response
    #     print('ask for permission dude')
    #     # return ""
    # return jsonify({'process': 'done'})
    # ! Podria pasar el user directamente para trabajar con todos los atributos

    # 'user_jwt_token': user_id

    # else:
    #     return jsonify({'message': 'something went wrong'})


@ auth.post('/token/refresh')
@ jwt_required(refresh=True)
def refresh_users_token():
    identity = get_jwt_identity()
    access = create_access_token(identity=identity)

    return jsonify({'access': access})

    #! Validaciones:

    # #! first_name:

    # #! Apellidos:

    # #! Numero de telefono:

    # if User.query.filter_by(phone_number=phone_number).first() is not None:
    #     return jsonify({"error": "Phone number is taken already"})
    # #! neighborhood:

    # #!Ciudad:

    # #! Departamento:

    # #!Password:

    # # TODO: REGEX para el password

    # #!Username:
