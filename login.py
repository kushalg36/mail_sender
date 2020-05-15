from driver import new_driver
from json_file_parser import json_credentials

"""
TODO
1. Set the value of username in enviroment variable ----DONE
2. Set the value of password in enviroment variable ----DONE
3. Create logs
"""

"""
===================================
IMPORTANT:
Inorder to change password- change the value of instance variable at line 8
===================================
"""
class login:
    def __init__(self):
        self.credentials = json_credentials()
        self.username=self.credentials['username']
        self.password=self.credentials['password']
        self.driver = new_driver()
        self.url='https://myshare.vodafoneidea.com'
        self.driver.get(self.url)
    
    def login_now(self):
        """
        logs user in the portal
        """
        credentials = self.driver.find_elements_by_css_selector('.form-control')
        username,password = credentials
        
        username.send_keys(self.username) #Username
        password.send_keys(self.password) #Password

        submit = self.driver.find_element_by_css_selector('.btn.btn-primary.hidden-xs')
        submit.click()
        return True
        