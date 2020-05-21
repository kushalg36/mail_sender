from login import filler

'''
TODO
1. Implement try catch
2. Implement IF-ELSE condition to handle any changes in website (Line no. 13)
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
# ===================================

if __name__=='__main__':
    login_obj = filler()
    
    login_obj.login_now()
    # login_obj.mail_builder()
    # login_obj.drag_n_drop()
    # login_obj.check_box()
    # login_obj.close()