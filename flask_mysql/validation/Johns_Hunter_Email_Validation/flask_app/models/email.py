import email
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    db_name = "emails_schema"

    def __init__(self, data) -> None:
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save_to_db(cls, data):
        query = "INSERT INTO emails(email) VALUES(%(email)s)"

        results = connectToMySQL(cls.db_name).query_db(query, data)

        return results

    @classmethod
    def get_all_emails(cls):
        query = "SELECT * FROM emails"

        results = connectToMySQL(cls.db_name).query_db(query)

        if len(results) == 0:
            return []

        emails = [cls(email_data) for email_data in results]

        return emails

    @classmethod
    def delete_from_db(cls, data):
        query = "DELETE FROM emails WHERE id = %(id)s"

        connectToMySQL(cls.db_name).query_db(query, data)

    @staticmethod
    def validate_email(user):
        is_valid = True

        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid user email!", 'email')
            is_valid = False

        all_emails = Email.get_all_emails()
        
        for email_class in all_emails:
            if user['email'] == email_class.email:
                flash("Email is already Taken!")
                is_valid = False
        
        return is_valid
