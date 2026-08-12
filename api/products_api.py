from api.base_api import BaseAPI

class ProductsAPI(BaseAPI):

    def get_all_products(self, params=None):
        return self.get('/products', params=params)

    def get_product_by_id(self, product_id):
        return self.get(f'/products/{product_id}')

    def search_products(self, query):
        return self.get('/products/search',params={"q":query})

    def get_all_categories(self):
        return self.get('/products/categories')

    def get_products_by_category(self, category):
        return self.get(f"/products/category/{category}")

    def add_product(self, payload):
        return self.post('/products/add',payload)

    def update_product(self, product_id, payload):
        return self.put(f"/products/{product_id}", payload)

    def patch_product(self, product_id, payload):
        return self.patch(f"/products/{product_id}", payload)

    def delete_product(self, product_id):
        return self.delete(f"/products/{product_id}")

