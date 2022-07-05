# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    def __init__(self, data) -> None:
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.handle = data["handle"]
        self.birthday = data["birthday"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"

        results = connectToMySQL("twitter").query_db(query)

        users = []

        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def new_user(cls, user_data):
        query = "INSERT INTO users(first_name, last_name, handle, birthday) VALUES( %(first_name)s, %(last_name)s, %(handle)s, %(birthday)s );"
        results = connectToMySQL("twitter").query_db(query, user_data)



    