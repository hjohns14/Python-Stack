from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Recipe:
    db_name = "recipe_schema"


    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.under_30 = data['under_30'].lower() == "yes"
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_created = data['date_created']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

        self.creator = None

    @classmethod 
    def save(cls, data):
        query = """INSERT INTO recipes(name, description, instructions, date_created, user_id)
                    VALUES(%(name)s, %(description)s, %(instructions)s, %(date_created)s, %(user_id)s)"""

        result = connectToMySQL(cls.db_name).query_db(query, data)

        return result

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes"

        results = connectToMySQL(cls.db_name).query_db(query)

        if len(results) == 0:
            return []
        
        return [cls(recipe_data) for recipe_data in results]
    
    @classmethod
    def get_recipe_by_id(cls, data):
        query = "SELECT * FROM recipes WHERE id=%(id)s"

        results = connectToMySQL(cls.db_name).query_db(query)

        if len(results) == 0:
            return []

        return cls(results[0])

    
    @staticmethod
    def validate_recipe(data):
        is_valid = True

        if len(data['name']) < 2:
            flash("Name must be more than one letter", "Recipe")
            is_valid = False
        if len(data['description']) < 5:
            flash("Description must be at least 5 characters", "Recipe")
            is_valid = False
        if len(data['instructions']) < 10:
            flash("Please enter throrough instructions. (More than 10 letters)", "Recipe")
            is_valid = False
        if len(data['date_created']) < 8:
            flash("Invalid date", "Recipe")
            is_valid = False
        
        return is_valid



