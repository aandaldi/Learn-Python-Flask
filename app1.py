# This the Firs app using flask

from flask import Flask

app1 = Flask(__name__)

@app1.route('/')        #decorator to route the app
def home():
    string = 'Hello World, Welcome to my First app using Flask'
    print(string)
    return string

app1.run(port=5000)
