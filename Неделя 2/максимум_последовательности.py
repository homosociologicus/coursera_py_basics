num = int(input())
curmax = num
while num != 0:
    if curmax < num:
        curmax = num
    num = int(input())
print(curmax)
