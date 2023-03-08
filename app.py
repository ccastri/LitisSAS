from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime
# import init_app


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/litis'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text())
    date = db.Column(db.DateTime, default=datetime.datetime.now)


with app.app_context():
    db.create_all()

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/get', methods=['GET'])
def get_LitisPackages():
    return jsonify([{'litis': 'decolombia '}])


if __name__ == "__main__":
    app.run(debug=True)
