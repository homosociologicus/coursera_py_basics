s = input()
first = s.find('f')
last = s[::-1].find('f')
if first != -1 and first == len(s) - 1 - last:
    print(first)
elif first != -1:
    print(first, len(s) - 1 - last)
