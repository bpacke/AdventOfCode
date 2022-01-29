from re import findall

from numpy import roll, zeros


def read_puzzle_input(filename):
    instructions = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if 'rect' in line: cmd = 'rect'
            elif 'row' in line: cmd = 'row'
            elif 'column' in line: cmd = 'col'
            instructions.append((cmd, *[int(x) for x in findall('\d+', line)]))
    return instructions

def task_one(instructions, screen):
    for cmd, a, b in instructions:
        if cmd == 'rect': screen[:b, :a] = 1
        elif cmd == 'row': screen[a] = roll(screen[a], b)
        elif cmd == 'col': screen[:, a] = roll(screen[:, a], b)
    count = int(sum(screen.flatten()))
    print(f'Task One: {count}')

def display_screen(screen):
    for row in screen:
        for item in row:
            pixel = '⬜️' if item == 1 else '⬛️'
            print(pixel, end='')
        print()

if __name__ == '__main__':
    instructions = read_puzzle_input('2016/data/input/day08.txt')
    screen = zeros((6, 50))
    task_one(instructions, screen)
    display_screen(screen)
