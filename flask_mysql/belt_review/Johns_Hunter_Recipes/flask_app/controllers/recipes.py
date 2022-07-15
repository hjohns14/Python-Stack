from flask import render_template, request, redirect, session, flash, url_for
from flask_app import app
from flask_app.models import user, recipe

@app.route('/recipes/new')
def new_recipe():
    if not user.User.check_session(session):
        return redirect("/")
    return render_template("create_recipe.html")

@app.route('/recipes/<int:id>')
def view_recipe(id):
    if not user.User.check_session(session):
        return redirect("/")
    data = {
        'id': id
    }
    return render_template("view_recipe.html", recipe = recipe.Recipe.get_recipe_by_id(data))

@app.route('/recipes/<int:id>/edit')
def edit_recipe(id):
    if not user.User.check_session(session):
        return redirect("/")
    data = {
        'id': id
    }
    current_recipe = recipe.Recipe.get_recipe_by_id(data)
    return render_template("edit_recipe.html", recipe = current_recipe)

## Hidden Routes

@app.route('/recipes/new/create', methods=['POST'])
def create_recipe():
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_created': request.form['date_created'],
        'under_30': request.form['under_30'],
    }
    # Get user id and add to data
    print(session)
    data['user_id'] = session['user_id']

    if not recipe.Recipe.validate_recipe(data):
        return redirect("/recipes/new")

    print(data)

    recipe.Recipe.save(data)
    
    return redirect("/dashboard")

@app.route("/recipes/<int:id>/edit/process", methods=["POST"])
def edit_in_db(id):
    
    data = {
        'id': id,
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_created': request.form['date_created'],
        'under_30': request.form['under_30']
    }
    print(data)
    if not recipe.Recipe.validate_recipe(data):
        return redirect("/recipes/new")

    recipe.Recipe.update(data)
    return redirect("/dashboard")

@app.route('/recipes/<int:id>/delete')
def delete_recipe(id):
    data = {
        'id': id
    }
    recipe.Recipe.delete(data)

    return redirect("/dashboard")

