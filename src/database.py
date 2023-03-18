from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_marshmallow import Marshmallow


# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/litis'
# app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy()
ma = Marshmallow()

# with app.app_context():
#     db.create_all()


class Plan(db.Model):

    __tablename__ = 'plans'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text(), nullable=False)
    price = db.Column(db.String(100), unique=True, nullable=False)
    img = db.Column(db.String(100), unique=True, nullable=False)
    #!Especifico la tabla usuarios y su columna ID para la foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, name: str, description: str, price: str, img: str, user_id: int):
        self.name = name
        self.description = description
        self.price = price
        self.img = img
        self.user_id = user_id

    def __repr__(self) -> str:
        return f'Plan>>> {self.name}'


class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.Text(), nullable=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    confirm_password = db.Column(db.String(50), nullable=True)
    neighborhood = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    department = db.Column(db.Text(), nullable=False)
    img = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)
    plan = db.relationship('Plan', backref="user")

    def __init__(self, id: int, first_name: str, last_name: str, phone_number: str, email: str, username: str, password: str, neighborhood: str, city: str, department: str, img: str):
        self.id = 1
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.username = username
        self.password = password
        self.neighborhood = neighborhood
        self.city = city
        self.department = department
        self.img = img

    def __repr__(self) -> str:
        return f'User>>> {self.username}'
