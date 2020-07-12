num = int(input())
q = 0
num_max = 0
while num != 0:
    if num == num_max:
        q += 1
    elif num > num_max:
        num_max = num
        q = 1
    num = int(input())
print(q)
