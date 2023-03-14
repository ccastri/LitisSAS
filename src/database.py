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


class Plans(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text(), unique=True, nullable=False)
    price = db.Column(db.String(100), unique=True, nullable=False)
    img = db.Column(db.String(100), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime, default=datetime.datetime.now)


def __repr__(self) -> str:
    return 'Plan>>> {self.name}'


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.Text(), nullable=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    neighborhood = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    department = db.Column(db.String(30), nullable=False)
    img = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)
    plans = db.relationship('Plan', backref="user")

    def __repr__(self) -> str:
        return 'User>>> {self.phone_number}'
