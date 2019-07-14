import sqlite3
from flask_restful import Resource, reqparse                                      #insert this when using sql lite in app5.py


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    # using this on app5.py

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query,(username,))  #this is will be execute username for the firs execute then query. "(username,)" using comma to define username is tupple
        row = result.fetchone()
        if row:
            # user = cls(row[0], row[1], row[2])        # We can change to /n
            user = cls(*row)                            #this will be show all index from row
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query,(_id,))  #this is will be execute username for the firs execute then query. "(username,)" using comma to define username is tupple
        row = result.fetchone()
        if row:
            # user = cls(row[0], row[1], row[2])        # We can change to /n
            user = cls(*row)                            #this will be show all index from row
        else:
            user = None

        connection.close()
        return user


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
        if User.find_by_username(data['username']):                 #this is the mean, if User.find_by_username(data['username']) note None
            return {"message" : "A user with that username already exists"}, 400

        connection = sqlite3.connect('data.db')             
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message" : "User created successfully."}, 201