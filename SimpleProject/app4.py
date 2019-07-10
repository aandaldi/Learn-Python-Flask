# DIFFERENT WAY SIMPLE RESTFUL API WITH FLASK

from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

# import eksternal library
from security import authenticate, identity                    # import Class from file security.py


app3 = Flask(__name__)
app3.secret_key = 'Aan'                                        # you must create this secret_key on flask
api = Api(app3)

jwt = JWT(app3, authenticate, identity)                        # JWT create endpoint "/auth"

items = []


class Item(Resource):
    @jwt_required()                                           # this will be required token from jwt to access this function
    def get(self, name):
       item = next(filter(lambda x: x['name'] == name, items), None)
       return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message' : "An item with name '{}' already exist.".format(name)}, 404
        
        data = request.get_json()
        item = {'name': name, 'price': data['name']}
        items.append(item)
        return item, 201 


class ItemList(Resource):
    def get(self):
        return{'items': items}

api.add_resource(Item, '/item/<string:name>')        # this is same like "@app3.route('/item/<string =:name>')"
api.add_resource(ItemList, '/items/')


app3.run(port=5000, debug=True)                     # debug to give you error message