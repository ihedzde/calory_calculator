from unittest import TestCase

from database.database import SQLITE
from di_containers.di_containers import Configs, Repositories
from models.user_model import User
from random import randint


class TestUserRepository(TestCase):
    Configs.dbname.override('fitness_db.sqlite')
    Configs.dbtype.override(SQLITE)
    repo = Repositories.user_repo()

    def test_get_all_users(self):
        print(self.repo.get_all_users())
        assert self.repo.get_all_users() is not None

    def test_create_user(self):
        # Arrange
        # Login is UNIQUE filled, so we use random for new unique login field.
        userA = User(fullname='UserA', login="user" + str(randint(-1000, 1000)), password="hashed with salt")
        # Act
        self.repo.create_user(userA)
        print("With a unique login", userA)
        # Assert
        # Should be not None as id was assigned by Database
        assert userA.id is not None
    def test_get_user_by_id(self):
        assert self.repo.get_user_by_id(2) is not None

    def test_delete_user(self):
        userA = User(fullname='UserA', login="user" + str(randint(-1000, 1000)), password="hashed with salt")
        self.repo.create_user(userA)
        self.repo.delete_user(userA)
        assert self.repo.get_user_by_id(userA.id) is None
