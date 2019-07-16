# DIFFERENT WAY SIMPLE RESTFUL API WITH FLASK

from flask import Flask
from flask_restful import Api           
from flask_jwt import JWT


# import eksternal library
from security import authenticate, identity                    # import Class from file security.py
from resources.user import UserRegiser
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'    # tell to sqlachemy, where to find the data.db file. this is will be route to root folder, can using another sql
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///home/aandaldi/Documents/TrainInternal/Learn-Python-Flask/data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Aan'                                        # you must create this secret_key on flask
api = Api(app)

@app.before_first_request
def create_tables():
    print("create db")
    db.create_all()

jwt = JWT(app, authenticate, identity)                        # JWT create endpoint "/auth"

items = []

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')        # this is same like "@app3.route('/item/<string =:name>')"
api.add_resource(UserRegiser,'/register')
api.add_resource(ItemList, '/items/')
api.add_resource(StoreList, '/stores/')



if __name__=='__main__':
    from db import db
    print("nii")
    db.init_app(app)
    print("bisa")
    app.run(port=5000, debug=True)                     
