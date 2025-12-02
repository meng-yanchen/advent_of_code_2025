
import os 
with open("input.txt", "r") as file:
    input = file.read()
    input = input.split(',')


def factorize(value):
    listOfFactors = []
    for factor in range(1, value):
        if value % factor == 0:
            # we've found a factor!
            listOfFactors.append(factor)
    
    return listOfFactors


sum = 0
# find the range of the IDs
for rangeOfID in input:
    firstValueOfRange = int(rangeOfID.split('-')[0])
    lastValueOfRange = int(rangeOfID.split('-')[1])
    
    for id in range(firstValueOfRange, lastValueOfRange+1):
        # checking if each ID in the range is odd number of digits or even number of digits
        numberOfDigits = len(str(id))
        listOfFactors = factorize(numberOfDigits)
        for factor in listOfFactors:                  # you have 9, factor is 3
            strID = str(id)
            splitList = [strID[i:i+factor] for i in range(0, numberOfDigits, factor)]
            if len(list(set(splitList))) == 1:
                print("invalid ID:" + strID)
                sum += id
                break                
print(sum)