steps = []
visited = []
jmpnop = []
accumulator = 0

with open('2020/data/input/day08.txt') as file:
    for i, line in enumerate(file):
        line = line.strip()
        cmd = line.split(' ')[0]
        if cmd == 'jmp' or cmd == 'nop': jmpnop.append(i)
        value = int(line.split(' ')[1])
        steps.append((cmd, value))

index = 0
while True:
    if index < 0 or index >= len(steps): break
    if index in visited: break

    visited.append(index)

    cmd, value = steps[index]
    if cmd == 'acc':
        accumulator += value
        index += 1
    elif cmd == 'jmp':
        index += value
    elif cmd == 'nop':
        index += 1
print(f'Task One: {accumulator}')

for swap in jmpnop:
    accumulator = 0
    index = 0
    visited = []
    infinite_loop = False
    while True:
        if index < 0 or index >= len(steps): break
        if index in visited:
            infinite_loop = True
            break

        visited.append(index)

        cmd, value = steps[index]
        if index == swap:
            if cmd == 'jmp': cmd = 'nop'
            else: cmd = 'jmp'

        if cmd == 'acc':
            accumulator += value
            index += 1
        elif cmd == 'jmp':
            index += value
        elif cmd == 'nop':
            index += 1
            
    if not infinite_loop:
        print(f'Task Two: {accumulator}')
        break