alu = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
model = 99429795993929
# steps = ['inp x', 'mul x -1']
# steps = ['inp z', 'inp x', 'mul z 3', 'eql z x']
incomplete_steps = []

with open('2021/input24.txt') as file:
    steps = [l.strip() for l in file]

for s in steps:
    inp_count = 0
    s = (s[:3], s[4:])
    print(s)
    if ' ' in s[-1]:
        s = (s[0], s[1].split(' ')[0], s[1].split(' ')[1])
    print(s)
    if s[0] == 'inp':
        alu[s[-1]] = int(str(model)[inp_count])
        inp_count += 1

    elif s[0] == 'add':
        try:
            b = int(s[-1])
        except ValueError:
            b = alu[s[-1]]
        alu[s[1]] += b

    elif s[0] == 'mul':
        try:
            b = int(s[-1])
        except ValueError:
            b = alu[s[-1]]
        alu[s[1]] *= b

    elif s[0] == 'div':
        try:
            b = int(s[-1])
        except ValueError:
            b = alu[s[-1]]
        val = int(alu[s[1]] / b)
        alu[s[1]] = val

    elif s[0] == 'mod':
        try:
            b = int(s[-1])
        except ValueError:
            b = alu[s[-1]]
        val = alu[s[1]] % b
        alu[s[1]] = val

    elif s[0] == 'eql':
        try:
            b = int(s[-1])
        except ValueError:
            b = alu[s[-1]]
        alu[s[1]] = 1 if alu[s[1]] == b else 0


    print(f'{alu}\n')
