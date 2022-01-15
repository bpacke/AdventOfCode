from itertools import combinations

preamble = 25
back_range = 25

with open('2020/data/input/day09.txt') as file:
    sequence = [int(line.strip()) for line in file]

for index, value in enumerate(sequence):
    if index < preamble: continue
    back_range_sums = [a + b for a, b in combinations(sequence[index - preamble: index], 2)]
    if value not in back_range_sums:
        print(f'Task One: {value}')
        break

sequence = sequence[:index]

for group_size in range(2, len(sequence)):
    for i in range(0, len(sequence) - group_size + 1):
        group = sequence[i: i + group_size]
        if sum(group) == value:
            print(f'Task Two: {min(group) + max(group)}')
            break