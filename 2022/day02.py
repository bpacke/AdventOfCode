opponent_shapes = ['A', 'B', 'C']
players_shapes = ['X', 'Y', 'Z']
game_possibilites = []

# generate all possible games, results and scores
for o_index, o in enumerate(opponent_shapes):
    for p_index, p in enumerate(players_shapes):
        if o_index == p_index:
            game_possibilites.append([o, p, 'Y', p_index + 1 + 3])
        elif o == 'A' and p == 'Y' or \
             o == 'B' and p == 'Z' or \
             o == 'C' and p == 'X':
             game_possibilites.append([o, p, 'Z', p_index + 1 + 6])
        else:
            game_possibilites.append([o, p, 'X', p_index + 1 + 0])

matches = []

with open('2022/data/input/day02.txt', 'r') as file:
    for line in file:
        matches.append([line[0], line[2]])

task_one_score = 0
task_two_score = 0
for m in matches:
    task_one_score += [gp[-1] for gp in game_possibilites if gp[:2] == m][0]
    task_two_score += [gp[-1] for gp in game_possibilites if [gp[0], gp[2]] == m][0]

print(f'Task One: {task_one_score}')
print(f'Task Two: {task_two_score}')
        
 