from flask import Flask, session, render_template, make_response

app = Flask(__name__)
app.secret_key = "abc"          # harusnya disimpan di server production


# ROUTING
@app.route('/')
def index():
    resp = make_response(render_template('protectedPage.html'))
    session['users']='users1'


    username = session['users']
    print(username)
    return resp, "Hello World"


if __name__== "__main__":
    app.run(port=5000, debug=True)