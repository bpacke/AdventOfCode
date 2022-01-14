from collections import Counter

groups = []

with open('2020/data/input/day06.txt') as file:
    group_answers = []
    for line in file:
        line = line.strip()
        if line != '': group_answers.append(line)
        else:
            group = ''.join(group_answers)
            responses = len(group_answers)
            answers = set(list(group))
            matching_answers = set.intersection(*[set(list(g)) for g in group_answers])
            groups.append((group, responses, len(answers), len(matching_answers)))
            group_answers = []
    group = ''.join(group_answers)
    responses = len(group_answers)
    answers = set(list(group))
    matching_answers = set.intersection(*[set(list(g)) for g in group_answers])
    groups.append((group, responses, len(answers), len(matching_answers)))

task_1 = sum([g[2] for g in groups])
print(f'Task One: {task_1}')

task_2 = sum([g[-1] for g in groups])
print(f'Task One: {task_2}')
