def CountSort(A):
    count_a = [0] * 101
    for a in A:
        count_a[a] += 1
    for a in range(101):
        print((str(a) + ' ') * count_a[a], end='')
A = list(map(int, input().split()))
CountSort(A)
