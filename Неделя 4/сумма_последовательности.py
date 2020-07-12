s = 0


def sumseq():
    n = int(input())
    global s
    s += n
    if n != 0:
        sumseq()


sumseq()
print(s)
