from models.physical_stats import PhysicalStats


class PhysicalStatsRepository:

    def __init__(self, database):
        self.session = database.session()
        database.create_db_tables()

    def get_all_physical_stats(self):
        return self.session.query(PhysicalStats).all()

    def get_physical_stats_by_id(self, id):
        for stats in self.session.query(PhysicalStats):
            if stats.id == id:
                return stats
        return None

    def safe_update_changes(self):
        self.session.commit()

    def delete_physical_stats(self, physical_stats):
        self.session.delete(physical_stats)
        self.safe_update_changes()

    def create_physical_stats(self, physical_stats):
        self.session.add(physical_stats)
        self.safe_update_changes()
