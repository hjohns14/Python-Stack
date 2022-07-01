from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "42" ## replace when using

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/process', methods=["POST"])
def process():
    print(request.form)
    for key, val in request.form.items():
        session[key] = val.capitalize()
    return redirect("/result")

@app.route('/result')
def result():
    return render_template("result.html", session=session)

if __name__ == "__main__":
    app.run(debug=True)