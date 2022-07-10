from flask_app import app
from flask_app.models.user import User
from flask import redirect, render_template, session, request, url_for

@app.route('/')
def main():
    return redirect("/friendships")


@app.route('/friendships')
def show_friendships():
    result = User.get_users_and_friends()
    all_users = User.get_all_users()

    return render_template("index.html", users = result, all_users = all_users)



@app.route('/friendships/add_user', methods=['POST'])
def db_add_user():
    user_data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
    }
    User.add_user(user_data)
    return redirect(url_for("show_friendships"))

@app.route('/friendships/make_friend', methods=['POST'])
def db_make_friend():
    data = {
        'user_id': request.form["user_id"],
        'friend_id': request.form['friend_id']
    }
    User.make_friends(data)
    return redirect(url_for("show_friendships"))