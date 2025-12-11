import math

input = [
    "123 328  51 64 ",
    " 45 64  387 23 ",
    "  6 98  215 314",
    "*   +   *   +  ",
]
with open('./input.txt', 'r') as file:
    input = file.read().split('\n')

columns = {}
rowData = []
for line in input:
    rowElements = line.split(" ")
    rowElements = [r for r in rowElements if r != ""]
    rowData.append(rowElements)

    i = 0
    for r in rowElements:
        columns[i] = [] 
        i += 1

for r in rowData:
    i = 0
    for j in r:
        columns[i].append(j)
        i += 1

grandTotal = 0
for c in columns:
    operand = columns[c][-1]
    if operand == "+":
        grandTotal += sum([int(x) for x in columns[c][:-1]])
    elif operand == "*":
        grandTotal += math.prod([int(x) for x in columns[c][:-1]])
    else:
        raise Exception("Unknown operand", operand)

print(f"answer: {grandTotal}")
