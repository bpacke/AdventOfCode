from itertools import combinations

with open('2020/data/input/day01.txt') as file:
    report = [int(line) for line in file.readlines()]

combs = combinations(report, 2)
pair = [(a, b) for a, b in combs if a + b == 2020][0]
print(f'Task One: {pair[0] * pair[1]}')

combs = combinations(report, 3)
pair = [(a, b, c) for a, b, c in combs if a + b + c == 2020][0]
print(f'Task Two: {pair[0] * pair[1] * pair[2]}')
