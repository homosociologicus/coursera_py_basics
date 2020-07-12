s = input()
first = s.find('h')
last = len(s) - 1 - s[::-1].find('h')
print(s[:first], s[last + 1:], sep='')
