from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route("/say/<string:word>")
def say(word):
    return f'Hi {word.capitalize()}!'

@app.route("/repeat/<int:num>/<string:word>")
def repeat(num, word):
    return word * num

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)