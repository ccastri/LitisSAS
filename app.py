from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/litis'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

with app.app_context():
    db.create_all()

#! MODELOS:


class Plans(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text())
    price = db.Column(db.String(100))
    img = db.Column(db.String(100))
    date = db.Column(db.DateTime, default=datetime.datetime.now)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.Text())
    phone_number = db.Column(db.String(20))
    email = db.Column(db.String(20))
    neighborhood = db.Column(db.String(20))
    city = db.Column(db.String(30))
    department = db.Column(db.String(30))
    img = db.Column(db.String(50))
    date = db.Column(db.DateTime, default=datetime.datetime.now)

    #!INICIALIZAR MODELO PLANES:
    def __init__(self, name, description, price, img):
        self.name = name
        self.description = description
        self.price = price
        self.img = img

    #!INICIALIZAR MODELO USUARIOS:
    def __init__(self, first_name, last_name, phone_number, email, neighborhood, city, department, img):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.neighborhood = neighborhood
        self.city = city
        self.department = department
        self.img = img

 # self.price = price
 # self.isSelected = isSelected


#! Serializing data to submit it to the frontend
class PlanSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'img', 'date')


#! For one article
plan_schema = PlanSchema()
#! For a set of articles
plans_schema = PlanSchema(many=True)

#! Serializing data to submit it to the frontend


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'phone_number',
                  'email', 'neighborhood', 'city', 'department', 'img', 'date')


#! For one article
user_schema = UserSchema()
#! For a set of articles
users_schema = UserSchema(many=True)

# TODO: ORGANIZAR LOS MODELOS Y ESQUEMAS DE MARSHMELLOW (PLANS, USERS, //PlanSchema, UserSchema ) EN OTRO SCRIPT
# TODO: MONTAR CRUD DE USUARIOS


# !!!!!!!!!!!!RUTES!!!!!!!!!!!!!#


@app.route('/get', methods=['GET'])
def get_allLitisPackages():
    all_articles = Plans.query.all()
    results = plan_schema.dump(all_articles)
    return jsonify(results)


# @app.route('/get/<id>/', methods=['GET'])
# def get_LitisPackagesById(id):
#     article = Articles.query.get(id)
#     return article_schema.jsonify(article)


@app.route('/update/<id>/', methods=['PUT'])
def update_LitisPackagesById(id):
    _plan = Plans.query.get(id)

    name = request.json['name']
    description = request.json['description']
    img = request.json['img']
    price = request.json['price']

    _plan.name = name
    _plan.description = description
    _plan.price = price
    _plan.img = img

    db.session.commit()
    return plan_schema.jsonify(_plan)


@app.route('/planss', methods=['POST'])
def add_article():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    img = request.json['img']
    plans = Plans(name, description, price, img)
    db.session.add(plans)
    db.session.commit()
    return plan_schema.jsonify(plans)

    # price = request.json['price']


@app.route('/delete/<id>/', methods=['DELETE'])
def delete_LitisPackagesById(id):
    plan = Plans.query.get(id)
    db.session.delete(plan)
    db.session.commit()

    return plan_schema.jsonify(plan)


if __name__ == "__main__":
    app.run(debug=True,  port=3000, host='192.168.1.4')
