from flask import Flask, render_template, Response, request, jsonify 
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    good_position = db.Column(db.Text, unique=True, nullable=False)
    bad_position = db.Column(db.Text, unique=True, nullable=False)


db.create_all()

@app.route('/get_all',  methods=['GET'])
def get_all():
    positions = Position.query.all()
    res = []
    for i in positions:
        res.append({
            "Bonne position" : i.good_position,
            "Mauvaise position" : i.bad_position
        })
    print(res)
    return {'status' : 'ok', 'data' : res}

@app.route('/',  methods=['GET', 'POST'])
def index():
    data = request.json
    print(data)
    print(data['value'])
    print(data['value'][0])


    position = Position(good_position=data['value'][0], bad_position=data['value'][1])
    db.session.add(position)
    db.session.commit()

    return {"status" : "ok"}





if __name__ == '__main__':
    # defining server ip address and port
    app.run(host='0.0.0.0',port='5000', debug=True)