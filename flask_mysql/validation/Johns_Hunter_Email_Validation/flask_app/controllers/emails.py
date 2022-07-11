from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import email

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/success')
def success():
    all_emails = email.Email.get_all_emails()
    return render_template("show_emails.html", all_emails=all_emails)

### Hidden Routes

@app.route('/process', methods=["POST"])
def process():

    if not email.Email.validate_email(request.form):
        return redirect("/")
    data = {}
    for key, val in request.form.items():
        data[key] = val

    email.Email.save_to_db(data)

    return redirect("/success")

@app.route('/delete/<int:id>')
def delete_from_db(id):
    data = {
        'id': id
    }

    email.Email.delete_from_db(data)

    return redirect("/success")