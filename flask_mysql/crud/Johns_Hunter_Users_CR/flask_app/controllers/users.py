from flask_app.models import user
from flask_app import app
from flask import redirect, render_template, session, request

@app.route('/')
def main():
    return redirect("/users")

@app.route('/users')
def show_all_users():
    return render_template("all_users.html", all_users = user.User.get_all_users())

@app.route('/users/new')
def create_new_user():
    return render_template("create_user.html")

#### Invisible Routes ###

@app.route('/users/add', methods=["POST"])
def method_name():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }
    user.User.create_user(data)


    return redirect("/users")

