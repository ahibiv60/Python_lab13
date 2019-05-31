from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
ma = Marshmallow(app)

class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.Integer)
    price = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    adress = db.Column(db.String(100), unique=True)
    number_of_rooms = db.Column(db.Integer)
    city = db.Column(db.String(100))

    def __init__(self, area, price, rating, adress, number_of_rooms, city):
        self.area = area
        self.price = price
        self.rating = rating
        self.adress = adress
        self.number_of_rooms = number_of_rooms
        self.city = city

# Product Schema
class HouseSchema(ma.Schema):
  class Meta:
    fields = ('id', 'area', 'price', 'rating', 'adress', 'number_of_rooms', 'city')
# Init schema
house_schema =  HouseSchema(strict=True)
houses_schema =  HouseSchema(many=True, strict=True)

# Create a Product
@app.route('/house', methods=['POST'])
def add_house():
  area = request.json['area']
  price = request.json['price']
  rating = request.json['rating']
  adress = request.json['adress']
  number_of_rooms = request.json['number_of_rooms']
  city = request.json['city']

  new_house = House(area, price, rating, adress, number_of_rooms, city)

  db.session.add(new_house)
  db.session.commit()

  return house_schema.jsonify(new_house)

# Get All Products
@app.route('/house', methods=['GET'])
def get_houses():
  all_houses = House.query.all()
  result = houses_schema.dump(all_houses)

  return jsonify(result.data)

# Get Single Products
@app.route('/house/<id>', methods=['GET'])
def get_house(id):
  house = House.query.get(id)

  return house_schema.jsonify(house)

# Update a Product
@app.route('/house/<id>', methods=['PUT'])
def update_house(id):
  house = House.query.get(id)

  area = request.json['area']
  price = request.json['price']
  rating = request.json['rating']
  adress = request.json['adress']
  number_of_rooms = request.json['number_of_rooms']
  city = request.json['city']

  house.area = area
  house.price = price
  house.rating = rating
  house.adress = adress
  house.number_of_rooms = number_of_rooms
  house.city = city

  db.session.commit()

  return house_schema.jsonify(house)

# Delete Product
@app.route('/house/<id>', methods=['DELETE'])
def delete_house(id):
  house = House.query.get(id)
  db.session.delete(house)
  db.session.commit()

  return house_schema.jsonify(house)

#db.create_all()

# Run Server
if __name__ == '__main__':
  app.run(debug=True, use_reloader=False)
