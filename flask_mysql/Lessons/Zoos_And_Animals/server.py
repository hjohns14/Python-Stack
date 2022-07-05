from flask import render_template
from flask_app import app

#Import All YOUR CONTROLLERS
from flask_app.controllers import zoos, animals


if __name__ == "__main__":
    app.run(debug=True)