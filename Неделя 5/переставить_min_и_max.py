nums = list(map(int, input().split()))
max_index = nums.index(max(nums))
min_index = nums.index(min(nums))
nums[max_index], nums[min_index] = nums[min_index], nums[max_index]
for num in nums:
    print(num, end=' ')
