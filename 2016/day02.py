def read_puzzle_input(filename):
    instructions = []
    with open(filename) as file:
        for line in file:
            instructions.append(list(line.strip()))
    return instructions

def do_task_1(puzzle_input, task_2=False):
    keypad = [  [1, 2, 3], 
                [4, 5, 6],
                [7, 8, 9]   ]
    start_col = start_row = 1
    key_code = ''
    for directions in puzzle_input:
        for direction in directions:
            if direction == 'U': start_row -= 1
            elif direction == 'D': start_row += 1
            elif direction == 'R': start_col += 1
            elif direction == 'L': start_col -= 1

            if start_row < 0: start_row = 0
            elif start_row > 2: start_row = 2
            if start_col < 0: start_col = 0
            elif start_col > 2: start_col = 2
        key_code += str(keypad[start_row][start_col])
    return key_code

def do_task_2(puzzle_input):
    keypad = [  [' ', ' ', '1', ' ', ' '], 
                [' ', '2', '3', '4', ' '],
                ['5', '6', '7', '8', '9'],
                [' ', 'A', 'B', 'C', ' '],
                [' ', ' ', 'D', ' ', ' ']   ]
    start_col = 0
    start_row = 2
    key_code = ''
    for directions in puzzle_input:
        for direction in directions:
            if direction == 'U' and start_row - 1 >= 0 and keypad[start_row - 1][start_col] != ' ':
                start_row -= 1
            elif direction == 'D' and start_row + 1 < 5 and keypad[start_row + 1][start_col] != ' ':
                start_row += 1
            elif direction == 'R'and start_col + 1 < 5 and keypad[start_row][start_col +  1] != ' ':
                start_col += 1
            elif direction == 'L'and start_col - 1 >= 0 and keypad[start_row][start_col - 1] != ' ':
                start_col -= 1

            if start_row < 0: start_row = 0
            elif start_row > 4: start_row = 4
            if start_col < 0: start_col = 0
            elif start_col > 4: start_col = 4
        key_code += keypad[start_row][start_col]
    return key_code

if __name__ == '__main__':
    steps = read_puzzle_input('2016/data/input/day02.txt')
    print(f'Task One: {do_task_1(steps)}')
    print(f'Task Two: {do_task_2(steps)}')