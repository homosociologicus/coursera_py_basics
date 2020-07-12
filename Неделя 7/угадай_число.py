whole = set(range(1, 1 + int(input())))
line1 = input()
while line1 != 'HELP':
    line2 = input()
    if line2 == 'NO':
        whole -= set(map(int, line1.split()))
    else:
        whole &= set(map(int, line1.split()))
    line1 = input()
print(*sorted(list(whole)))
