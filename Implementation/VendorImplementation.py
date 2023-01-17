from Abstractions.Vendor import Vendor
from Models.VendorModel import VendorModel
from Models.VendorSessionModel import VendorSessionModel


class VendorImplementation(Vendor):

    def __init__(self):
        self.vendor_model = VendorModel()
        self.vendor_session = VendorSessionModel()
        
    def login(self, username, password):
        # Add you code here after verifying the vendor data exists in the dictionary
        if self.vendor_model.is_correct_vendor(username, password):
            self.vendor_session.login(username) 
            print(f" logged in successfully". format(username))
            return True
        else:
            print("Invalid Username or Password")
            return False
        
    def logout(self, username):
        # Add your code here to log out the current vendor
        if (username in VendorSessionModel.vendor_session_db):
            print(f" logged out successfully".format(username))
        else:
            return False
