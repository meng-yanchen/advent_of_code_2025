input = [
    "11-22","95-115","998-1012","1188511880-1188511890","222220-222224","1698522-1698528","446443-446449","38593856-38593862","565653-565659","824824821-824824827","2121212118-2121212124"
]
with open('input.txt', 'r') as file:
    input = file.read()
input = input.split(',')

password = 0

for r in input:
    start = int(r.split('-')[0])
    end = int(r.split('-')[1])

    for id in range(start, end+1):
        id_str = str(id)
        id_str_len = len(id_str)
        if id_str_len % 2 == 0 and id_str[0:id_str_len//2] == id_str[id_str_len//2:]:
            password += id

print(f"answer: {password}")