from unittest import TestCase

from database.database import SQLITE
from di_containers.di_containers import Configs, Repositories
from models.physical_stats import PhysicalStats


class TestPhysicalStatsRepository(TestCase):
    Configs.dbname.override('fitness_db.sqlite')
    Configs.dbtype.override(SQLITE)
    repo = Repositories.physical_stats_repo()

    def test_get_all_physical_statss(self):
        print(self.repo.get_all_physical_stats())
        assert self.repo.get_all_physical_stats() is not None

    def test_create_physical_stats(self):
        # Arrange
        physical_statsA = PhysicalStats(user_id=2, weight=78, height=190, age=23, gender="male",
                                        level_of_activity="medium")
        # Act
        self.repo.create_physical_stats(physical_statsA)
        print("With a unique login", physical_statsA)
        # Assert
        # Should be not None as id was assigned by Database
        assert physical_statsA.id is not None

    def test_get_physical_stats_by_id(self):
        assert self.repo.get_physical_stats_by_id(2) is not None

    def test_delete_physical_stats(self):
        physical_statsA = PhysicalStats(user_id = 2, weight = 78, height = 190, age = 23, gender="male", level_of_activity = "medium")
        self.repo.create_physical_stats(physical_statsA)
        self.repo.delete_physical_stats(physical_statsA)
        assert self.repo.get_physical_stats_by_id(physical_statsA.id) is None
