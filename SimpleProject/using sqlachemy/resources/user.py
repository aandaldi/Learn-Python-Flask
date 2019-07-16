import sqlite3
from flask_restful import Resource, reqparse   
from models.user import UserModel




class UserRegiser(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
         type=str,
         required=True,
         help="This field cannot be blank."
    )

    parser.add_argument(
        'password',
         type=str,
         required=True,
         help="This field cannot be blank."
    )

    def post(self):
        data = UserRegiser.parser.parse_args() 

        #check if the username already exists on database
        if UserModel.find_by_username(data['username']):                 #this is the mean, if User.find_by_username(data['username']) note None
            return {"message" : "A user with that username already exists"}, 400

        # user = UserModel(data['username'], data['password'])
        user = UserModel(**data)

        user.save_to_db()

        return {"message" : "User created successfully."}, 201