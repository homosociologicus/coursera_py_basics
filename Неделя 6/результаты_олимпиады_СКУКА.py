N = int(input())
man_list = []
for _ in range(N):
    man_list.append(input().split())
man_list.sort(key=lambda i: i[1], reverse=True)
for _ in man_list:
    print(_[0])
