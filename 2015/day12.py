import re

with open('2015/data/input/day12.txt', 'r') as file:
    lines = [l.strip() for l in file]

total = 0


for l in lines:
    for i in [int(r) for r in re.findall('-?\d+', l)]:
        print(i)
        total += i

print(total)