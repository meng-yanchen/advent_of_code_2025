input = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111"
]
with open('input.txt', 'r') as file:
    input = file.read()
input = input.split('\n')

jolt_sum = 0

for num in input:
    num_str = num

    while len(num_str) > 12:
        digit_removed = False

        for i in range(len(num_str)-1):
            if num_str[i] < num_str[i+1]:
                num_str = num_str[0:i] + num_str[i+1:len(num_str)]
                digit_removed = True
                break

        if not digit_removed:
            index_to_cut = len(num_str) - 1
            num_str = num_str[0:index_to_cut]

    largest_sub = int(str(num_str))
    jolt_sum += largest_sub

print(f"answer: {jolt_sum}")
