
from re import findall, match


def read_puzzle_input(filename):
    with open(filename) as file:
        return [line.strip() for line in file]

def task_one(line):
    out_string = ''
    index = 0
    while index < len(line):
        m = match('\(\d+x\d+\)', line[index:])
        if m:
            index += m.end() - 1
            char_count = int(findall('\d+', m.group())[0])
            repeat_count = int(findall('\d+', m.group())[1])
            to_repeat = (line[index + 1 : index + 1 + char_count]) * repeat_count
            out_string += to_repeat
            index += char_count
        else:
            out_string += line[index]
        index += 1
    return out_string

if __name__ == '__main__':
    line = read_puzzle_input('2016/data/input/day09.txt')[0]
    t1 = task_one(line)
    while '(' in t1:
        print(t1.count('('))
        t1 = task_one(t1)
