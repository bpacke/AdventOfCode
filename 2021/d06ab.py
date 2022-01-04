import time
init_state = [5,1,1,5,4,2,1,2,1,2,2,1,1,1,4,2,2,4,1,1,1,1,1,4,1,1,1,1,1,5,3,1,4,1,1,1,1,1,4,1,5,1,1,1,4,1,2,2,3,1,5,1,1,5,1,1,5,4,1,1,1,4,3,1,1,1,3,1,5,5,1,1,1,1,5,3,2,1,2,3,1,5,1,1,4,1,1,2,1,5,1,1,1,1,5,4,5,1,3,1,3,3,5,5,1,3,1,5,3,1,1,4,2,3,3,1,2,4,1,1,1,1,1,1,1,2,1,1,4,1,3,2,5,2,1,1,1,4,2,1,1,1,4,2,4,1,1,1,1,4,1,3,5,5,1,2,1,3,1,1,4,1,1,1,1,2,1,1,4,2,3,1,1,1,1,1,1,1,4,5,1,1,3,1,1,2,1,1,1,5,1,1,1,1,1,3,2,1,2,4,5,1,5,4,1,1,3,1,1,5,5,1,3,1,1,1,1,4,4,2,1,2,1,1,5,1,1,4,5,1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,4,2,1,1,1,2,5,1,4,1,1,1,4,1,1,5,4,4,3,1,1,4,5,1,1,3,5,3,1,2,5,3,4,1,3,5,4,1,3,1,5,1,4,1,1,4,2,1,1,1,3,2,1,1,4]
#init_state = [3,4,3,1,2]

from collections import Counter
tz = []
for _ in range(100):
    l_fish = Counter(init_state)
    print('-' * 25)
    print(f'Day 0: {sorted(l_fish.items())}')
    print(sum(l_fish.values()))
    start = time.time()
    for day in range(1,257):
        for x in range(-1, 9):
            l_fish[x] = l_fish[x + 1]

        l_fish[8] = l_fish [8]+ l_fish[-1]
        l_fish[6] = l_fish[6] + l_fish[-1]
        l_fish[-1] = 0
        # print(f'Day {day}: {sorted(l_fish.items())}')
        # print(sum(l_fish.values()))
        # print('-' * 25)
    end = time.time()
    print(f'Fish: {sum(l_fish.values())}')
    tz.append(end-start)

print(f'Average time: {sum(tz)/len(tz)}')
