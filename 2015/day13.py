from itertools import permutations

task_1 = False
input_file = '2015/data/input/day13.txt' if task_1 else '2015/data/input/day13me.txt'

seating_plans = []
attendees = set()
pairings = {}

with open(input_file, 'r') as file:
    for line in file:
        l = line.strip().split(' ')
        attendees.add(l[0])
        pair = (l[0], l[-1][:-1])
        score = int(l[3]) if l[2] == 'gain' else -int(l[3])
        pairings[pair] = score

seating_plans = [list(p) for p in permutations(attendees, len(attendees))]
seating_plans_and_scores = []
for s in seating_plans:
    plan = list(zip(s, s[1:] + [s[0]]))
    score = 0
    for p1, p2 in plan:
        score += pairings[(p1, p2)] + pairings[(p2, p1)]
    seating_plans_and_scores.append((s, score))

seating_plans_and_scores.sort(key=lambda s: s[-1], reverse=True)
max_score = max([s for _, s in seating_plans_and_scores])
best_seating_plans = [p for p, s in seating_plans_and_scores if s == max_score]
print(f'Best score: {max_score}\nThere are {len(best_seating_plans)} plans with that score.')