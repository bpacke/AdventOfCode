in_data = []
with open('input08.txt', 'r') as file:
    for line in file:
        line_split = line.split('|')
        i = [i for i in [l.strip() for l in line_split[0].split(' ')] if i != '']
        out = [o for o in [l.strip() for l in line_split[1].split(' ')] if o != '']
        in_data.append((i, out))

value_total = 0
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

# count = 0
# for _, o in in_data:
#     for x in o:
#         if len(x) == seg_counts[1] or len(x) == seg_counts[4] or len(x) == seg_counts[7] or len(x) == seg_counts[8]:
#             count = count + 1
# print(f'Count: {count}') 
seg_bits = {0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    }
for _, o in in_data:
    found = []
    for i, x in enumerate(o):
        if len(x) == seg_counts[1]:
            o[i] = 1
            seg_bits[1] = list(x)
            found.append(1)
        elif len(x) == seg_counts[4]:
            o[i] = 4
            seg_bits[4] = list(x)
            found.append(4)
        elif len(x) == seg_counts[7]:
            o[i] = 7
            seg_bits[7] = list(x)
            found.append(7)
        elif len(x) == seg_counts[8]:
            o[i] = 8
            seg_bits[8] = list(x)
            found.append(8)
        elif len(x) == 5: #2/3/5
            # print('elif len(x) == 5: #2/3/5')
            # print(f'len({seg_bits[1]}) != 0   ---   {len(seg_bits[1]) != 0}')
            # print(f'all([y in seg_bits[1] for y in x])   ---   {all([y in seg_bits[1] for y in x])}')
            if len(seg_bits[1]) != 0 and all([y in x for y in seg_bits[1]]): # is a 3
                o[i] = 3
                seg_bits[3] = list(x)
                found.append(3)
            if len([a for a in x if a in seg_bits[4]]) == 3:
                o[i] = 2
                seg_bits[2] = list(x)
                found.append(2)
            else:
                o[i] = 5
                seg_bits[5] = list(x)
                found.append(5)
        elif len(x) == 6: #0/6/9
            if len(seg_bits[1]) != 0 and not all([y in x for y in seg_bits[1]]): # is a 6
                o[i] = 6
                seg_bits[6] = list(x)
                found.append(6)
            elif len(seg_bits[4]) != 0 and not all([y in x for y in seg_bits[4]]): # is a 9
                o[i] = 9
                seg_bits[9] = list(x)
                found.append(9)
            else:
                o[i] = 0
                seg_bits[0] = list(x)
                found.append(0)

    print(o)
    value_total = value_total + int(''.join([str(z) for z in o]))
    seg_bits = {0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    }
    print('-' * 30)

print(f'value_total: {value_total}')
