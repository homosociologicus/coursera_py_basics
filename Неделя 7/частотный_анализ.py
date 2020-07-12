def frequency(tup):
    return (- tup[0], tup[1])

with open('input.txt', encoding='utf8') as f:
    txt = f.read().split()
words = dict()
for word in txt:
    words[word] = words.get(word, 0) + 1
ans = []
for word, freq in words.items():
    ans.append((freq, word))
ans.sort(key=frequency)
for a in ans:
    print(a[1])
