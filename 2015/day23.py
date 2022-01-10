task_2 = True
registers = {'a': 0, 'b': 0}
if task_2: registers['a'] = 1
steps = []

with open('2015/data/input/day23.txt') as file:
    for line in file:
        line = line.strip()
        if line[0] != 'j': #not a jump step
            command = line.split(' ')[0]
            register = line.split(' ')[1]
            steps.append((command, register))
        elif line[:3] == 'jmp':
            command = line.split(' ')[0]
            offset = int(line.split(' ')[1])
            steps.append((command, offset))
        elif line[:2] == 'ji':
            command = line.split(' ')[0]
            register = line.split(' ')[1][:-1]
            offset = int(line.split(' ')[2])
            steps.append((command, register, offset))
            
i = 0
while True:
    if i < 0 or i >= len(steps): break
    s = steps[i]
    if s[0] == 'hlf':
        registers[s[1]] //= 2
        i += 1
    elif s[0] == 'tpl':
        registers[s[1]] *= 3
        i += 1
    elif s[0] == 'inc':
        registers[s[1]] += 1
        i += 1
    elif s[0] == 'jmp':
        i += s[1]
    elif s[0] == 'jie':
        if registers[s[1]] % 2 == 0:
            i += s[2]
        else: i += 1
    elif s[0] == 'jio':
        if registers[s[1]] == 1:
            i += s[2]
        else: i += 1 

ans = registers['b']
print(f'Answer: {ans}')
