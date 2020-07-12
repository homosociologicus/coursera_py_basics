nums = list(map(int, input().split()))
min_num = 1000
for num in nums:
    if 0 < num < min_num:
        min_num = num
print(min_num)
