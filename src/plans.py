from flask import Blueprint, request, jsonify
from src.database import Plan, db
plans = Blueprint("plans", __name__, url_prefix="/api/v1/plans")


@plans.post('/')
def add_plans():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    img = request.json['img']
    user_id = request.json['user_id']
    # created_at = request.json['created_at']

    plans = Plan(name=name, description=description,
                 price=price, img=img, user_id=user_id,)

    db.session.add(plans)
    db.session.commit()

    return jsonify({'Message': 'Status code 200',
                    'plans': {
                        'name': name,
                        'Description': description,
                        'Price': price,
                        'img': img,
                        'user_id': user_id,
                    }
                    })
