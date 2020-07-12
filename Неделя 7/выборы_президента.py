ppl = {}
with open('input.txt', encoding='utf8') as f:
    for prs in f.readlines():
        ppl[prs] = ppl.get(prs, 0) + 1
ans = sorted([(- v, k) for k, v in ppl.items()])
s = sum(ppl.values())
with open('output.txt', 'w', encoding='utf8') as f:
    if ans[0][0] < - s / 2:
        print(ans[0][1], end='', file=f)
    else:
        print(ans[0][1], ans[1][1], sep='', end='', file=f)
