
if __name__ == "__main__":
    try:
        with open('./input.txt', 'r') as file:
            config = file.read()
        instructions = config.split('\n')
        # instructions = ["L105", "R250", "L50", "R75"]
        print(f"Configuration loaded successfully: {len(instructions)} instructions found.")

        password = 0
        position = 50

        for instruction in instructions:

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

            # print("ins: {}, old_pos: {}, new_pos: {}, old_pwd: {}, new_pwd: {}".format(instruction, old_pos, position, old_pwd, password))


        print(f"Final position: {position}, PASSWORD: {password}")

    except Exception as e:
        print(e)
