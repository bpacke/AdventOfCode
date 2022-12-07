import re

task_one = 0
task_two = 0

with open('2022/data/input/day04.txt', 'r') as file:
    for line in file:
        a, b, c, d = [int(x) for x in re.findall('\d+', line)]
        section_1 = set(range(a, b + 1))
        section_2 = set(range(c, d + 1))

        if section_1.issubset(section_2) or section_2.issubset(section_1):
            task_one += 1
        
        if len(section_1.intersection(section_2)) > 0:
            task_two += 1

print(f'Task One: {task_one}')
print(f'Task Two: {task_two}')
