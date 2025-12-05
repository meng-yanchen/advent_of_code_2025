input = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82",
]
with open('input.txt', 'r') as file:
    input = file.read()
input = input.split('\n')

password = 0
position = 50

for instruction in input:

    to_move = int(instruction[1:])

    if to_move > 100:
        to_move = to_move % 100
        full_rotations = int(instruction[1:]) // 100
        password += full_rotations

    if instruction.startswith("L"):
        for _ in range(to_move):
            position -= 1
            if position < 0:
                position = 99
            if position == 0:
                password += 1

    elif instruction.startswith("R"):

        for _ in range(to_move):
            position += 1
            if position > 99:
                position = 0
            if position == 0:
                password += 1

print(f"answer: {password}")
