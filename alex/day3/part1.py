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

    largest = int(str(num[0] + num[1]))

    for i in range(len(num)-1):
        first = num[i]
        second = num[i+1]
        
        for j in range(i+1, len(num)):
            if j <= len(num) and int(str(first + num[j])) > largest:
                largest = int(str(first + num[j]))

    jolt_sum += largest

print(f"answer: {jolt_sum}")
