from sqlalchemy.orm import sessionmaker

from models.user_model import User


class UserRepository:
    def __init__(self, database):
        self.session = database.session()
        database.create_db_tables()
    def get_all_users(self):
        return self.session.query(User).all()
    def get_user_by_id(self, id):
        for user in self.session.query(User):
            if user.id == id:
                return user
        return None
    def safe_update_changes(self):
        self.session.commit()

    def delete_user(self, user):
        self.session.delete(user)
        self.safe_update_changes()

    def create_user(self, user):
        self.session.add(user)
        self.safe_update_changes()
