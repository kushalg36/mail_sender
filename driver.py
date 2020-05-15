from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

'''
=========================================
IMPORTANT:
1. Add the file system link of the driver to enviroment variables
=========================================
'''

def new_driver():
    '''
    Instantiate chrome object
    '''
    browser = webdriver.Chrome()
    return browser
