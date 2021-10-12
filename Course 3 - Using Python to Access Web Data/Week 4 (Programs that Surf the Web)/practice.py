import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

def openURL(URL):
    content = urllib.request.urlopen(URL)
    return content


html_page = openURL('http://www.dr-chuck.com/page1.htm')

soup = BeautifulSoup(html_page,"html.parser")

for link in soup.findAll('a'):
    urlLink= link.get('href')
    page2 = openURL(urlLink)
    for line in page2:
        print(line.decode().strip())