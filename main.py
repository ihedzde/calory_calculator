from database.database import *
from sqlalchemy import select
from models.user_model import User
if __name__ == '__main__':
    test_db = Database(SQLITE, dbname='fitness_db.sqlite')
    test_db.create_db_tables()
    user_a = User(fullname = "user_a", login = "login_a", password="hash and salt")
    print(user_a.fullname)