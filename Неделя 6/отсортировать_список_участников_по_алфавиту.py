parts = []
with open('input.txt', 'r', encoding='utf8') as in_file:
    for line in in_file:
        words = line.split()
        parts.append(' '.join([words[0], words[1], words[3]]))
with open('output.txt', 'w', encoding='utf8') as out_file:
    for line in sorted(parts):
        print(line, file=out_file)
