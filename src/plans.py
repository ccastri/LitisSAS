from flask import Blueprint

plans = Blueprint("plans", __name__, url_prefix="/api/v1/plans")


@plans.post('/')
def register():
    return 'there are some plans'
