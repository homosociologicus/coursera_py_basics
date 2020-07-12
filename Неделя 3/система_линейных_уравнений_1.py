# ax + by = e; cx + dy = f

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if a != 0:
    y = (f - c * e / a) / (d - b * c / a)
    print((e - b * y) / a, y)
else:
    print((f - d * e / b) / c, e / b)
