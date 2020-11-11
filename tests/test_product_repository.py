from unittest import TestCase

from database.database import SQLITE
from di_containers.di_containers import Configs, Repositories
from models.product import Product


class TestProductRepository(TestCase):
    Configs.dbname.override('fitness_db.sqlite')
    Configs.dbtype.override(SQLITE)
    repo = Repositories.product_repo()

    def test_get_all_products(self):
        print(self.repo.get_all_products())
        assert self.repo.get_all_products() is not None

    def test_create_product(self):
        # Arrange
        productA = Product(name="Vegan donat with meat", carb = 51, fat = 25, protein= 4.9)
        # Act
        self.repo.create_product(productA)
        print("With a unique login", productA)
        # Assert
        # Should be not None as id was assigned by Database
        assert productA.id is not None

    def test_get_product_by_id(self):
        assert self.repo.get_product_by_id(2) is not None

    def test_delete_product(self):
        productA = Product(name="Vegan donat with meat", carb=51, fat=25, protein=4.9)
        self.repo.create_product(productA)
        self.repo.delete_product(productA)
        assert self.repo.get_product_by_id(productA.id) is None
