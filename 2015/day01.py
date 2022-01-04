instructions = []
floor = 0
basement_instruction = []

with open('2015/data/input/day01.txt', 'r') as file:
    for line in file:
        for l in line.strip():
            instructions.append(l)

for x, i in enumerate(instructions):
    if i == '(':  floor = floor + 1
    elif i == ')': floor = floor - 1

    if floor < 0: basement_instruction.append(x)
    print()

print(f'Floor: {floor}')
print(f'First basement call: {basement_instruction[0] + 1}')