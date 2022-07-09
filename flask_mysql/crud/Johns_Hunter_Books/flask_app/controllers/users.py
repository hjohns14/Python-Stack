from flask import render_template, session, redirect, request, url_for
from flask_app import app
from flask_app.controllers.books import all_books
from flask_app.models  import user, book

@app.route('/')
@app.route("/authors")
def all_authors():

    return render_template("main.html", authors=user.User.get_all_users())

@app.route('/authors/<int:id>')
def show_author(id):
    data = {
        "id": id
    }

    author_with_favorites = user.User.get_authors_favorites(data)
    unfavorited_books = user.User.get_unfavorited_books(data)
    


    return render_template("author_show.html", author=author_with_favorites, unfav_books=unfavorited_books)


## Hidden Routes ##

@app.route('/authors/add', methods=["POST"])
def add_new_author():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
    }
    result = user.User.add_new_author(data)
    return redirect("/authors")

@app.route('/authors/<int:id>/add_book', methods=["POST"])
def add_favorite(id):

    data = {
        "user_id": id,
        "book_id": request.form['book_id']
    }

    user.User.add_favorite_book(data)

    return redirect(url_for("show_author", id=id))