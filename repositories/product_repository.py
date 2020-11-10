from models.product import Product


class ProductRepository:
    def __init__(self, database):
        self.session = database.session()
        database.create_db_tables()

    def get_all_products(self):
        return self.session.query(Product).all()

    def get_product_by_id(self, id):
        for product in self.session.query(Product):
            if product.id == id:
                return product
        return None

    def safe_update_changes(self):
        self.session.commit()

    def delete_product(self, product):
        self.session.delete(product)
        self.safe_update_changes()

    def create_product(self, product):
        self.session.add(product)
        self.safe_update_changes()
