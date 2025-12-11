input = [
    "3-5",
    "10-14",
    "16-20",
    "12-18",
    "",
    "1",
    "5",
    "8",
    "11",
    "17",
    "32",
]
with open('input.txt', 'r') as file:
    input = file.read().split('\n')

freshIngredientIdRanges = []
availableIds = []

readFirstPart = True
for line in input:
    if readFirstPart:
        if line == "":
            readFirstPart = False
            continue
        else:
            freshIngredientIdRanges.append(line)
    else:
        availableIds.append(int(line))

totalFreshCount = 0

for id in availableIds:
    for r in freshIngredientIdRanges:
        rangeStart = int(r.split("-")[0])
        rangeEnd = int(r.split("-")[1])

        if id >= rangeStart and id <= rangeEnd:
            totalFreshCount += 1
            break

print(f"answer: {totalFreshCount}")
