from re import findall, match


def read_puzzle_input(filename):
    with open(filename) as file:
        return [line.strip() for line in file][0]

def do_task(line, task_two):
    out_count = 0
    index = 0
    while index < len(line):
        marker = match('\(\d+x\d+\)', line[index:])
        if marker:
            index += marker.end() - 1
            char_count = int(findall('\d+', marker.group())[0])
            repeat_count = int(findall('\d+', marker.group())[1])
            if task_two:
                to_repeat =  do_task(line[index + 1 : index + 1 + char_count], True) * repeat_count
            else:
                to_repeat = char_count * repeat_count
            out_count += to_repeat
            index += char_count
        else:
            out_count += 1
        index += 1
    return out_count

if __name__ == '__main__':
    line = read_puzzle_input('2016/data/input/day09.txt')
    task_one = do_task(line, False)
    print(task_one)
    task_two = do_task(line, True)
    print(task_two)
