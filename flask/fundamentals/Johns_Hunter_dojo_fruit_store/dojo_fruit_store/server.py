import re
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "super_secret_key" 

@app.route('/')         
def index():
    session.clear()
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    for key, val in request.form.items():
        session[key] = val
    print(session)
    total_order = int(request.form['strawberry']) + int(request.form['raspberry']) +int(request.form['apple'])
    session['total_order'] = total_order
    print(f"Charging {request.form['first_name']} {request.form['last_name']} for {total_order} fruits")
    return redirect("/success")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

@app.route('/success')
def success():
    return render_template("checkout.html", total_order=session['total_order'], request_form=session) 

if __name__=="__main__":   
    app.run(debug=True)    