
if __name__ == "__main__":
    try:
        with open('input.txt', 'r') as file:
            config = file.read()
        banks = config.split('\n')
        print(f"Configuration loaded successfully: {len(banks)} instructions found.")

        totalJoltage = 0
        for bank in banks:
            bank = [int(x) for x in bank]
            firstBattery = max(bank) # find the first battery
            firstBatteryLocation = bank.index(firstBattery)
            if firstBatteryLocation == 0:
                firstHalf = []
                secondHalf = bank[1:]
                battery = firstBattery*10 + max(secondHalf) 
            elif firstBatteryLocation == len(bank) - 1:
                firstHalf = bank[:-1]
                secondHalf = []
                battery = max(firstHalf)*10 + firstBattery
            else:
                firstHalf = bank[:firstBatteryLocation]
                secondHalf = bank[-((len(bank)-1) - firstBatteryLocation):]
                battery1 = max(firstHalf)*10 + firstBattery
                battery2 = firstBattery*10 + max(secondHalf)
                battery = max(battery1, battery2)
            print(f"Calculated battery value: {battery}")
            totalJoltage += battery
        print(f"Total joltage: {totalJoltage}")


    except Exception as e:
        print(e)