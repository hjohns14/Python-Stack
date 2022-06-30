from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key("42") ## replace when using

@app.route('/')
def main():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(debug=True)