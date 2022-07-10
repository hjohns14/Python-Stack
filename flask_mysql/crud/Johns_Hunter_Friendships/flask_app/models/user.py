from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db_name = "friendships_schema"

    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.friends = []


    @classmethod
    def get_all_users(cls):
        query = "select * from users;"
        result = connectToMySQL(cls.db_name).query_db(query)

        if len(result) == 0:
            return []
        else:
            return [cls(user) for user in result]
    
    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users(first_name, last_name) VALUES(%(first_name)s, %(last_name)s);"

        id = connectToMySQL(cls.db_name).query_db(query, data)

        return id

    @classmethod
    def get_users_and_friends(cls):
        query = """select * from users
                join friendships on friendships.user_id = users.id
                join users as friends on friend_id = friends.id
                order by users.id;"""

        result = connectToMySQL(cls.db_name).query_db(query)

        all_users = []
        for i in range(len(result)):
            user_data = {
                'id': result[i]['id'],
                'first_name': result[i]['first_name'],
                'last_name': result[i]['last_name'],
                'created_at': result[i]['created_at'],
                'updated_at': result[i]['updated_at']
            }

            friend_data = {
                'id': result[i]['friends.id'],
                'first_name': result[i]['friends.first_name'],
                'last_name': result[i]['friends.last_name'],
                'created_at': result[i]['friends.created_at'],
                'updated_at': result[i]['friends.updated_at']
            }


            if i == 0 :
                user = cls(user_data)
                all_users.append(user)
            elif user_data['id'] != result[i-1]['id']:
                user = cls(user_data)
                all_users.append(user)
            
            user.friends.append(cls(friend_data))

        return all_users

    @classmethod
    def make_friends(cls, data):
        query = """insert into friendships(user_id, friend_id)
                select %(user_id)s, %(friend_id)s from dual
                where not exists(
                select * from friendships
                where user_id = %(user_id)s and friend_id = %(friend_id)s)"""

        result = connectToMySQL(cls.db_name).query_db(query, data)

        return result

    

