from Implementation.ProductsImplementation import ProductsImplementation
from Implementation.VendorImplementation import VendorImplementation

    
if __name__ == '__main__':
    vendor = VendorImplementation()
    username = input("Enter the username")
    password = input("Enter the password")
    #login_res = vendor.login(username, password)
    login_res = vendor.login("Rossum", "rossum_pw")
    if login_res == False:
        print("Not Authorized Vendor")
    else:
        products = ProductsImplementation("Rossum")
        print("Enter the no of products you want to add: ")
        n = int(input())
        for i in range(0, n+1):
           product_name = input("Enter the product name:")
           product_type = "Laptop"
           available_quantity = 40
           unit_price = input("Enter the price per unit:")
           products.add_product(product_name, product_type, available_quantity, unit_price)
        search_product = products.search_product_by_name("Lenovo Gaming")
        if (search_product):
            print("Searched Product details:")
            [print(key, value) for key, value in search_product.items()]
        else:
            print("No product exists by the name")
        
        all_products = products.get_all_products()

        if (all_products):
            print("All Product Details:")
            [print(key, value) for key, value in all_products.items()]
        else:
            print("No product is available to fetch.")
            
        vendor.logout("Rossum")  