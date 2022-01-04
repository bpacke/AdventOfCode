data_mini = [((8,0), (0,8)),
((6,4), (2,0)),
((0,0), (8,8)),
((5,5), (8,2))]
data_hand = [((1,4), (3,6)),
((4,9), (7,6)),
((7,3), (4,0)),
((10,2), (7,5))]

data = data_hand

for c1, c2 in data:
    # c1[0] = x1
    # c1[1] = y1
    # c2[0] = x2
    # c2[1] = y2
    if c1[0] < c2[0]:
        s_range = range(c1[0], c2[0] + 1)
    elif c1[0] > c2[0]:
        s_range = reversed(range(c2[0], c1[0] + 1))

    if c1[1] < c2[1]:
        e_range = range(c1[1], c2[1] + 1)
    elif c1[1] > c2[1]:
        e_range = reversed(range(c2[1], c1[1] + 1))
    print(f'{c1} --- {list(zip(s_range, e_range))} --- {c2}')

