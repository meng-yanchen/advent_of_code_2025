jolt_sum = 0
nums = [
    "987654321111111", # 987654321111 987543211111
    "811111111111119", # 811111111119 811111111119
    "234234234234278", # 434234234278 434234234278
    "818181911112111"  # 888911112111 888911112111
]
with open('input.txt', 'r') as file:
    nums = file.read()
nums = nums.split('\n')

for num in nums:
    num_str = num

    while len(num_str) > 12:
        digit_removed = False

        # print(f"finding first digit not in decending order: {num_str}")
        for i in range(len(num_str)-1):
            if num_str[i] < num_str[i+1]:
                # print(f"cutting index: {i} value: {num_str[i]}")
                num_str = num_str[0:i] + num_str[i+1:len(num_str)]
                digit_removed = True
                break

        if not digit_removed:
            index_to_cut = len(num_str) - 1
            num_str = num_str[0:index_to_cut]

    largest_sub = int(str(num_str))
    jolt_sum += largest_sub
    # print(f"num: {num}, largest12: {largest_sub}")

# print("test actual = 3121910778619")
print(f"jolt_sum: {jolt_sum}")

