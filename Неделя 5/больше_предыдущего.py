nums = list(map(int, input().split()))
for i, num in enumerate(nums):
    if i > 0 and num > nums[i - 1]:
        print(num, end=' ')
