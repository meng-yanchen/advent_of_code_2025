input = [
    "3-5",
    "10-14",
    "16-20",
    "12-18",
    # "101012613040912-105113606231378",
    "",
    "1",
    "5",
    "8",
    "11",
    "17",
    "32",
]
# with open('input.txt', 'r') as file:
#     input = file.read().split('\n')

totalFreshCount = 0
freshIngredientIdRanges = []

readFirstPart = True
for line in input:
    if readFirstPart:
        if line == "":
            readFirstPart = False
            continue
        else:
            freshIngredientIdRanges.append(line)

print(f"freshIngredientIdRanges: {len(freshIngredientIdRanges)}")

minRangeStart = int(freshIngredientIdRanges[0].split("-")[0])
maxRangeEnd = int(freshIngredientIdRanges[0].split("-")[1])

print(minRangeStart, maxRangeEnd)

uniqueRanges = []

for r in freshIngredientIdRanges:
    rangeStart = int(r.split("-")[0])
    rangeEnd = int(r.split("-")[1])

    if rangeStart > maxRangeEnd:
        print("new higher range", r, uniqueRanges)

        rangeUpdated = False
        for u in uniqueRanges:
            print(u, rangeStart, rangeEnd)
            if u[0] <= rangeStart <= u[1] and rangeEnd > u[1]:
                print("updating overlapping range", r, u)
                u[1] = rangeEnd
                rangeUpdated = True
            elif u[0] <= rangeEnd <= u[1] and rangeStart < u[0]:
                print("updating overlapping range", r, u)
                u[0] = rangeStart
                rangeUpdated = True

        if not rangeUpdated:
            uniqueRanges.append((minRangeStart, maxRangeEnd))
            minRangeStart = rangeStart
            maxRangeEnd = rangeEnd
        continue

    if rangeEnd < minRangeStart:
        print("new lower range", r)
        uniqueRanges.append((minRangeStart, maxRangeEnd))
        # totalFreshCount += maxRangeEnd - minRangeStart
        minRangeStart = rangeStart
        maxRangeEnd = rangeEnd
        continue
    if rangeStart < minRangeStart:
        print("new min", rangeStart)
        minRangeStart = rangeStart
    if rangeEnd > maxRangeEnd:
        print("new max", rangeEnd)
        maxRangeEnd = rangeEnd

uniqueRanges.append((minRangeStart, maxRangeEnd))

# while 
# print(minRangeStart, maxRangeEnd)
# totalFreshCount += maxRangeEnd - minRangeStart

print(uniqueRanges)

print(f"answer: {totalFreshCount}")
