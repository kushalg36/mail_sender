from driver import new_driver
"""
TODO
1. Set the value of password in enviroment variable
"""

"""
Inorder to change password- change the value of instance variable at line 8
"""
class login:
    def __init__(self):
        self.username="Rahul.Mane1@vodafoneidea.com"
        self.password="Apr@2020"
        self.driver = new_driver()
    
    def login_now(self):
