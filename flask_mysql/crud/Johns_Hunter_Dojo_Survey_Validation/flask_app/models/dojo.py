from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    db_name = "dojo_survey_schema"

    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = """INSERT INTO dojos(name, location, language, comment)
                    VALUES(%(name)s, %(location)s, %(language)s, %(comment)s)"""

        results = connectToMySQL(cls.db_name).query_db(query, data)

        return results

    @classmethod
    def get_one_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"

        results = connectToMySQL(cls.db_name).query_db(query, data)

        print(results)
        return cls(results[0])

    @staticmethod
    def validate_input(dojo):
        is_valid = True
        if len(dojo['name']) < 2:
            flash("Name must be at least 2 Characters!")
            is_valid = False

        if len(dojo['comment']) < 1 or dojo['comment'].isspace():
            flash("You Must enter a comment!")
            is_valid = False
        
        if len(dojo['comment']) > 254:
            flash("Comment Length is 255 characters")
            is_valid = False

        return is_valid