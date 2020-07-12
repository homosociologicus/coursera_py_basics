from math import floor

p = int(input())
x = int(input())
y = int(input())
dep0 = x + 0.01 * y
dep1 = dep0 * (1 + 0.01 * p)
dep1_frac = 100 * (dep1 - floor(dep1))
print(floor(dep1), int((dep1_frac * 100 + 0.5) // 100))
