# let us cheat over and over again
box1 = [int(input()), int(input()), int(input())]
box2 = [int(input()), int(input()), int(input())]
a1, b1, c1 = sorted(box1)
a2, b2, c2 = sorted(box2)
if a1 == a2 and b1 == b2 and c1 == c2:
    print('Boxes are equal')
elif a1 >= a2 and b1 >= b2 and c1 >= c2:
    print('The first box is larger than the second one')
elif a1 <= a2 and b1 <= b2 and c1 <= c2:
    print('The first box is smaller than the second one')
else:
    print('Boxes are incomparable')
