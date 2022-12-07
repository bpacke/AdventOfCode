with open('2022/data/input/day06.txt', 'r') as file:
    input = file.readline().strip()

def do_task(distinct_characters):
    for i in range(0, len(input)):
        if len(set(input[i:i + distinct_characters])) == distinct_characters:
            return i + distinct_characters

print(f'Task One: {do_task(4)}')
print(f'Task Two: {do_task(14)}')