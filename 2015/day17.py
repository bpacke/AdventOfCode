from itertools import combinations

containers = []
eggnog = 150
combs = []
with open('2015/data/input/day17.txt', 'r') as file:
    containers = [int(l.strip()) for l in file]

for i in range(len(containers)):
    for c in list(combinations(containers, i + 1)):
        combs.append(c)

valid = [c for c in combs if sum(c) == eggnog]

print(f'Part One: {len(valid)}')

min_viable_containers = min([len(v) for v in valid])
print(f'Part Two: Minimum conainers = {min_viable_containers}')
minimal_containers = [v for v in valid if len(v) == min_viable_containers]
print(f'Part Two: {len(minimal_containers)}')