nums = list(map(int, input().split()))
q = 0
for num in nums:
    if num > 0:
        q += 1
print(q)
