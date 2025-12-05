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

grid = {}
i = 1
grid[0] = "." * (len(input[0]) +2)
for line in input:
    grid[i] = "." + line +"."
    i += 1
grid[len(input)+1] = "." * (len(input[0]) +2)

def extract_roles(grid):
    accessable_roles = 0
    grid_copy = grid
    for row in range(1, len(grid) -1):
        for col in range(1, len(grid[row]) -1):
            current = grid[row][col]
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
                old_row = grid_copy[row]
                grid_copy[row] = old_row[:col] + "." + old_row[col+1:]
    # print(f"found new roles: {accessable_roles}")
    return accessable_roles, grid_copy

total_roles = 0
new_grid = None
while True:
    if new_grid:
        new_accessable_roles, new_grid = extract_roles(new_grid)
    else:
        new_accessable_roles, new_grid = extract_roles(grid)
    if new_accessable_roles == 0:
        break
    total_roles += new_accessable_roles

print(f"total_roles: {total_roles}")
# for row in new_grid:
#     print(new_grid[row])