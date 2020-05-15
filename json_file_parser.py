import json

def json_credentials():
    '''
    Converts json file to username,password
    '''
    with open('credential.json') as f:
        content = json.load(f)
    return content

def json_mail_info():
    '''
    Converts json file to to,cc,subject,body
    '''
    with open('mail_info.json') as f:
        content = json.load(f)
    return content