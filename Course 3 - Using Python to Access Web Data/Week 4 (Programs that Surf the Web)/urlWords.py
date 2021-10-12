import urllib.request, urllib.parse, urllib.error

file = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for lines in file:
    line = lines.decode().split()
    for word in line:
        counts[word] = counts.get(word,0) + 1
        
print(counts)
        
    
    