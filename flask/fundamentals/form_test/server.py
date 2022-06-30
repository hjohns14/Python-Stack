from flask import Flask


from flask import Flask, render_template, redirect, request

app  = Flask(__name__)


@app.route('/')
def main():
    return render_template("main.html")

@app.route('/go', methods=["POST"])
def print_info():
    print(request.form["name"], request.form["email"], request.form["pet"], sep="\n")
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)