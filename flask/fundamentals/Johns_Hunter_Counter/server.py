from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "big_ol_secret" #since not actually launching on anything


@app.route('/')
def main():
    if 'visits' not in session and 'counter' not in session:
        session['visits'] = 0
        session['counter'] = 0
    session['visits'] += 1
    return render_template("main.html")


@app.route('/count_2')
def count2():
    session['counter'] += 2
    return redirect("/")

@app.route('/count_num', methods=["POST"])
def count_num():
    session['counter'] += int(request.form['num'])
    return redirect("/")

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect("/")




if __name__ == "__main__":
    app.run(debug=True)
