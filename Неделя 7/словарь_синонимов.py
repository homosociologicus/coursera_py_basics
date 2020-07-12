n = int(input())
w_dict = dict()
for _ in range(n):
    line = list(input().split())
    w_dict[line[0]] = line[1]
search = input()
for key, value in w_dict.items():
    if key == search:
        print(value)
    elif value == search:
        print(key)
