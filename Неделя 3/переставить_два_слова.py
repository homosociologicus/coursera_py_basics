s = input()
space = s.find(' ')
print(s[space + 1:] + ' ' + s[:space + 1])
