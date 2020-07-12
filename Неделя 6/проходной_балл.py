appl = []
with open('input.txt', 'r', encoding='utf8') as inp:
    k = int(inp.readline())
    for line in inp:
        data = line.split()
        if ((int(data[-1]) >= 40 and
             int(data[-2]) >= 40 and
             int(data[-3]) >= 40)):
            appl.append(sum(map(int, data[-3:])))
if len(appl) <= k:
    print(0)
else:
    appl.sort(reverse=True)
    got = appl.count(appl[0])
    if got > k:
        print(1)
    else:
        while got + appl.count(appl[got]) <= k:
            got += appl.count(appl[got])
        print(appl[got - 1])
