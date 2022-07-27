from flask import render_template
from flask_app import app

#Import All YOUR CONTROLLERS
from flask_app.controllers import users, recipes

## TODO: Create recipe class and controller with CRUD
## TODO: Validate all forms
##       Set get all links working

if __name__ == "__main__":
    app.run(debug=True)