
class ProductService:
    def __init__(self, product_repo):
        self.product_repo = product_repo

    def get_all_product(self):
        return self.product_repo.get_all_products()

    def get_product_by_id(self, product_id):
        return self.product_repo.get_product_by_id(product_id)
    def delete_product(self, id):
        product = self.product_repo.get_product_by_id(id)
        self.product_repo.delete_product(product)
        return product
    def create_new_product(self, product):
        self.product_repo.create_product(product)
    def update_product(self):
        self.product_repo.save_update_changes()
