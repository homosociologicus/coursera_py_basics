A = int(input())
l1 = '+___ '
l3 = '|__\\ '
l4 = '|    '
print(A * l1)
for i in range(1, A + 1):
    print('|' + str(i) + ' /', end=' ')
print()
print(A * l3)
print(A * l4)
