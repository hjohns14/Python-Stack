from flask_app.models import dojo, ninja
from flask_app import app
from flask import redirect, render_template, session, request, url_for


@app.route('/ninjas')
def add_ninja_page():
    dojos = dojo.Dojo.get_all_dojos()

    return render_template("add_ninja.html", dojos=dojos)


## Hidden routes

@app.route('/ninjas/add', methods=["POST"])
def db_add_ninja():
    
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"],
    }
    dojo_id = data['dojo_id']
    result = ninja.Ninja.create_ninja(data)
    if result == False:
        return redirect("/ninjas")

    return redirect(url_for("show_dojo_with_ninjas", id=dojo_id))