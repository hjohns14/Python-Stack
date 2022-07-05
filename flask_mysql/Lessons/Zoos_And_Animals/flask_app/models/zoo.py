from winreg import QueryInfoKey
from flask_app.config.mysqlconnection import connectToMySQL
# Might need to import the other model files
from flask_app.models import animal
# from flask_app import app # Might need to import the app in certain cases

class Zoo:
    # Use a class variable later on - it'd be nice to not have to change the schema name a million times (hint)
    db_name = "animals_zoos_schema"

    def __init__(self,data):
        self.id = data["id"]
        self.city = data["city"]
        self.name = data["name"]
        self.size = data["size"] # Acreage
        self.visitor_capacity = data["visitor_capacity"]
        self.opening_date = data["opening_date"] # When the zoo opened for the first time
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.animals = [] # NEW: Hold a list of Animals


    # We will write our queries here and talk to MySQL
    @classmethod
    def add_zoo(cls, data):
        query = """INSERT INTO zoos(city, name, size, visitor_capacity, opening_date) 
        VALUES( %(city)s, %(name)s, %(size)s, %(visitor_capacity)s, %(opening_date)s);"""

        connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all_zoos(cls):
        query = "SELECT * FROM zoos;"
        results = connectToMySQL(cls.db_name).query_db(query)

        #List will hold object form of zoos
        if len(results) == 0:
            return []
        else:
            zoo_objects = [cls(zoo_dict) for zoo_dict in results]

        return zoo_objects

    @classmethod
    def get_one_zoo(cls, data):
        query = "SELECT * FROM zoos WHERE id = %(id)s;"

        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) == 0:
            return None
        else:
            #Should only return one 
            zoo_objects = [cls(zoo_dict) for zoo_dict in results]

        return zoo_objects[0]
        
    @classmethod
    def edit_zoo(cls, data):
        query = """UPDATE zoos SET name= %(name)s, city= %(city)s,
                    size= %(size)s, visitor_capacity= %(visitor_capacity)s,
                    opening_date= %(opening_date)s
                    WHERE id = %(id)s;"""

        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete_zoo(cls, data):
        query = "DELETE FROM zoos WHERE id = %(id)s"
        return connectToMySQL(cls.db_name).query_db(query, data)



