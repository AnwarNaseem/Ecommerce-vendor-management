from Abstractions.Products import Products
from Models.ProductModel import ProductModel
from Models.VendorSessionModel import VendorSessionModel


class ProductsImplementation(Products):

    def __init__(self, username):
        self.product_model = ProductModel()
        self.vendor_session = VendorSessionModel()
        self._username = username

    def add_product(self, product_name, product_type, available_quantity, unit_price):
        # check if the vendor is logged in, then add the product and return True else Return False
        if self.vendor_session.check_login(self._username) == True:
            self.product_model.add_product(product_name, product_type, available_quantity, unit_price)
            print(product_name + " added successfully")
            return True
        else:
            print("Please signup or login first")
            return False
            
    def search_product_by_name(self, product_name):
        # Search if the product is available in the dictionary if the vendor is authorized to access else return False
        # If product is available then return product
        if self.vendor_session.check_login(self._username) == True:
            return self.product_model.search_product(product_name)
        else:
            print(f"User {self._username} not logged in .")
         
        retrieved_product = self.product_model.search_product(product_name)
        return retrieved_product

    def get_all_products(self):
        # Check if the vendor can retrieve all the product if not return False
        # otherwise return all the products 
        if self.vendor_session.check_login(self._username) == True:
            if self.product_model.all_products():
                return self.product_model.all_products()
            else:
                print("Product not available")
                return False
        else:
            print(f"User {self._username} not logged in .")
            
        products = self.product_model.all_products()
        return products


