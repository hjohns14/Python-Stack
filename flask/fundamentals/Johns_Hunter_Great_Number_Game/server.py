from flask import Flask, render_template, redirect, request_started, session, request
from random import randint

answer = randint(1, 100)


app = Flask(__name__)
app.secret_key = "42"  ## replace when using

@app.route('/')
def main():
    session['answer'] = randint(1, 100)
    session['count'] = 0

    print(session['answer'])
    return render_template("main.html")

@app.route('/guess', methods=["POST"])
def guess():
    session['guess'] = request.form['guess']
    return redirect("/display")

@app.route('/display')
def display():
    session['count'] += 1
    if session['count'] > 5:
        color = 'green'
        text= "You have run out of guesses"
    elif int(session['guess']) == int(session['answer']):
        color = 'green'
        text= f"Correct! It took you {session['count']} guesses."
    elif int(session['guess']) > int(session['answer']):
        color = 'red'
        text = "Too High! Guess again?"
    else:
        color = 'red'
        text = "Too Low! Guess again?" 
    return render_template("display.html", text=text, color=color)



if __name__ == "__main__":
    app.run(debug=True)