from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
import flask_app.models.dojo as dojo


class Ninja:
    db_name = "dojos_and_ninjas_schema"

    def __init__(self, data) -> None:
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.dojo_id = data["dojo_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create_ninja(cls, data):
        query = """INSERT INTO ninjas(first_name, last_name, age, dojo_id)
                VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"""

        for key, val in data.items():
            if val == "":
                return False

        result = connectToMySQL(cls.db_name).query_db(query, data)

        return result
