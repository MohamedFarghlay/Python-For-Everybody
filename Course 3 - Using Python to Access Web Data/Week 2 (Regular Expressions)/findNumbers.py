from os import read

import re


def readFile():
    #open file in read mode
    #file = open(r"Sample_data.txt","r")
    file = open(r"Actual_data.txt","r")
    
    #read the content of the file and close it
    fileContent = file.read()
    file.close()
    
    #extract the number from the file
    numbers = parseNumbers(fileContent)

    return numbers

def parseNumbers(file):
    #Pares numbers using regex
    numbers = re.findall(r'\d+',file)
    return numbers

def getSum(numbersList):
    sumN = 0
    for n in numbersList:
        sumN += float(n)
    return sumN
        
def main():
    numbers = readFile()
    sumOfNumbers = getSum(numbers)
    print(sumOfNumbers)  
    
  
main()