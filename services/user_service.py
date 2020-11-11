import hashlib
import os

from models.user_model import User


class UserService:
    def __init__(self, user_repo):
        self.user_repo = user_repo


    def _hash_password_with_salt(self, password):
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=128)
        return {'key': key, 'salt': salt}

    def _verify(self, salt, key, password):

        new_key = hashlib.pbkdf2_hmac('sha256', password.encode("utf-8"), salt, 100000, dklen=128)
        if new_key == key:
            return True
        else:
            return False

    def delete_user(self, id):
        user = self.user_repo.get_user_by_id(id)
        self.user_repo.delete_user(user)
        return user
    def create_new_user(self, user):
        if user.login in [u.login for u in self.user_repo.get_all_users()]:
            raise Exception("User with that login is already exists")
        key_salt = self._hash_password_with_salt(user.password)
        user.password = key_salt['salt'] + key_salt['key']
        self.user_repo.create_user(user)
    def update_users(self):
        self.user_repo.save_update_changes()
    def verify_user(self, user):
        user_from_repo = next(filter(lambda x: x.login == user.login, self.user_repo.get_all_users()))

        if user_from_repo is None:
            raise Exception("User not found.")
        elif self._verify(user_from_repo.password[:32],user_from_repo.password[32:], user.password):
            return user_from_repo
        else:
            raise Exception("Wrong password")
