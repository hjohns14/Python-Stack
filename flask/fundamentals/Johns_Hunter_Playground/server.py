from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello (go to /play)"

@app.route("/play")
@app.route("/play/<int:x>")
@app.route("/play/<int:x>/<string:color>")
def play(x=3, color="lightblue"):
    return render_template("index.html", x=x, color=color)

if __name__ == "__main__":
    app.run(debug=True)