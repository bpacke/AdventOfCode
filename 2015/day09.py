from itertools import permutations

places = set()
places_a_to_b = []
routes_with_distance = []
with open('2015/data/input/day09.txt', 'r') as file:
    for line in file:
        line = line.strip().split(' ')
        s = line[0]
        e = line[2]
        d = int(line[4])
        places_a_to_b.append((s, e, d))
        places_a_to_b.append((e, s, d))
    places = set([a for a, _, _ in places_a_to_b])

routes = permutations(places)
for r in routes:
    hops = zip(r, r[1:])
    total_distance = 0
    for h in hops:
        distance = [d for s, e, d, in places_a_to_b if (s, e) == h][0]
        total_distance = total_distance + distance
    routes_with_distance.append((r, total_distance))

# routes_with_distance = routes_with_distance.sort(key=lambda r: r[-1])
routes_with_distance = sorted(routes_with_distance, key=lambda r: r[-1])
shortest_distance = routes_with_distance[0][-1]
longest_distance = routes_with_distance[-1][-1]
print(f'The shortest distance is: {shortest_distance}')
print(f'The longest distance is: {longest_distance}')