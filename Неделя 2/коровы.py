n = int(input())
if n != 11 and n % 10 == 1:
    print(str(n) + ' korova')
elif 10 <= n <= 14 or 5 <= n % 10 <= 9 or n % 10 == 0:
    print(str(n) + ' korov')
else:
    print(str(n) + ' korovy')
