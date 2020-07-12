N = int(input())
i = 1
power = 0
while i <= N * 2:
    if i >= N:
        print(power)
        break
    else:
        i *= 2
        power += 1
