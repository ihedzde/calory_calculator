from sqlalchemy import Column, Integer, String, Float

from database.database import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    protein = Column(Float)
    fat = Column(Float)
    carb = Column(Float)

    def __repr__(self):
        return f'Product: id:{self.id}, name:{self.name}, carbs:{self.carb*100}, fats:{self.fat*100}, proteins:{self.protein*100}.'

    def get_nutrition(self, weight):
        return {'carbs': weight*self.carb*4, 'fats': weight*self.fat*9, 'proteins':weight*self.protein*4}

    def count_calories(self, weight):
        return weight * (self.protein / 100 * 4 + self.fat/100 * 9 + self.carb/100 * 4)
