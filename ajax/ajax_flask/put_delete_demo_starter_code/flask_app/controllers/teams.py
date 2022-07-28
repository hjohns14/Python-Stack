# Where we define our routes!
from flask_app import app # Needed for @app.route() among other things
from flask_app.models import team # Import models
from flask import render_template, redirect, request, session # Import methods from Flask

# VISIBLE routes
@app.route("/") # Route shows ALL the teams from our database in a page
def all_teams_page(): 
    return render_template("all_teams.html", all_teams = team.Team.get_all_teams())

@app.route("/teams/new") # Shows the form where one can add a team
def new_team_page():
    return render_template("add_team_page.html")

@app.route("/teams/<int:id>/view") # Shows the page where we can examine a specific team
def view_one_team_page(id):
    data = {
        "id": id
    }
    return render_template("view_one_team.html", this_team = team.Team.get_one_team(data))

@app.route("/teams/<int:id>/edit") # Shows the form where a specific team can be edited
def edit_one_team_page(id):
    data = {
        "id": id
    }
    return render_template("edit_team_page.html", this_team = team.Team.get_one_team(data))

# INVISIBLE or HIDDEN routes
@app.route("/teams/<int:id>/delete") # Route that will delete team from the database
def delete_team(id):
    data = {
        "id": id
    }
    team.Team.delete_team(data)
    return redirect("/")

@app.route("/teams/add_team_to_db", methods=["POST"]) # POST route that will add a team to the database
def add_team_to_db():
    # Data from the form
    data = {
        "name": request.form["name"],
        "location": request.form["location"],
        "sport": request.form["sport"],
        "description": request.form["description"],
    }
    team.Team.add_team(data) # Call on model to add this team to DB
    return redirect("/") # Go to all teams page

@app.route("/teams/<int:id>/edit_team_in_db", methods=["POST"]) # POST route where a team will be edited in the database
def update_team_in_db(id):
    data = {
        "name": request.form["name"],
        "location": request.form["location"],
        "sport": request.form["sport"],
        "description": request.form["description"],
        "id": id,
    }
    team.Team.edit_team(data) # Edit team in DB
    return redirect(f"/teams/{id}/view")