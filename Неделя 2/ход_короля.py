s1 = int(input())
s2 = int(input())
f1 = int(input())
f2 = int(input())
if (abs(f1 - s1) + abs(f2 - s2) <= 2 and
        abs(f1 - s1) <= 1 and
        abs(f2 - s2) <= 1):
    print('YES')
else:
    print('NO')
