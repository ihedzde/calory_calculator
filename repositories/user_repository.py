import sqlite3

from models.user_model import User
class UserRepository:
    def __init__(self):
       try:
           self.conn = sqlite3.connect('users.db')
       except sqlite3.Error as e:
            raise e
    def __del__(self):
        self.conn.close()

    def get_all_user(self):
         pass
         #return self.conn.cursor().execute("SELECT * FROM users")
    def get_user_by_id(self, id):
        pass

    def autheticate_user(self, user):
        pass
    def update_user(self, id, password):
        pass
    def delete_user(self, id):
        pass

    def create_user(self, name, password, physical_stats_id):
        if name in self.get_all_user():
            raise Exception("The user with that name is already exist")
        user = User(name, password, physical_stats_id)
        query = '''
            INSERT INTO users(name, physical_stats_id, hashed_password
            VALUES(?,?,?)
        '''
        self.conn.cursor().execute(query, user)
