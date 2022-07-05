from flask_app import app
from flask_app.models import animal, zoo
from flask import render_template, redirect, session, request

#Visible Routes
@app.route('/')
def main():
    return redirect("/zoos")

@app.route('/zoos')
def method_name():
    return render_template("all_zoos.html", zoos = zoo.Zoo.get_all_zoos())

@app.route('/zoos/new')
def new_zoo_page():
    return render_template("add_zoo_page.html")

@app.route('/zoos/<int:id>/view')
def view_one_zoo(id):
    data = {
        "id": id
    }
    return render_template("view_one_zoo.html", zoo=zoo.Zoo.get_one_zoo(data))

@app.route('/zoos/<int:id>/edit')
def edit_one_zoo(id):
    data = {
        "id": id
    }
    return render_template("edit_zoo_page.html", zoo=zoo.Zoo.get_one_zoo(data))


####  Hidden routes ######

# Route to delete a zoo in db
@app.route('/zoos/<int:id>/delete')
def db_delete_zoo(id):
    data = {
        "id": id
    }
    zoo.Zoo.delete_zoo(data)
    return redirect("/zoos")

# Route to add a zoo to the db
@app.route('/zoos/add_to_db', methods=["POST"])
def db_add_one_zoo():
    #Remember to check if someone is logged in and check if the validations pass

    # Data dict for data from form
    data = {
        "name": request.form["name"],
        "city": request.form["city"],
        "size": request.form["size"],
        "visitor_capacity": request.form["visitor_capacity"],
        "opening_date": request.form["opening_date"]
    }

    #Use Class Method to query db
    zoo.Zoo.add_zoo(data)

    # Redirect to all Zoos
    return redirect("/zoos")

# Route to edit a zoo in the db
@app.route('/zoos/<int:id>/edit_zoo_in_db', methods=["POST"])
def db_edit_zoo(id):
    data = {
        "id": id,
        "name": request.form["name"],
        "city": request.form["city"],
        "size": request.form["size"],
        "visitor_capacity": request.form["visitor_capacity"],
        "opening_date": request.form["opening_date"],
    }
    zoo.Zoo.edit_zoo(data)
    return redirect(f"/zoos/{id}/view")