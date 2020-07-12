h = int(input())
houses = list(map(int, input().split()))
s = int(input())
shelters = list(map(int, input().split()))
h_tup = [(x, w) for w, x in enumerate(houses)]
s_tup = [(y, q) for q, y in enumerate(shelters)]
h_tup.sort()
s_tup.sort()
i, j = 0, 0
answer = [None] * h
while i <= h - 1 and j <= s:
    if (j == s - 1 or (abs(h_tup[i][0] - s_tup[j][0]) <=
                       abs(h_tup[i][0] - s_tup[j + 1][0]))):
        answer[h_tup[i][1]] = s_tup[j][1] + 1
        i += 1
    else:
        j += 1
print(' '.join(map(str, answer)))
