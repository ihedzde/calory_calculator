class Food:
    def __init__(self, name, proteins, fats, carbs):
        self.name = name * 0.01
        self.protein = proteins * 0.01
        self.fat = fats * 0.01
        self.carb = carbs * 0.01

    def get_nutrition(self, weight):
        return {'carbs': weight*self.carb*4, 'fats': weight*self.fat*9, 'proteins':weight*self.protein*4}

    def count_calories(self, weight):
        return weight * (self.protein * 4 + self.fat * 9 + self.carb * 4)
