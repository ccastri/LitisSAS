# from src import app
# from flask_cors import cross_origin
# from flask import Blueprint, request, jsonify
# from werkzeug.security import check_password_hash, generate_password_hash
# from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity
# from flask_marshmallow import Marshmallow

# from src.database import User, db
# from models.User import RegisterForm
# from models.UserSchema import user_schema

# auth = Blueprint("dashboard", __name__, url_prefix="/api/v1/dashboard")
# ma = Marshmallow(app)


# @ auth.get('/dashborard/profile/id')
# @ jwt_required()
# def auth_route():
#     #! Para desplegar la informacion del perfil y completar con la seccion de docs
#     #!Este metodo devuelve el id del usuario autenticado

#     user_id = get_jwt_identity()

#     user = User.query.filter_by(id=user_id).first()
#     # ! Podria pasar el user directamente para trabajar con todos los atributos
#     return jsonify({'username': user.username,
#                     'email': user.email,
#                     'user_jwt_token': user_id})
