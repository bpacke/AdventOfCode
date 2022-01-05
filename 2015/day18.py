task_2 = True
light_grid = []
with open('2015/data/input/day18.txt') as file:
    for line in file:
        row = []
        for light in line:
            if light == '#': row.append(True)
            elif light == '.': row.append(False)
        light_grid.append(row)

def print_grid(grid):
    for row in grid:
        print(''.join(list(map(lambda x: '#' if x else '.', row))))

steps = 100

for step in range(steps):
    new_grid = [[None for _ in l] for l in light_grid]
    for r, lights in enumerate(light_grid):
        for c, light in enumerate(lights):
            neighbours = []
            if r - 1 >= 0 and c - 1 >= 0: neighbours.append((r -1 , c -1))
            if r - 1 >= 0: neighbours.append((r -1 , c))
            if r - 1 >= 0 and c + 1 < len(lights): neighbours.append((r -1 , c + 1))
            if c - 1 >= 0: neighbours.append((r, c - 1))
            if c + 1 < len(lights): neighbours.append((r, c + 1))
            if r + 1 < len(light_grid) and c - 1 >= 0: neighbours.append((r + 1 , c -1))
            if r + 1 < len(light_grid): neighbours.append((r + 1, c))
            if r + 1 < len(light_grid) and c + 1 < len(lights): neighbours.append((r + 1 , c + 1))

            neighbours_on = len([l for l in [light_grid[r][c] for r, c in neighbours] if l == True])
 
            if light == True and (neighbours_on == 2 or neighbours_on == 3): new_grid[r][c] = True
            elif light == True: new_grid[r][c] = False
            elif light == False and neighbours_on == 3: new_grid[r][c] = True
            else: new_grid[r][c] = False

    light_grid = new_grid
count = 0
print(f'# Lights on after {steps} steps: ', end='')
for r in light_grid:
    for l in r:
        if l: count += 1
print(count)