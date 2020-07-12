from math import sqrt, floor


def MinDivisor(n):
    '''Finds minimal divisor of n.'''
    i = 1
    while i <= sqrt(n):
        i += 1
        if n % i == 0:
            return i
        elif i >= floor(sqrt(n)):
            return n


n = float(input())
print(int(MinDivisor(n)))
