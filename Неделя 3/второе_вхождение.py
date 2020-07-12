s = input()
first = s.find('f')
second = s[first + 1:].find('f')
if first == -1:
    print(-2)
elif second == -1:
    print(-1)
else:
    print(first + 1 + second)
