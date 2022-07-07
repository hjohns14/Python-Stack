from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db_name = "users_schema"

    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db_name).query_db(query)

        if len(results) == 0:
            return []

        else:
            users = [cls(user_dict) for user_dict in results]

        return users

    @classmethod
    def get_one_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(cls.db_name).query_db(query, data)

        if len(result) == 0:
            return 0
        else:
            return cls(result[0])

    @classmethod
    def create_user(cls, data):
        query = """INSERT INTO users(first_name, last_name, email)
                    VALUES(%(first_name)s, %(last_name)s, %(email)s);"""
        result = connectToMySQL(cls.db_name).query_db(query, data)

        return result

    @classmethod
    def edit_user(cls, data):
        query = """UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s
                    WHERE id = %(id)s"""

        result = connectToMySQL(cls.db_name).query_db(query, data)

        return result

    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM users WHERE id=%(id)s"

        result = connectToMySQL(cls.db_name).query_db(query, data)

        return result
