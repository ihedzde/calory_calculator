from random import randint
from unittest import TestCase

from database.database import SQLITE
from di_containers.di_containers import Configs, Services
from models.user_model import User


class TestUserService(TestCase):
    Configs.dbname.override('fitness_db.sqlite')
    Configs.dbtype.override(SQLITE)
    user_service = Services.user_service()

    def test_create_new_user(self):
        user = User(
            fullname="New user service user.",
            login="On Service " + str(randint(-1000, 1000)),
            password="pass123")
        self.user_service.create_new_user(user)
        assert user.id is not None

    def test_verify_user(self):
        login = "On Service " + str(randint(-1000, 1000))

        password = "pass123"
        user = User(
            fullname="New user service user.",
            login=login,
            password=password)
        self.user_service.create_new_user(user)
        user2 = User(login=login, password=password)
        assert self.user_service.verify_user(user2) is not None

    def test_delete_user(self):
        user = User(
            fullname="New user service user.",
            login="On Service " + str(randint(-1000, 1000)),
            password="pass123")
        self.user_service.create_new_user(user)
        assert user.id is not None
        deleted_user = self.user_service.delete_user(user.id)
        assert deleted_user is not None
