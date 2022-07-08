from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    db_name = "dojos_and_ninjas_schema"

    def __init__(self, data) -> None:
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.ninjas = []


    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        result = connectToMySQL(cls.db_name).query_db(query)

        if len(result) == 0:
            return []
        else:
            return [cls(dojo) for dojo in result]

    @classmethod
    def add_dojo(cls, data):
        query = "INSERT INTO dojos(name) VALUES(%(name)s)"
        if data["name"] == "":
            return False

        result = connectToMySQL(cls.db_name).query_db(query, data)
        

        return result
    
    @classmethod
    def show_ninjas_for_dojo(cls, data):
        query = """Select * from dojos
                left join ninjas on ninjas.dojo_id = dojos.id
                where dojos.id = %(id)s;"""

        results = connectToMySQL(cls.db_name).query_db(query, data)
        dojo = cls(results[0])
        for row in results:

            ninja_data = {
                "id": row["ninjas.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "age": row["age"],
                "created_at": row["ninjas.created_at"],
                "updated_at": row["ninjas.updated_at"],
                "dojo_id": row["dojo_id"],
            }

            dojo.ninjas.append(ninja.Ninja(ninja_data))

        return dojo


