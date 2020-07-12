nums = list(map(int, input().split()))
l = len(nums)
if l % 2 == 0:
    for i, num in enumerate(nums):
        if i % 2 == 0:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
else:
    for i, num in enumerate(nums[:l - 1]):
        if i % 2 == 0:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
for num in nums:
    print(num, end=' ')
