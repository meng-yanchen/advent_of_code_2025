input = [
    "..@@.@@@@.",
    "@@@.@.@.@@",
    "@@@@@.@.@@",
    "@.@@@@..@.",
    "@@.@@@@.@@",
    ".@@@@@@@.@",
    ".@.@.@.@@@",
    "@.@@@.@@@@",
    ".@@@@@@@@.",
    "@.@.@@@.@.",
]

with open('input.txt', 'r') as file:
    input = file.read()
input = input.split('\n')

accessable_roles = 0

grid = {}
i = 1
grid[0] = "." * (len(input[0]) +2)
for line in input:
    # print(line)
    grid[i] = "." + line +"."
    i += 1
grid[len(input)+1] = "." * (len(input[0]) +2)

coordinates = {}
for row in range(1, len(grid) -1):
    # print("row above :", grid[row -1])
    # print(f"row: {row} => {grid[row]}")
    for col in range(1, len(grid[row]) -1):
        # print(f"  col: {grid[row][col]}", row, col)
        current = grid[row][col]
        # print(f"row: {row} col: {col} current: {current}")
        # check sourrounding
        surrounding = 0
        up = grid[row -1][col]
        if up == "@":
            surrounding += 1
        down = grid[row +1][col]
        if down == "@":
            surrounding += 1
        left = grid[row][col -1]
        if left == "@":
            surrounding += 1
        right = grid[row][col +1]
        if right == "@":
            surrounding += 1
        left_up = grid[row -1][col -1]
        if left_up == "@":
            surrounding += 1
        right_up = grid[row -1][col +1]
        if right_up == "@":
            surrounding += 1
        left_down = grid[row +1][col -1]
        if left_down == "@":
            surrounding += 1
        right_down = grid[row +1][col +1]
        if right_down == "@":
            surrounding += 1
        if surrounding < 4 and current == "@":
            accessable_roles += 1
            # coordinates[(row, col)] = current

# print("coordinates:", coordinates)
print(f"accessable_roles: {accessable_roles}")