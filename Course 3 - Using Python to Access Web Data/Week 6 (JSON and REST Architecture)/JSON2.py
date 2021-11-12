import json
import json

data = '''
[
    {
        "id" : "001",
        "x" : "2",
        "name" : "mohamed"
    },
    {
        "id": "009",
        "x" : "7",
        "name" : "Jack"
    }
]
'''


info = json.loads(data)
print("User Count : ", len(info))

for item in info:
    print("Name: ", item['name'])
    print("id: ", item['id'])
    print("Attributes : ", item['x'])
