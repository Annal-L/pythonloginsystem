from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def new_user():
    return render_template("registration.html")

@app.route('/new')
def profile():
    return render_template("profile.html")

if __name__ == '__main__':
    app.run(debug=True)


