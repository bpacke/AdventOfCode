import re

procedure = []
task_one_stacks = []
task_two_stacks = []

with open('2022/data/input/day05.txt', 'r') as file:
    lines = []
    for line in file:
        if '[' in line:
            lines.insert(0, [line[i] for i in range(1, len(line), 4)])
        elif line.startswith('move'):
            procedure.append([int(r) for r in re.findall('\d+', line)])
    for i in range(0, len(lines[0])):
        task_one_stacks.append([l[i] for l in lines if l[i] != ' '])
        task_two_stacks.append([l[i] for l in lines if l[i] != ' '])

for count, x, y in procedure:
    for _ in range(count):
        task_one_stacks[y-1].append(task_one_stacks[x-1].pop())
    task_two_stacks[y-1] += task_two_stacks[x-1][-count:]
    task_two_stacks[x-1] = task_two_stacks[x-1][:-count]

print(f'Task One: {"".join([s[-1] for s in task_one_stacks])}')
print(f'Task Two: {"".join([s[-1] for s in task_two_stacks])}')