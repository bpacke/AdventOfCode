with open('2022/data/input/day06.txt', 'r') as file:
    input = file.readline().strip()

task_one = 0
task_two = 0
for i in range(0, len(input)):
    if task_one == 0 and len(set(input[i:i+4])) == 4:
        task_one = i + 4
    if task_two == 0 and len(set(input[i:i+14])) == 14:
        task_two = i + 14

print(f'Task One: {task_one}')
print(f'Task Two: {task_two}')