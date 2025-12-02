
import os 
with open("input.txt", "r") as file:
    input = file.read()
    input = input.split(',')
    print(input)

sum = 0
# find the range of the IDs
for rangeOfID in input:
    firstValueOfRange = int(rangeOfID.split('-')[0])
    lastValueOfRange = int(rangeOfID.split('-')[1])
    
    for id in range(firstValueOfRange, lastValueOfRange+1):
        # checking if each ID in the range is odd number of digits or even number of digits
        numberOfDigits = len(str(id))
        if numberOfDigits % 2 == 0:
            strID = str(id)
            halfLength = len(strID) // 2
            firstHalf = strID[:halfLength]
            secondHalf = strID[-halfLength:]
            if firstHalf == secondHalf:
                print("invalid ID:" + strID)
                sum += id
                
    

print(sum)

        

