a = int(input())
first = a // 1000
second = a // 100 % 10
third = a // 10 % 10
fourth = a % 10
reverse = 1000 * fourth + 100 * third + 10 * second + first
print((a + 1) // (reverse + 1) + (a + 1) % (reverse + 1))
