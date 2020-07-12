f0 = 0
f1 = 1
fn = 1
i = 1
A = int(input())
while fn <= A:
    if fn == A:
        print(i)
        break
    fn = f1 + f0
    f0 = f1
    f1 = fn
    i += 1
if A != fn:
    print(-1)
