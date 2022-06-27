from tkinter import Y
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route("/<int:x>")
@app.route("/<int:x>/<int:y>")
@app.route("/<int:x>/<int:y>/<string:color1>")
@app.route("/<int:x>/<int:y>/<string:color1>/<string:color2>")
def build_board(x=8, y=8, color1='red', color2='black'):
    return render_template("index.html", x=x, y=y, color1=color1, color2=color2)

if __name__ == '__main__':
    app.run(debug=True)
