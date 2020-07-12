nums = list(map(int, input().split()))
max_num = nums[0]
index = 0
for i, num in enumerate(nums):
    if num >= max_num:
        index = i
        max_num = num
print(max_num, index)
