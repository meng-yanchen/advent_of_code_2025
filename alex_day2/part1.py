if __name__ == "__main__":
    try:
        with open('./input.txt', 'r') as file:
            config = file.read()
        ranges = config.split(',')
        # ranges = ["11-22", "95-105", "998-1012", "4775-7265"]
        print(f"Input File loaded successfully: {len(ranges)} ranges found.")

        password = 0

        for r in ranges:
            start = int(r.split('-')[0])
            end = int(r.split('-')[1])

            for id in range(start, end+1):
                id_str = str(id)
                id_str_len = len(id_str)
                if id_str_len % 2 == 0 and id_str[0:id_str_len//2] == id_str[id_str_len//2:]:
                    # print(f"in range: {r} found invalid_id: {id}")
                    password += id

        print(f"Result: {password}")
        # assert=23701357374

    except Exception as e:
        print(e)