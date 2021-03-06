from driver import new_driver
from json_file_parser import json_credentials,json_mail_info
import time
from drag_and_drop_func import drop_files

"""
TODO
1. Set the value of username in enviroment variable ----DONE
2. Set the value of password in enviroment variable ----DONE
3. Create logs ---BUG
4. Password check ---DONE
5. Seperate json file for mail construction ----DONE
6. Handle chrome version ---CHROMIUM BUG-CAN'T BE HANDLED
"""


# ===================================
# IMPORTANT:
# Inorder to change password- change the password in credential.json file
# Inorder to change filepath/to/cc/body- change the content in json_file_parser file
# ===================================

class filler:
    def __init__(self):
        self.credentials = json_credentials()
        self.mail_info = json_mail_info()
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

        # To handle failed login attempt exceptions
        time.sleep(5)
        isLoggedIn = True
        try:
            self.driver.find_element_by_id('message_recipients')
            isLoggedIn = True
        except:
            isLoggedIn = False
        finally:
            return isLoggedIn

    def mail_builder(self):
        """
        Fills the mail content
        """
        try:
            to = self.driver.find_element_by_id('message_recipients')
            to.send_keys(self.mail_info['to'])
            cc=self.driver.find_element_by_css_selector('.btn.clsIdeaMsgButton')
            cc.click()
            time.sleep(2)
            cc=self.driver.find_element_by_id('message_cc')
            cc.send_keys(self.mail_info['cc'])

            subject=self.driver.find_element_by_id('message_subject')
            subject.send_keys(self.mail_info['subject'])

            body = self.driver.find_element_by_id('message_message')
            body.send_keys(self.mail_info['body'])
        except:
            print('Elements have been changed in website!')

    def drag_n_drop(self):
        '''
        Tackle drag and drop of files from filesystem
        '''
        dropzone = self.driver.find_element_by_css_selector(".html5.drop_target")
        try:
            file_path = self.mail_info['filepath']
            dropzone.drop_files(file_path)
        except:
            print("File path is incorrect!")

    def check_box(self):
        '''
        Check checkbox for auto-sending
        '''
        try:
            auto_send_check = self.driver.find_element_by_id('done_editing')
            auto_send_check.click()
        except:
            print("Checkbox is not working!")

    def close(self):
        time.sleep(10)
        self.driver.quit()