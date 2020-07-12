disk, users = tuple(map(int, input().split()))
files = []
for _ in range(users):
    files.append(int(input()))
size = 0
answ = 0
for file in sorted(files):
    if size + file <= disk:
        size += file
        answ += 1
    else:
        break
print(answ)
