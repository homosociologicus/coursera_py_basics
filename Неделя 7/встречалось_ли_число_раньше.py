ans = set()
inp = list(map(int, input().split()))
for i in inp:
    if i in ans:
        print('YES')
    else:
        print('NO')
    ans.add(i)
