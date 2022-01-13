from collections import Counter
from re import findall

task_1_passwords = []
task_2_passwords = []

with open('2020/data/input/day02.txt') as file:
    for line in file:
        line = line.strip()
        password = line.split(': ')[-1]
        rule_line = line.split(': ')[0]
        min_max = findall('\d+', rule_line)
        min_count = int(min_max[0])
        max_count = int(min_max[1])
        rule_char = rule_line[-1]
        char_count = Counter(password)[rule_char]
        if min_count <= char_count and char_count <= max_count:
            task_1_passwords.append(password)
        if (password[min_count - 1] == rule_char) != (password[max_count - 1] == rule_char):
            task_2_passwords.append(password)

print(f'Task One: {len(task_1_passwords)}')
print(f'Task Two: {len(task_2_passwords)}')

