
if __name__ == "__main__":
    try:
        with open('./input.txt', 'r') as file:
            config = file.read()
        instructions = config.split('\n')
        print(f"Configuration loaded successfully: {len(instructions)} instructions found.")

        hit_zero_count = 0
        current_position = 50
        for instruction in instructions:
            # print(f"Processing instruction: {instruction}")

            to_move = int(instruction[1:])

            if to_move > 100:
                to_move = to_move % 100

            if instruction.startswith("L"):

                ticks_to_move = current_position - to_move
                if ticks_to_move < 0:
                    ticks_to_move += 100
                # print(f"Moving to position: {ticks_to_move}")
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

                # print(f"Moving to position: {ticks_to_move}")
                for _ in range(to_move):
                    current_position += 1
                    if current_position > 99:
                        current_position = 0

        print(f"Final position: {current_position}, Total times hit zero: {hit_zero_count}")

    except Exception as e:
        print(e)
