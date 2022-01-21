

x_travelled = 0
y_travelled = 0
directions = ['N', 'E', 'S', 'W']
current_direction = 'N'

instructions = []

with open('2016/data/input/day01.txt') as file:
    for line in file:
        instructions += line.strip().split(', ')

for i in instructions:
    travel_direction = i[0]
    travel_distance = int(i[1:])
    if travel_direction == 'R': current_direction = directions [(directions.index(current_direction) + 1) % len(directions)]
    elif travel_direction == 'L': current_direction = directions [(directions.index(current_direction) - 1) % len(directions)]

    if current_direction == 'N': y_travelled += travel_distance
    elif current_direction == 'S': y_travelled -= travel_distance
    elif current_direction == 'E': x_travelled += travel_distance
    elif current_direction == 'W': x_travelled -= travel_distance

total_distance = abs(x_travelled) + abs(y_travelled)
print(f'Task One: {total_distance}')


x_travelled = 0
y_travelled = 0
current_direction = 'N'
visited_locations = [(0, 0)]
double_visit = (0, 0)

found = False
index = 0
while found == False and index < len(instructions):
    i = instructions[index]
    travel_direction = i[0]
    travel_distance = int(i[1:])
    if travel_direction == 'R': current_direction = directions [(directions.index(current_direction) + 1) % len(directions)]
    elif travel_direction == 'L': current_direction = directions [(directions.index(current_direction) - 1) % len(directions)]

    if current_direction == 'N':
        for _ in range(travel_distance):
            y_travelled += 1
            coords = (y_travelled, x_travelled)
            if coords not in visited_locations: visited_locations.append(coords)
            else:
                double_visit = coords
                found = True
                break

    elif current_direction == 'S':
        for _ in range(travel_distance): 
            y_travelled -= 1
            coords = (y_travelled, x_travelled)
            if coords not in visited_locations: visited_locations.append(coords)
            else:
                double_visit = coords
                found = True
                break

    elif current_direction == 'E':
        for _ in range(travel_distance):
            x_travelled += 1
            coords = (y_travelled, x_travelled)
            if coords not in visited_locations: visited_locations.append(coords)
            else:
                double_visit = coords
                found = True
                break

    elif current_direction == 'W':
        for _ in range(travel_distance):
            x_travelled -= 1
            coords = (y_travelled, x_travelled)
            if coords not in visited_locations: visited_locations.append(coords)
            else:
                double_visit = coords
                found = True
                break

    index += 1

print(f'Task Two: {abs(double_visit[0])  + abs(double_visit[1])}')