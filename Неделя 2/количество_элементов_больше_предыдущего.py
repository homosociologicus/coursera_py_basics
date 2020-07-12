n = int(input())
q = 0
while n != 0:
    new = int(input())
    if new > n:
        q += 1
    n = new
print(q)
