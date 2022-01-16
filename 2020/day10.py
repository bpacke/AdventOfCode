from itertools import combinations

from numpy import append

with open('2020/data/test/day10.txt') as file:
    adapters = [int(line.strip()) for line in file]
    adapters.sort()

jolts = [b - a for a, b in list(zip(adapters, adapters[1:]))]
jolt_1 = [j for j in jolts if j == 1] + [1]
jolt_3 = [j for j in jolts if j == 3] + [3] #for final connection to device

print(f'Task One: {len(jolt_1) * len(jolt_3)}')

combs = []
for i in range(1, len(adapters) + 1):
    print(f'i = {i}')
    for c in combinations(adapters, i):
        combs.append(c)

print(len(combs))

