from selenium import webdriver

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
