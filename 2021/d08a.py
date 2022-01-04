in_data = []
with open('input08.txt', 'r') as file:
    for line in file:
        line_split = line.split('|')
        i = [i for i in [l.strip() for l in line_split[0].split(' ')] if i != '']
        out = [o for o in [l.strip() for l in line_split[1].split(' ')] if o != '']
        in_data.append((i, out))

seg_counts = {0: 6,
1: 2,
2: 5,
3: 5,
4: 4,
5: 5,
6: 6,
7: 3,
8: 7,
9: 6,
}

count = 0
for _, o in in_data:
    for x in o:
        if len(x) == seg_counts[1] or len(x) == seg_counts[4] or len(x) == seg_counts[7] or len(x) == seg_counts[8]:
            count = count + 1
print(f'Count: {count}') 