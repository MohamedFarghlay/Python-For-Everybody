import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/comments_1385323.xml'

else:
    serviceurl = 'http://py4e-data.dr-chuck.net/comments_42.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:

    uh = urllib.request.urlopen(serviceurl, context=ctx)

    data = uh.read()
    tree = ET.fromstring(data)
    counts = tree.findall('.//count')
    total = 0
    for c in counts:
        total += int(c.text)
    print(total)
    break
