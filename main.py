from login import filler


if __name__=='__main__':
    login_obj = filler()
    try:
        if(login_obj.login_now()):
            login_obj.mail_builder()
        else:
            print('Not able to login! Please check the password!')
    except Exception:
        print('Something went wrong! Please check the logs')