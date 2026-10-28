from dataclasses import asdict

from app.repositories.product_repository import ProductRepository


class ProductService:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def get_all_products(self):

        products = self.repository.get_all()

        return [asdict(product) for product in products]

    def get_product(self, product_id: int):

        product = self.repository.get_by_id(product_id)

        if product is None:
            return None

        return asdict(product)

    def create_product(self, product_data: dict):

        product = self.repository.create(product_data)

        return asdict(product)

    def update_product(self, product_id: int, product_data: dict):

        product = self.repository.update(
            product_id,
            product_data
        )

        if product is None:
            return None

        return asdict(product)

    def delete_product(self, product_id: int):

        product = self.repository.delete(product_id)

        if product is None:
            return None

        return asdict(product)