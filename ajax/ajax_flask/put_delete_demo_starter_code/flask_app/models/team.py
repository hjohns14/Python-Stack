from flask_app.config.mysqlconnection import connectToMySQL

class Team:
    db_name = "teams_schema_july_2022"
    def __init__(self, data): # data is a dictionary - a row of data from your database
        self.id = data["id"]
        self.location = data["location"]
        self.name = data["name"]
        self.sport = data["sport"]
        self.description = data["description"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def add_team(cls, data):
        query = "INSERT INTO teams (name, location, sport, description) VALUES (%(name)s, %(location)s, %(sport)s, %(description)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all_teams(cls):
        query = "SELECT * FROM teams;"
        results = connectToMySQL(cls.db_name).query_db(query)
        print(results)
        if len(results) == 0: # No teams found
            return []
        else: # At least one team is found
            all_team_objects = []
            # Loop through the list of team dictionaries
            for this_team_dictionary in results:
                # Create the Team object
                new_team_object = cls(this_team_dictionary)
                # Add this Team to the list of all Teams
                all_team_objects.append(new_team_object)
            return all_team_objects

    @classmethod
    def get_one_team(cls, data):
        query = "SELECT * FROM teams WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        if len(results) == 0: # No teams found
            return None
        else: # At least one team is found
            # Create the Team object
            new_team_object = cls(results[0]) # Need 0 because we need a DICTIONARY!
            return new_team_object

    @classmethod
    def edit_team(cls, data):
        query = "UPDATE teams SET location = %(location)s, name = %(name)s, sport = %(sport)s, description = %(description)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete_team(cls, data):
        query = "DELETE FROM teams WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
