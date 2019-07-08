# SIMPLE RESTFUL API WITH FLASK

from flask import Flask, request
from flask_restful import Resource, Api


app3 = Flask(__name__)
api = Api(app3)

items = []


class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item' : None}, 404                 #to give status 404 Not Found

    def post(self, name):
        data = request.get_json()                   # you can add force=True to give header on respon api
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201                            # to give status 201 Created


class ItemList(Resource):
    def get(self):
        return{'items': items}

api.add_resource(Item, '/item/<string:name>')        # this is same like "@app3.route('/item/<string =:name>')"
api.add_resource(ItemList, '/items/')
app3.run(port=5000, debug=True)                     # debug to give you error message