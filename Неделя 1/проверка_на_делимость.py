A = int(input())
B = int(input())
print('YES' * 0 ** (A % B) + 'NO' * (abs(0 ** (A % B) - 1)))
