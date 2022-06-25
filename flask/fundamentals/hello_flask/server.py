from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/users/<name>/<int:user_id>')
def show_user(name, user_id):
    return "name: " + name + " user id: " + user_id 

if __name__ == "__main__":
    app.run(debug=True)