import urllib.request, urllib.parse, urllib.error

file = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

for line in file:
    print(line.decode().strip()+"\n")
    
        
    
    