from abc import abstractmethod

from Models import VendorSessionModel

class Vendor:
    def __init__(self, username, password):
        self._username = username
        self._password = password
            
    @abstractmethod
    def login(self, username, password):
        """This method will be used to login an existing Vendor."""
        if (username in VendorSessionModel.vendor_session_db):
            print(f" User logged in successfully". format(username))
            return True
        else:
            print("Invalid Username or Password")
            return False   
    
    @abstractmethod
    def logout(self, username):
        """This method will be used to logout an existing Vendor."""
        if (username in VendorSessionModel.vendor_session_db):
            print("Logged out successfully")
        else:
            return False