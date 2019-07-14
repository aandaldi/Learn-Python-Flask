# DIFFERENT WAY SIMPLE RESTFUL API WITH FLASK

from flask import Flask
from flask_restful import Api           #
from flask_jwt import JWT

# import eksternal library
from security5 import authenticate, identity                    # import Class from file security.py
from user5 import UserRegiser
from item import Item, ItemList

app5 = Flask(__name__)
app5.secret_key = 'Aan'                                        # you must create this secret_key on flask
api = Api(app5)

jwt = JWT(app5, authenticate, identity)                        # JWT create endpoint "/auth"

items = []

api.add_resource(Item, '/item/<string:name>')        # this is same like "@app3.route('/item/<string =:name>')"
api.add_resource(ItemList, '/items/')
api.add_resource(UserRegiser,'/register')

app5.run(port=5000, debug=True)                     # debug to give you error message