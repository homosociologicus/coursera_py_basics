def ReduceFraction(n, m):
    i = 2
    while i <= min(n, m):
        if n % i == 0 and m % i == 0:
            n = n / i
            m = m / i
        else:
            i += 1
    return int(n), int(m)


n = int(input())
m = int(input())
print(*ReduceFraction(n, m))
