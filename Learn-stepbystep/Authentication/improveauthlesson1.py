from flask import Flask, request, render_template, make_response

app = Flask(__name__)


# ROUTING
@app.route('/')
def index():
    return render_template('index.html'), "Hello World",

@app.route('/auth')
def login():
    users = request.cookies.get('users')

    if users:
        return render_template('protectedPage.html')
    return render_template('loginPage.html')

@app.route('/auth/singin', methods=["GET", "POST"])
def signin():
    if request.method=='POST':
        users = request.form["username"]
        password = request.form['password']

    if password == 'test':
        resp = make_response(render_template('protectedPage.html'))
        resp.set_cookie('users', users)

        username = request.cookies.get('users')
        print(username)
        return resp
    respwrong = make_response(render_template('loginPage.html'), 'Password is indcorrect')
    return  respwrong

@app.route('/auth/singout')
def logout():
    username = request.cookies.get('users')
    print(username)
    if username:
        resp = make_response(render_template('index.html'))
        resp.set_cookie('users', expires=0)
        return resp
    return "You Session cannot delete"

@app.route('/protectedPage')
def protectedPage():
    username = request.cookies.get('users')
    print(username)
    if username:
        return (render_template('protectedPage.html'))
    return render_template('loginPage.html'), "You Must be Login First"

if __name__== "__main__":
    app.run(port=7000, debug=True)