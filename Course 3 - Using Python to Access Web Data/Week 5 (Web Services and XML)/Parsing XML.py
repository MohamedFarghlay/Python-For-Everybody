import xml.etree.ElementTree as ET
data = '''
<person>
    <name>mohamed</name>
    <phone type="intl"> 
        485596314 
    </phone>
    <email hide="yes"/> 
</person>'''
tree = ET.fromstring(data)
print('name: ', tree.find('name').text)
print('Attr: ', tree.find('email').get('hide'))
