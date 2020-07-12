n = int(input())
q = 0
sumall = 0
while n != 0:
    q += 1
    sumall += n
    n = int(input())
print(sumall / q)
