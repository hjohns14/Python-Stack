from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models import user, recipe
from datetime import date
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/')
def index():
    today = date.today().strftime("%Y-%m-%d")
    if user.User.check_session(session):
        return redirect("/dashboard")
    return render_template('index.html', today=today, session=session)

@app.route('/dashboard')
def dashboard():
    if not user.User.check_session(session):
        return redirect("/")
    all_recipes = recipe.Recipe.get_all_recipes_and_creator()
    return render_template("dashboard.html", session=session, all_recipes=all_recipes)


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
    session['user_id'] = user.User.save(user_data)
    return redirect("/dashboard")

@app.route('/login', methods=['POST'])
def login():
    data = {
        'email': request.form['email']
    }
    user_in_db = user.User.get_user_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password", "Login")
        session['email'] = data['email']
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password", "Login")
        session['email'] = data['email']
        return redirect("/")

    #Use session.pop if you need to hang on to any other data
    session.clear()

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

