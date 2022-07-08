from flask_app.models import dojo, ninja
from flask_app import app
from flask import redirect, render_template, session, request

@app.route('/')
def main():
    return redirect("/dojos")

@app.route('/dojos')
def all_dojos():
    return render_template("main.html", dojos = dojo.Dojo.get_all_dojos())

@app.route('/dojos/<int:id>')
def show_dojo_with_ninjas(id):

    data = {
        "id": id
    }

    current_dojo = dojo.Dojo.show_ninjas_for_dojo(data)
    return render_template("show_ninjas.html", dojo=current_dojo)

## INVISIBLE ROUTES
@app.route('/dojos/add', methods=["POST"])
def add_dojo():
    data = {
        "name": request.form["name"]
    }


    result = dojo.Dojo.add_dojo(data)
    return redirect("/dojos")


