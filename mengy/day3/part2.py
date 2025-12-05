if __name__ == "__main__":
    try:
        with open('input_example.txt', 'r') as file:
            config = file.read()
        banks = config.split('\n')
        print(f"Configuration loaded successfully: {len(banks)} instructions found.")

        def

        batteryList = []
        for bankValue in banks:
            print(bank)

            # trim the last 12 characters
            bank = [int(x) for x in bankValue]
            for i in range(12):

                firstBattery = max(bank) # find the first battery
                firstBatteryLocation = bank.index(firstBattery)
                batteryList.append(firstBattery)
                bank = bank[firstBatteryLocation:]
                print(bank)


#            if firstBatteryLocation == (len(bank) - 12):
#                battery = bankValue[-12:]
            

                

            
            


#          batteryBuilder(firstBatteryLocation, bank)





    
    except Exception as e:
        print(e)