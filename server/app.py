#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    baked_breads = [food.to_dict() for food in BakedGood.query.all()]
    response = make_response(baked_breads,200)
    return response

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bread_by_id = BakedGood.query.filter(BakedGood.id == id).first()
    bread_to_dict = bread_by_id.to_dict()

    response = make_response(bread_to_dict, 200)
    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    bread_by_price = BakedGood.query.order_by(BakedGood.price.desc()).all()
    bread_to_dict = jsonify([bread.to_dict for bread in bread_by_price])
    response = make_response(bread_to_dict,200)
    return response

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    return ''

if __name__ == '__main__':
    app.run(port=5555, debug=True)
