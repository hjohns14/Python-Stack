import bcrypt
from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models import user
from datetime import date
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/')
def index():
    today = date.today().strftime("%Y-%m-%d")
    if user.User.check_session(session):
        return redirect("/dashboard")
    return render_template('index.html', today=today)

@app.route('/dashboard')
def method_name():
    if user.User.check_session(session):
        return render_template("dashboard.html", session=session)

    else:
        return redirect("/")
### Hidden Routes


@app.route('/register', methods=['POST'])
def register():
    if not user.User.validate_registration(request.form):
        return redirect("/")

    hash_password = bcrypt.generate_password_hash(request.form['password'])

    user_data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': hash_password,
        'birthday': request.form['birthday']
    }

    for key, val in user_data.items():
        if key == 'password':
            continue
        session[key] =  val
    session['logged_in'] = True

    print(session)
    user.User.save(user_data)
    return redirect("/dashboard")

@app.route('/login', methods=['POST'])
def login():
    data = {
        'email': request.form['email']
    }
    user_in_db = user.User.get_user_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password", "Login")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password", "Login")
        return redirect("/")

    print("Success!")
    session['user_id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name
    session['last_name'] = user_in_db.last_name
    session['birthday'] = user_in_db.birthday
    session['logged_in'] = True
    
    return redirect("/dashboard")

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")

