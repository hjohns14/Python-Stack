from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class User:
    db_name = "books_schema"

    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.favorite_books = []
    
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users"

        results = connectToMySQL(cls.db_name).query_db(query)

        if len(results) == 0:
            return []
        else:
            output = [cls(user) for user in results]

        return output

    @classmethod
    def add_new_author(cls, data):
        query = """INSERT INTO users(first_name, last_name)
                VALUES(%(first_name)s, %(last_name)s)"""

        result = connectToMySQL(cls.db_name).query_db(query, data)

        return result

    @classmethod
    def get_one_author(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"

        result = connectToMySQL(cls.db_name).query_db(query, data)

        return cls(result[0])

    @classmethod
    def get_authors_favorites(cls, data):
        query = """select * from users
                left join favorites on favorites.user_id = users.id
                left join books on favorites.book_id = books.id
                where users.id = %(id)s;"""

        result = connectToMySQL(cls.db_name).query_db(query, data)

        author = cls(result[0])
        for row in result:
            book_data = {
                "id": row["books.id"],
                "title": row["title"],
                "num_of_pages": row["num_of_pages"],
                "created_at": row["books.created_at"],
                "updated_at": row["books.updated_at"],
            }
            author.favorite_books.append(book.Book(book_data))
        return author

    @classmethod
    def add_favorite_book(cls, data):
        query = "INSERT INTO favorites(user_id, book_id) VALUES(%(user_id)s, %(book_id)s)"

        result = connectToMySQL(cls.db_name).query_db(query, data)

        return result

    @classmethod
    def get_unfavorited_books(cls, data):
        query = """SELECT * FROM books WHERE books.id NOT IN
                (SELECT book_id from favorites where user_id=%(id)s)"""
        
        result = connectToMySQL(cls.db_name).query_db(query, data)

        unfav_books = [book.Book(row) for row in result]
        return unfav_books

