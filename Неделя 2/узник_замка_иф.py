a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
if max(a, b, c) == a:
    x, y = b, c
elif max(a, b, c) == b:
    x, y = a, c
else:
    x, y = a, b
if max(x, y) <= max(d, e) and min(x, y) <= min(d, e):
    print('YES')
else:
    print('NO')
