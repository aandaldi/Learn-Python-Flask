from flask import Flask, request, render_template, make_response

app = Flask(__name__)


# ROUTING
@app.route('/')
def index():
    resp = make_response(render_template('protectedPage.html'))
    resp.set_cookie('username', 'ini cookienya yah')

    username = request.cookies.get('username')
    print(username)
    return resp, "Hello World"


if __name__== "__main__":
    app.run(port=7000, debug=True)