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

            for id in range(start, end +1):
                id_str = str(id)

                id_substring_len = 1
                while id_substring_len <= len(id_str) // 2:
                    
                    if (len(id_str) % id_substring_len) != 0:
                        id_substring_len += 1
                        continue

                    if id_str[0:id_substring_len] == id_str[-id_substring_len:]:
                        splits = id_str.split(id_str[:id_substring_len])
                        if all(s == '' for s in splits[1:-1]):
                            # print(f"in range: {r} found invalid_id: {id}")
                            password += id
                            break

                    id_substring_len += 1

        print(f"Result: {password}")
        # assert=34284458938

    except Exception as e:
        print(e)