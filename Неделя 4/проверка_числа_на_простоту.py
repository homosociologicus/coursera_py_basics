from math import sqrt, floor


def IsPrime(n):
    if n == 2:
        return True
    i = 1
    while i <= sqrt(n):
        i += 1
        if n % i == 0:
            return False
        elif i >= floor(sqrt(n)):
            return True


n = int(input())
if IsPrime(n):
    print('YES')
else:
    print('NO')
