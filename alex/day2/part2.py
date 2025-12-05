input = [
    "11-22","95-115","998-1012","1188511880-1188511890","222220-222224","1698522-1698528","446443-446449","38593856-38593862","565653-565659","824824821-824824827","2121212118-2121212124"
]
with open('./input.txt', 'r') as file:
    input = file.read()
input = input.split(',')

password = 0

for r in input:
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
                    password += id
                    break

            id_substring_len += 1

print(f"answer: {password}")

