from collections import Counter

directions = []
santa_x_coordinate = 0
santa_y_coordinate = 0

robo_x_coordinate = 0
robo_y_coordinate = 0

total_houses_visited = []

with open('2015/data/input/day03.txt', 'r') as file:
    for line in file:
        for l in line.strip():
            directions.append(l)

total_houses_visited.append((santa_x_coordinate, santa_y_coordinate))
total_houses_visited.append((robo_x_coordinate, robo_y_coordinate))
for i, d in enumerate(directions):
    if i % 2 == 0:
        if d == '^' : santa_y_coordinate = santa_y_coordinate + 1
        elif d == 'v' : santa_y_coordinate = santa_y_coordinate - 1
        elif d == '>' : santa_x_coordinate = santa_x_coordinate + 1
        elif d == '<' : santa_x_coordinate = santa_x_coordinate - 1
        total_houses_visited.append((santa_x_coordinate, santa_y_coordinate))
    else:
        if d == '^' : robo_y_coordinate = robo_y_coordinate + 1
        elif d == 'v' : robo_y_coordinate = robo_y_coordinate - 1
        elif d == '>' : robo_x_coordinate = robo_x_coordinate + 1
        elif d == '<' : robo_x_coordinate = robo_x_coordinate - 1
        total_houses_visited.append((robo_x_coordinate, robo_y_coordinate))
counter = Counter(total_houses_visited)
print(f'{len(counter)} get at least one present')