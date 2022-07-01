from flask import Flask, render_template, redirect, session, request
from random import randint

app = Flask(__name__)
app.secret_key = "42" ## replace when using

@app.route('/')
def main():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    
    return render_template("main.html", session=session)

@app.route('/process_gold', methods=["POST"])
def process_gold():
    if request.form['building'] == 'farm':
        gold = randint(10,20)
        session['gold'] += gold
        session['activities'].append(gold)
    elif request.form['building'] == 'cave':
        gold = randint(5,10)
        session['gold'] += gold
        session['activities'].append(gold)
    elif request.form['building'] == 'house':
        gold = randint(2,5)
        session['gold'] += gold
        session['activities'].append(gold)
    if request.form['building'] == 'casino':
        gold = randint(-50,50)
        session['gold'] += gold
        if gold <= 0:
            session['activities'].append(gold)
        else:
            session['activities'].append(gold)
    print(gold)
    return redirect("/")

@app.route('/reset')
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)