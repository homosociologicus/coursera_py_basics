w_dict = dict()
with open('input.txt', 'r', encoding='utf8') as f:
    words = list(f.read().split())
for word in words:
    if word in w_dict:
        print(w_dict[word], end=' ')
        w_dict[word] += 1
    else:
        print(0, end=' ')
        w_dict[word] = 1
