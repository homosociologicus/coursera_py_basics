a = int(input())
b = int(input())
c = int(input())
d = int(input())
if c == 0 and d == 0:
    print('NO')
elif a == 0 and b == 0:
    print('INF')
elif a == 0 and b != 0:
    print('NO')
elif a != 0 and (c * (- b / a) + d != 0) and (- b / a).is_integer():
    print(int(- b / a))
else:
    print('NO')
