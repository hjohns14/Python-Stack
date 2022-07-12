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