import urllib.request
import urllib.parse
import urllib.error
import json

serviceURL = "http://py4e-data.dr-chuck.net/comments_1385324.json"

uh = urllib.request.urlopen(serviceURL)
data = uh.read().decode()
print("len of data : ", len(data))

try:
    js = json.loads(data)
except:
    js = None

count = 0
for item in js["comments"]:
    count += item['count']
print(count)
