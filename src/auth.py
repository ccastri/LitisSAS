from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
import validators
# from src.database import Users

from src.database import User, db
auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


@auth.post('/register')
def register():

    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    confirm_password = request.json['confirm_password']
    # confirm_password = request.json['confirm_password']
#! Validaciones:
    if len(password) < 6:
        return jsonify({
            'Password too short'
        })

    # if password is not confirm_password:
    #     return jsonify({
    #         "Passwords didnt match"
    #     })

    if len(username) < 3:
        return jsonify({
            "error": 'username is too short'
        })

    if not username.isalnum() or " " in username:
        return jsonify({
            "error": 'Nombre de usuario debe contener numeros y letras, sin espacios spaces'
        })
    if not validators.email(email):
        return jsonify({
            'error': "Email is not valid"
        })

    if User.query.filter_by(email=email).first() is not None:
        return jsonify({"error": "Email is taken already"})
    if User.query.filter_by(username=email).first() is not None:
        return jsonify({"error": "username is taken already"})

    pwd_hash = generate_password_hash(password)
    user = User(username=username, password=pwd_hash, email=email)
    db.session.add(user)
    db.session.commit()

    return jsonify({
        'message': "User created",
        'user': {
            'username': username,
            'email': email
        }
    })


@auth.get('/me')
def my_name():

    return jsonify({
        "error": 'Camilo Castrillon'
    })
