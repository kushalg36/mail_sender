from login import filler

'''
TODO
1. Implement try catch ---DONE
2. Implement IF-ELSE condition to handle any changes in website (Line no. 13) ---DONE
'''

# ===================================
# Python: Automated file sender using selenium
# source: https://github.com/kushalg36/mail_sender
# ===================================

# ===================================
# Failure scenarios
# 1) Password might got old
# 2) Filename/Filepath isn't correct
# 3) Program is getting closed before mail sending/file upload
# 4) Elements in webpage got changed from the developers of myshare domain
# ===================================

if __name__=='__main__':
    login_obj = filler()

    login = login_obj.login_now()

    if(login==False):
        print("Credentials incorrect! Please check the credentials in credential.json file.")
        login_obj.close()
    else:
        login_obj.mail_builder()
        login_obj.drag_n_drop()
        login_obj.check_box()
        login_obj.close()