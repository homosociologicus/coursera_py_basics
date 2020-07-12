all_lang = set()
all_know = set()
n = int(input())
mi = int(input())
for _ in range(mi):
    lang = input()
    all_lang.add(lang)
    all_know.add(lang)
if n > 1:
    for stud in range(n - 1):
        mi = int(input())
        seti = set()
        for _ in range(mi):
            seti.add(input())
        all_lang |= seti
        all_know &= seti
print(len(all_know), *all_know, len(all_lang), *all_lang, sep='\n')
