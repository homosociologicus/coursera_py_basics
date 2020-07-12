fn_1 = 0
fn = 1
n = int(input())
i = 1
while i < n:
    fn1 = fn_1 + fn
    fn_1 = fn
    fn = fn1
    i += 1
print(fn)
