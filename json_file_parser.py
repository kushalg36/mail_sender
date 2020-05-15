import json

def json_credentials():
    with open('credential.json') as f:
        content = json.load(f)
    return content
