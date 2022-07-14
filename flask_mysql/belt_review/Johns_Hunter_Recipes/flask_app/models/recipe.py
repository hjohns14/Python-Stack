from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Recipe:
    db_name = "recipe_schema"


    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.under_30 = data['under_30']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_created = data['date_created']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

        self.creator = None

    @classmethod 
    def save(cls, data):
        query = """INSERT INTO recipes(name, under_30, description, instructions, date_created, user_id)
                    VALUES(%(name)s, %(under_30)s, %(description)s, %(instructions)s, %(date_created)s, %(user_id)s)"""

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

        results = connectToMySQL(cls.db_name).query_db(query, data)

        print(results)
        if len(results) == 0:
            return []

        return cls(results[0])

    @classmethod
    def get_all_recipes_and_creator(cls):
        query = """SELECT *
                    FROM recipes
                    JOIN users ON recipes.user_id = users.id"""

        results = connectToMySQL(cls.db_name).query_db(query)

        all_recipes = []
        for row in results:
            recipe = cls(row)

            user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': '',
                'birthday': row['birthday'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at'],
            }
            recipe.creator = user.User(user_data)
            all_recipes.append(recipe)


        return all_recipes

    @classmethod
    def update(cls, data):
        query = """UPDATE recipes SET
                    name = %(name)s, under_30 = %(under_30)s,
                    description = %(description)s, instructions = %(instructions)s,
                    date_created = %(date_created)s
                    WHERE id = %(id)s"""

        result = connectToMySQL(cls.db_name).query_db(query, data)


    
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



