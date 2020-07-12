n = int(input())
nums = list(map(int, input().split()))
x = int(input())
min_abs = 2001
num_current = nums[0]
for num in nums:
    if abs(x - num) <= min_abs:
        min_abs = abs(x - num)
        num_current = num
print(num_current)
