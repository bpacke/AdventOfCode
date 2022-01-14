forrest = []

with open('2020/data/input/day03.txt') as file:
    forrest = [line.strip() for line in file]

def ski(right, down):
    slope_x, slope_y = (right, down)
    route = slope_x
    trees = 0
    for i, row in enumerate(forrest[1:]):
        if (slope_x / slope_y) % 1 != 0 and i  % slope_y != 0:
            continue
        elif row[route] == '#':
            trees += 1
        route += slope_x
        route = route % len(row)
    return trees

print(f'Task One: {ski(3, 1)}')

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
task_2_total = 1
for r, d in slopes:
    res = ski(r, d)
    print(f'{(r, d)}   {res}')
    task_2_total *= res

print(f'Task Two: {task_2_total}') 
# 8147817216 too high
# 4364902080 too low
