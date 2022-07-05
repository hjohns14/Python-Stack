from flask import render_template
from flask_app import app
from flask_app.models import users
#Import All YOUR CONTROLLERS

new_user = {
    'first_name': "'Hunter'",
    'last_name' : "'Johns'",
    'handle': "'huntala'",
    'birthday': "'1994-12-19'"
}
#Move routes to controllers files
@app.route('/')
def main():
    users_list = users.User.get_all()
    print(users_list)
    return render_template("index.html", all_users=users_list)


if __name__ == "__main__":
    app.run(debug=True)