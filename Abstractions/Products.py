from abc import abstractmethod

class Products:
    def __init__(self, add_product, search_product_by_name, get_all_products):
        self.add_product = add_product
        self.search_product_by_name = search_product_by_name
        self.get_all_products = get_all_products

    @abstractmethod
    def add_product(self, product_name, product_type, available_quantity, unit_price):
        self.product_name = product_name
        self.product_type = product_type
        self.available_quantity = available_quantity
        self.unit_price = unit_price
        return self.add_product(product_name, product_type, available_quantity, unit_price)
   
    @abstractmethod
    def search_product_by_name(self, product_name):
        return self.product_model.search_product(product_name)
        

    @abstractmethod
    def get_all_products(self):
        return self.product_model.all_products()
 