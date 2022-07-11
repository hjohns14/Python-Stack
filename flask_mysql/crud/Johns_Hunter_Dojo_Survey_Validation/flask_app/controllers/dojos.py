from flask import render_template, redirect, session, request, url_for
from flask_app import app
from flask_app.models import dojo


@app.route('/')
def main():
    return render_template("main.html")

@app.route('/process', methods=["POST"])
def process():

    ## This works if everything is named properly in the html
    data = {}
    for key, val in request.form.items():
        data[key] = val

    if not dojo.Dojo.validate_input(request.form):
        return redirect("/")
    
    dojo_id = dojo.Dojo.save(data)

    id_data = {
        'id': dojo_id
    }

    db_dojo = dojo.Dojo.get_one_dojo(id_data)

    return redirect(url_for("result", id = dojo_id))

@app.route('/result/<int:id>')
def result(id):

    id_data = {
        'id': id
    }

    db_dojo = dojo.Dojo.get_one_dojo(id_data)

    return render_template("result.html", dojo = db_dojo)