from login import login


if __name__=='__main__':
    login_obj = login()
    try:
        if(login_obj.login_now()):
            pass
        else:
            pass
    except Exception:
        print('Something went wrong! Please check the logs')