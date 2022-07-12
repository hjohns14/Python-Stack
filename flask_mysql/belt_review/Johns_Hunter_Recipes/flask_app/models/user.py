
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

class User:
    db_name = 'recipe_schema'

    def __init__(self, data) -> None:
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.birthday = data["birthday"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls, data):
        query = """INSERT INTO users(first_name, last_name, email, password, birthday)
                    VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s, %(birthday)s)"""

        result = connectToMySQL(cls.db_name).query_db(query, data)

        return result

    @classmethod
    def get_user_by_email(cls, data):
        query = """SELECT * FROM users WHERE email=%(email)s;"""

        results = connectToMySQL(cls.db_name).query_db(query, data)

        if len(results) == 0:
            return False

        return cls(results[0])


    @classmethod
    def get_all_users_safe(cls):
        query = """SELECT id, first_name, last_name, email, birthday, created_at, updated_at FROM users;"""

        results = connectToMySQL(cls.db_name).query_db(query)

        if len(results) == 0:
            return False
        all_users = []
        for row in results:
            user_data = {
                'id': row['id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': '',
                'birthday': row['birthday'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at'],
            }
            all_users.append(cls(user_data))
        
        return all_users

    @staticmethod
    def validate_registration(user):
        is_valid = True
        pw_invalid = False
        if len(user['first_name']) < 1 or len(user['last_name']) < 1:
            flash("* Field Required: Name", 'Register')
            is_valid = False
        if len(user['email']) < 1:
            flash("* Field Required: Email", 'Register')
            is_valid = False
        if not user['password']:
            flash("* Field Required: Password", 'Register')
        if user['password'] != user['confirm_password']:
            flash("* Passwords do not match!", "Register")
            is_valid = False
        if not user['birthday']:
            flash("* Field Required: Birthday", "Register")
            is_valid = False

        all_users = User.get_all_users_safe()
        for db_user in all_users:
            if user['email'] == db_user.email:
                flash("* Email has been taken", "Register")
                is_valid = False
        
        # creates a list of each character in the password like ['a', 'b', 'c']
        pw = [letter for letter in user['password']]
        

        ## If any of these statement return false -> set password invalid true

        # any() checks for any True --- ### --- any([False, False, True, False]) -> True
        # checks if any character in the pw is a digit -> if so return True and move on
        if not any(char.isdigit() for char in pw):
            pw_invalid = True
        # same but for upper case -> if no char is lower return false and pw_invalid = True
        if not any(char.isupper() for char in pw):
            pw_invalid = True
        # same but for lower case
        if not any(char.islower() for char in pw):
            pw_invalid = True
        # finally check length
        if len(user['password']) < 6:
            pw_invalid = True

        ## If the password is invalid, the 
        if pw_invalid:
            flash("""* Password must contain one of each of the following
                    \n- An uppercase letter
                    \n- A lowercase letter
                    \n- A number
                    \n- Must be longer than 6 characters""", "Register")
            is_valid = False


        return is_valid

    @staticmethod
    def validate_password(user):


        pass

