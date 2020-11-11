from sqlalchemy import Column, Integer, ForeignKey, Float, String

from database.database import Base


class PhysicalStats(Base):
    __tablename__ = "physical_stats"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    weight = Column(Float)
    height = Column(Float)
    age = Column(Integer)
    gender = Column(String)
    level_of_activity = Column(String)
    def bmi(self):
        return self.weight/(self.height/100)**2
    def bmr(self):
        if self.gender == "male":
            return 88.362 + (13.397*self.weight) + (4.799 * self.height) + (5.677 * self.age)
        if self.gender == "female":
            return 447.593 + (9.247*self.weight) + (3.097 * self.height) + (4.33 * self.age)
    