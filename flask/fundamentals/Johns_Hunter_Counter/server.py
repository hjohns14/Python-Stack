from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "big_ol_secret" #since not actually launching




if __name__ == "__main__":
    app.run(debug=True)
