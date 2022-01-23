from collections import Counter

def read_puzzle_input(filename):
    with open(filename) as file:
        return [line.strip() for line in file]

def do_task(puzzle_input, task_two=False):
    columns = [[line[index] for line in puzzle_input] for index in range(len(puzzle_input[0]))]
    message = ''
    for c in columns:
        character_counter = Counter(c)
        if task_two: character, _ = character_counter.most_common(len(c))[-1]
        else: character, _ = character_counter.most_common(1)[0]
        message += character
    print(f'Task One: {message}')

if __name__ == '__main__':
    puzzle_input = read_puzzle_input('2016/data/input/day06.txt')
    do_task(puzzle_input)
    do_task(puzzle_input, task_two=True)