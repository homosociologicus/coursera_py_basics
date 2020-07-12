num = int(input())
length_current = 0
num_current = num
length_max = 0
while num != 0:
    if num == num_current:
        length_current += 1
        if length_current > length_max:
            length_max = length_current
    else:
        if length_current > length_max:
            length_max = length_current
        num_current = num
        length_current = 1
    num = int(input())
print(length_max)
