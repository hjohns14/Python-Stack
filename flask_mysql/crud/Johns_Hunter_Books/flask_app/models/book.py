from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Book:
    db_name = "books_schema"

    def __init__(self, data) -> None:
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.favorited_by = []

    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books"

        results = connectToMySQL(cls.db_name).query_db(query)

        output = [cls(book) for book in results]

        return output

    @classmethod
    def add_new_book(cls, data):
        query = """INSERT INTO books(title, num_of_pages)
                VALUES(%(title)s, %(num_of_pages)s)"""

        result = connectToMySQL(cls.db_name).query_db(query, data)

        return result

    @classmethod
    def get_books_with_favorites(cls, data):
        query = """select * from books
        left join favorites on favorites.book_id = books.id
        left join users on favorites.user_id = users.id
        where books.id = %(id)s;"""

        result = connectToMySQL(cls.db_name).query_db(query, data)

        book_result = cls(result[0])
        for row in result:
            user_data = {
                "id": row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"],
            }
            book_result.favorited_by.append(user.User(user_data))
        return book_result

    @classmethod
    def get_unfavorite_authors(cls, data):
        query = """SELECT * FROM users WHERE users.id NOT IN
                (SELECT user_id from favorites where book_id=%(id)s)"""
        
        result = connectToMySQL(cls.db_name).query_db(query, data)

        unfav_authors = [user.User(row) for row in result]
        return unfav_authors

    @classmethod
    def add_author_to_favorites(cls, data):
        query = "INSERT INTO favorites(user_id, book_id)"
