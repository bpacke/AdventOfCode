part = 2
size = 1000
if part == 1:
    light_grid = [[False for _ in range(size)] for _ in range(size)]
elif part == 2:
    light_grid = [[0 for _ in range(size)] for _ in range(size)]

with open('2015/data/input/day06.txt', 'r') as file:
    for line in file:
        line = line.strip().split(' ')
        start = line[-3]
        end = line[-1]
        start_x, start_y = int(start.split(',')[0]), int(start.split(',')[1])
        end_x, end_y = int(end.split(',')[0]), int(end.split(',')[1])
        # print(f'{start_x}, {start_y} -> {end_x}, {end_y}')
        for r in range(start_x, end_x + 1):
            for c in range(start_y, end_y + 1):
                if part == 1:
                    if 'on' in line: light_grid[r][c] = True
                    elif 'off' in line:light_grid[r][c] = False
                    elif 'toggle' in line: light_grid[r][c] = not light_grid[r][c]
                elif part == 2:
                    if 'on' in line: light_grid[r][c] = light_grid[r][c] + 1
                    elif 'off' in line and light_grid[r][c] > 0: light_grid[r][c] = light_grid[r][c] - 1
                    elif 'toggle' in line: light_grid[r][c] = light_grid[r][c] + 2
if part == 1:
    lights_on = 0
    for row in light_grid:
        for light in row:
            if light == True: lights_on = lights_on + 1

    print(f'Lights on: {lights_on}')
elif part == 2:
    brightness = 0
    for row in light_grid:
        for light in row:
            brightness = brightness + light

    print(f'Brightness: {brightness}')
