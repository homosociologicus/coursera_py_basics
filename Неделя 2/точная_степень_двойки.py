N = int(input())
i = 1
while i <= N:
    if i == N:
        print('YES')
        break
    elif i * 2 > N:
        print('NO')
        break
    else:
        i *= 2
