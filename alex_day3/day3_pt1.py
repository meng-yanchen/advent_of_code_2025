nums = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111"
]

jolt_sum = 0

with open('input.txt', 'r') as file:
    nums = file.read()

nums = nums.split('\n')

for num in nums:

    # print(num, len(num))

    largest = int(str(num[0] + num[1]))

    for i in range(len(num)-1):
        first = num[i]
        second = num[i+1]
        
        # print(first, second, largest, i)

        for j in range(i+1, len(num)):
            if j <= len(num) and int(str(first + num[j])) > largest:
                largest = int(str(first + num[j]))

        # print(f"largest: {largest}")

    jolt_sum += largest

print(jolt_sum)

