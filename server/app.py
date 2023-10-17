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
    bakeries = Bakery.query.all()
    bakery = [bakery.to_dict() for bakery in bakeries]
    return make_response(jsonify(bakery), 200)

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery = Bakery.query.filter(Bakery.id == id).first()
    return make_response(jsonify(bakery.to_dict()), 200)

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    baked_goods_list = BakedGood.query.order_by(BakedGood.price.desc()).all()
    baked_goods = [baked_goods.to_dict() for baked_goods in baked_goods_list]
    return make_response(jsonify(baked_goods), 200)

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    baked_goods_list = BakedGood.query.order_by(BakedGood.price.desc()).limit(2)
    baked_goods = [baked_goods.to_dict() for baked_goods in baked_goods_list]
    return make_response(jsonify(baked_goods), 200)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
