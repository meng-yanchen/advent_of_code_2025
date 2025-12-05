
if __name__ == "__main__":
    try:
        with open('./input.txt', 'r') as file:
            config = file.read()
        instructions = config.split('\n')
        print(f"Configuration loaded successfully: {len(instructions)} instructions found.")

#        print(instructions)
        x = 50
        counter = 0
        # check if it is negative or positive
        for input in instructions:
            direction = input[0]
            input = int(input[1:]) 
            if input >= 100:
                counter += input // 100
            input = input % 100

            if direction == 'L':
                #input = -int(input[1:])
                if input > x:
                    if x != 0:
                        counter += 1
                    x = 100 - (input - x) # solves turning left past 0 case
                else:
                    x = x - input # normal left turn
                # print(input, x, counter)
            if direction == 'R':

                if (input + x) > 100:
                    x = (input + x) - 100 # solves turning right past 0 case
                    counter += 1
                else:
                    x = x + input # normal right turn
                # print(input, x, counter)
            if x == 0 or x == 100:
                counter += 1
                x = 0
                # print(input, x, counter)
            
            print(f"instruction: {direction + (str(input))}, Current location: {x}, Counter: {counter}")
        

    except Exception as e:
        print(e)

