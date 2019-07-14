# DIFFERENT WAY SIMPLE RESTFUL API WITH FLASK

from flask import Flask, request
from flask_restful import Resource, Api, reqparse              #
from flask_jwt import JWT, jwt_required


# import eksternal library
from security5 import authenticate, identity                    # import Class from file security.py


app5 = Flask(__name__)
app5.secret_key = 'Aan'                                        # you must create this secret_key on flask
api = Api(app5)

jwt = JWT(app5, authenticate, identity)                        # JWT create endpoint "/auth"

items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type = float,
        required =True,                                 #should be price is mandatory
        help = "This field cannot be left blank!"
    )
    
    @jwt_required()                                           # this will be required token from jwt to access this function
    def get(self, name):
       item = next(filter(lambda x: x['name'] == name, items), None)
       return {'item': item}, 200 if item else 404

    # @jwt_required()                                           # this will be required token from jwt to access this function
    def post(self, name):
        

        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message' : "An item with name '{}' already exist.".format(name)}, 404
        
        # data = request.get_json()
        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201 
    
    def delete(self, name):
        global items
        items = list(filter(lambda x : x['name'] == name, items))
        return {"message" : "Item deleted"}

    def put(self, name):
       
        # data = request.get_json()
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name' : name   , 'price' : data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return{'items': items}

api.add_resource(Item, '/item/<string:name>')        # this is same like "@app3.route('/item/<string =:name>')"
api.add_resource(ItemList, '/items/')


app5.run(port=5000, debug=True)                     # debug to give you error message