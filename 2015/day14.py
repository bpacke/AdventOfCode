class Reindeer():
    name = None
    speed = None
    duration = None
    rest = None
    splits = None

    def __init__(self, n, s, d, r, c):
        self.name = n
        self.speed = s
        self.duration = d
        self.rest = r
        self.splits = c

reindeer = []
race_time = 2503

with open('2015/data/input/day14.txt') as file:
    for line in file:
        l = line.split(' ')
        name = l[0]
        speed = int(l[3])
        duration = int(l[6])
        rest = int(l[13])
        cycle = ([speed] * duration) + ([0] * rest)
        reindeer.append(Reindeer(name, speed, duration, rest, cycle))

race_splits = []

for r in reindeer:
    print(f'{r.name} running')
    splits = []
    time = 0
    for seconds in range(race_time):
        splits.append(r.splits[seconds % len(r.splits)])
    # print(splits)
    race_splits.append((r.name, sum(splits), splits))

task1_splits = sorted(race_splits, key=lambda r: r[1], reverse=True)
task_1_winner, task_1_distance, _ = task1_splits[0]
print(f'Task One -> Winner: {task_1_winner} - {task_1_distance} km')

race_cummulative = []

for n, rs in [(n, s) for n, _, s in race_splits]:
    cumm = []
    for i in range(1, len(rs)):
        cumm.append(sum(rs[:i]))
    race_cummulative.append((n, cumm))

task_2_scores = {}
for r in [r.name for r in reindeer]:
    task_2_scores[r] = 0

for i in range(race_time - 1):
    leaders = [name for name, splits in race_cummulative if splits[i] == max([s[i] for _, s in race_cummulative])]
    for l in leaders:
        task_2_scores[l] += 1

print(task_2_scores)