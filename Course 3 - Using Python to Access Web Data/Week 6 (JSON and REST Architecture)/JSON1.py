import json

data = '''
    {
        "name" : "Mohamed",
        "phone": {
            "type" : "intl",
            "number" : "477855"
        },
        "email" : {
            "hide" : "yes"
        }
    }
'''

info = json.loads(data)
print('Name : ', info['name'])
print('Hide : ', info['email']['hide'])
