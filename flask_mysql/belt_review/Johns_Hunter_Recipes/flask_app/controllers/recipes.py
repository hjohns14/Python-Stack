from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models import user, recipe

@app.route('/recipes/new')
def new_recipe():
    return render_template("create_recipe.html")

@app.route('/recipes/<int:id>')
def view_recipe(id):
    
    return render_template("view_recipe.html", recipe = recipe.Recipe.get_recipe_by_id(id))


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
    data['user_id'] = session['user_id']

    if not recipe.Recipe.validate_recipe(data):
        return redirect("/recipes/new")

    print(data)

    #recipe.Recipe.save(data)
    
    return redirect("/dashboard")
