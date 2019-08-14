from flask import Flask, session, render_template, make_response, request

app = Flask(__name__)
app.secret_key = "abc"          # harusnya disimpan di server production


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
        session['users']=users

        username = session['users']
        print(username)
        return resp
    respwrong = make_response(render_template('loginPage.html'), 'Password is indcorrect')
    return  respwrong

@app.route('/auth/singout')
def logout():
    if (session['users'] != None):
        if (session['users']==True):
            print(username)
            if username:
                del session['users']
                return render_template('index.html')
        return " Your session is invalid <button><a style='text-decoration: none' href='/auth'>LOGIN</button></a>"
    return "You Session cannot delete"

@app.route('/protectedPage')
def protectedPage():
    username = session['users']
    print(username)
    if username:
        return (render_template('protectedPage.html'))
    return render_template('loginPage.html'), "You Must be Login First"

if __name__== "__main__":
    app.run(port=5000, debug=True)