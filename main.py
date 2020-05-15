from login import filler

'''
TODO
1. Implement try catch
2. Implement IF-ELSE condition to handle any changes in website (Line no. 13)
'''

if __name__=='__main__':
    login_obj = filler()
    # try:
    if(login_obj.login_now()):
        login_obj.mail_builder()
        login_obj.drag_n_drop()
        login_obj.check_box()
    else:
        print('Not able to login! Please check the password!')
    # except Exception(e):
    #     print('Something went wrong! Please check the logs: ',e)
    # finally:
    login_obj.close()