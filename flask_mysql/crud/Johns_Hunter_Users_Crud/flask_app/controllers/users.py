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

@app.route('/users/<int:id>/view')
def view_user(id):
    data = {
        "id": id
    }
    return render_template("view_user.html", user_info = user.User.get_one_user(data))

@app.route('/users/<int:id>/edit')
def edit_user(id):
    data = {
        "id": id
    }
    return render_template("edit_user.html", user_info = user.User.get_one_user(data))


#### Invisible Routes ###

@app.route('/users/add', methods=["POST"])
def add_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }
    user.User.create_user(data)

    return redirect("/users")

@app.route('/users/edit/process/<int:id>', methods=["POST"])
def process_edit(id):
    data = {
        "id": id,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }
    user.User.edit_user(data)
    return redirect("/users")

@app.route('/users/<int:id>/delete')
def delete_user(id):
    data = {
        "id": id
    }
    user.User.delete_user(data)
    
    return redirect("/users")
