import sys
path = str(sys.argv[1])
len_nums = 0
sum_nums = 0
with open(path, 'r') as file:
    nums = [row.strip() for row in file]
nums = list(map(int, nums))
len_nums = len(nums)

for i in range(len_nums):
    sum_nums = sum_nums + nums[i]

result = round(sum_nums/len_nums)
count = 0
for id, i in enumerate(nums):
    while i != result:
        if i < result:
            i += 1
            count += 1
        elif i > result:
             i -= 1
             count += 1
        else:
            nums[id] = i
print(count)