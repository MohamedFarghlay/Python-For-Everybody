### Scraping Numbers from HTML
from os import access
import urllib.request, urllib.error
import re
from bs4 import BeautifulSoup as bs
from bs4.element import TemplateString


def getNumbers(file):
    numbers = re.findall(r'\d+',file)
    return numbers

def openURL(url):
    html_response = urllib.request.urlopen(url).read()
    return html_response


def htmlParser(html_content):
    soup = bs(html_content,'html.parser')
    tags = soup('span')
    return str(tags)

def getSum(numbers):
    sum_of_numbers = 0
    for n in numbers:
        sum_of_numbers += int(n)
    return sum_of_numbers
        
def convert_to_int(list):
    int_list = []
    for n in list:
        int_list.append(int(n))
    return int_list
def main():
    #simple_url = "http://py4e-data.dr-chuck.net/comments_42.html"
    actual_url = "http://py4e-data.dr-chuck.net/comments_1385321.html"
    #get the html page
    html = openURL(actual_url)
    
    #parse html using BeautifulSoup so we can extract numbers 
    html_parsed_data = htmlParser(html)
    
    #extract number using regex
    numbers = getNumbers(html_parsed_data)
    
    #get the sum of the numbers
    res = getSum(numbers)
    print(res)
     
    

main()