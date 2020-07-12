with open('input.txt', encoding='utf8') as f:
    txt = sorted(f.read().split())
words = dict()
for word in txt:
    words[word] = words.get(word, 0) + 1
m = max(words.values())
for word, freq in words.items():
    if freq == m:
        print(word)
        break
