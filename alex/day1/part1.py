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

hit_zero_count = 0
current_position = 50
for instruction in input:

    to_move = int(instruction[1:])

    if to_move > 100:
        to_move = to_move % 100

    if instruction.startswith("L"):

        ticks_to_move = current_position - to_move
        if ticks_to_move < 0:
            ticks_to_move += 100
        if ticks_to_move == 0:
            hit_zero_count += 1

        for _ in range(to_move):
            current_position -= 1
            if current_position < 0:
                current_position = 99

    elif instruction.startswith("R"):

        ticks_to_move = current_position + to_move
        if ticks_to_move > 99:
            ticks_to_move -= 100
        if ticks_to_move == 0:
            hit_zero_count += 1

        for _ in range(to_move):
            current_position += 1
            if current_position > 99:
                current_position = 0

print(f"answer: {hit_zero_count}")
