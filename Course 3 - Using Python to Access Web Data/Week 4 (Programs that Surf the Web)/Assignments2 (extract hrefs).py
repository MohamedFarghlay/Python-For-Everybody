import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup as bs
import ssl
import requests

def openURL(url):
    # Ignore SSL certificate errors 
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    html = urllib.request.urlopen(url, context=ctx).read()
    return html

def htmlParser(html_content):
    soup = bs(html_content,'html.parser')
    return soup

#url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
url = "http://py4e-data.dr-chuck.net/known_by_Allice.html"
html = openURL(url)
soup = htmlParser(html)
response = requests.request(
    'GET',
    url
)
hhtml = openURL(response)
soup = htmlParser(hhtml)
tags = soup('a')
pos = 17
n_repeat = 8
i = 0
while i < n_repeat:
    tag = tags[pos].get('href',None)
    print(tag)
    url = tag
    html = openURL(url)
    soup = htmlParser(html)
    tags = soup('a')
    i+=1
    
    
    
    