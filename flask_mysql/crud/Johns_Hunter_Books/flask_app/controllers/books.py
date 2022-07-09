import re
from flask import render_template, session, redirect, request, url_for
from flask_app import app
from flask_app.models  import user, book


@app.route('/books')
def all_books():

    all_books = book.Book.get_all_books()

    return render_template("all_books.html", books=all_books)

@app.route('/books/<int:id>')
def show_book_with_favorites(id):
    data ={
        "id": id
    }
    book_with_favs = book.Book.get_books_with_favorites(data)
    unfav_authors = book.Book.get_unfavorite_authors(data)

    return render_template("book_show.html", book = book_with_favs, unfav_authors=unfav_authors)



## Hidden Routes ##
@app.route('/books/add', methods=["POST"])
def add_new_book():
    data = {
        "title": request.form["title"],
        'num_of_pages': request.form["num_of_pages"]
    }
    book.Book.add_new_book(data)

    return redirect("/books")

@app.route('/books/<int:id>/add_favorite_author', methods=["POST"])
def add_author(id):
    data = {
        "user_id": request.form["user_id"],
        "book_id": id
    }

    user.User.add_favorite_book(data)
    return redirect(url_for("show_book_with_favorites", id=id))