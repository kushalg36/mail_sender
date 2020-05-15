from driver import new_driver
from json_file_parser import json_credentials
import time
from drag_and_drop_func import drop_files

"""
TODO
1. Set the value of username in enviroment variable ----DONE
2. Set the value of password in enviroment variable ----DONE
3. Create logs
4. Password check
5. Seperate json file for mail construction 
"""

"""
===================================
IMPORTANT:
Inorder to change password- change the value of instance variable at line 8
===================================
"""
class filler:
    def __init__(self):
        self.credentials = json_credentials()
        self.username=self.credentials['username']
        self.password=self.credentials['password']
        self.driver = new_driver()
        self.url='https://myshare.vodafoneidea.com'
        self.driver.get(self.url)
        self.driver
    
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

    def mail_builder(self):
        """
        Fills the mail content
        """
        to = self.driver.find_element_by_id('message_recipients')
        to.send_keys('Kushal.Gupta1@vodafoneidea.com')
        
        cc=self.driver.find_element_by_css_selector('.btn.clsIdeaMsgButton')
        cc.click()
        time.sleep(5)
        cc=self.driver.find_element_by_id('message_cc')
        cc.send_keys('tcs.unifyupssmisops@tcs.com')

        subject=self.driver.find_element_by_id('message_subject')
        subject.send_keys('#####TESTING#####')

        body = self.driver.find_element_by_id('message_message')
        body.send_keys('MAIL SENT YAYAYYAYA!!!!')

    def drag_n_drop(self):

        dropzone = self.driver.find_element_by_css_selector(".html5.drop_target")
        dropzone.drop_files("C://Users//kusha//OneDrive//Desktop//project//deep learning//datasets//crypto_data//crypto_data//BCH-USD.csv")