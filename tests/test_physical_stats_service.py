from random import randint
from unittest import TestCase

from database.database import SQLITE
from di_containers.di_containers import Configs, Services
from models.physical_stats import PhysicalStats
from models.user_model import User


class TestPhysicalStatsService(TestCase):
    Configs.dbname.override('fitness_db.sqlite')
    Configs.dbtype.override(SQLITE)
    physical_stats_service = Services.physical_stats_service()
    user_service = Services.user_service()

    def test_create_new_physical_stats(self):
        user = User(
            fullname="New user service user.",
            login="On Service " + str(randint(-1000, 1000)),
            password="pass123")
        self.user_service.create_new_user(user)

        physical_stats = PhysicalStats(user_id=user.id, weight=78, height=190, age=23, gender="male",
                                       level_of_activity="medium")

        self.physical_stats_service.create_new_physical_stats(physical_stats)
        assert physical_stats.id is not None

    def test_get_user_info(self):
        user = User(
            fullname="New user service user.",
            login="On Service " + str(randint(-1000, 1000)),
            password="pass123")
        self.user_service.create_new_user(user)

        physical_stats = PhysicalStats(user_id=user.id, weight=78, height=190, age=23, gender="male",
                                       level_of_activity="medium")

        assert self.physical_stats_service.get_user_info(physical_stats) is not None

    def test_delete_physical_stats(self):
        user = User(
            fullname="New user service user.",
            login="On Service " + str(randint(-1000, 1000)),
            password="pass123")
        self.user_service.create_new_user(user)

        physical_stats = PhysicalStats(user_id=user.id, weight=78, height=190, age=23, gender="male",
                                       level_of_activity="medium")

        self.physical_stats_service.create_new_physical_stats(physical_stats)
        assert physical_stats.id is not None
        deleted_physical_stats = self.physical_stats_service.delete_physical_stats(physical_stats.id)
        assert deleted_physical_stats is not None

    def test_get_physical_stats_by_user_id(self):
        user = User(
            fullname="New user service user.",
            login="On Service " + str(randint(-1000, 1000)),
            password="pass123")
        self.user_service.create_new_user(user)

        assert self.physical_stats_service.get_physical_stats_by_user_id(user.id) is None

        physical_stats = PhysicalStats(user_id=user.id, weight=78, height=190, age=23, gender="male",
                                       level_of_activity="medium")

        self.physical_stats_service.create_new_physical_stats(physical_stats)
        assert self.physical_stats_service.get_physical_stats_by_user_id(user.id) is not None


