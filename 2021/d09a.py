import functools
cave_floor = []
lowest_points = []
lowest_points_locs = []

with open('input09.txt', 'r') as file:
    for line in file:
        l = line.strip()
        cave_floor.append([int(i) for i in list(l)])

for row in range(len(cave_floor)):
    for col in range(len(cave_floor[row])):
        neighbours = []
        if row - 1 >= 0: neighbours.append(cave_floor[row - 1][col])
        if row + 1 < len(cave_floor): neighbours.append(cave_floor[row + 1][col])
        if col - 1 >= 0: neighbours.append(cave_floor[row][col - 1])
        if col + 1 < len(cave_floor[row]): neighbours.append(cave_floor[row][col + 1])

        if cave_floor[row][col] < min(neighbours):
            lowest_points.append(cave_floor[row][col])
            lowest_points_locs.append((row, col))

print(lowest_points)
risk_level = sum(lowest_points) + len(lowest_points)
print(f'Risk Level: {risk_level}')


print(f'len(cave_floor): {len(cave_floor)}')
for i, c in enumerate(cave_floor):
    print(f'len(row[i]): {len(c)}')


print('-------- Part 2 --------')

for basin_centre in lowest_points_locs:
    finished = True
    basin_points = []
    to_search = []
    searched = []
    while not finished:
        pass
    
def find_basin_points(row, col):
    # print(f'Given ({row}, {col})   ---   Value {cave_floor[row][col]}')
    incremental_neighbours = []
    # print(f'U {row} - 1 >= 0')
    if row - 1 >= 0:
        # print(f'UP avaliable   --   @ ({row-1}, {col})   --   Value {cave_floor[row-1][col]}')
        if cave_floor[row - 1][col] == cave_floor[row][col] + 1:
            if cave_floor[row - 1][col] < 9:
                incremental_neighbours.append((row - 1, col))
    # print(f'D {row} + 1 < {len(cave_floor)}')
    if row + 1 < len(cave_floor):
        # print(f'DOWN avaliable   --   @ ({row+1}, {col})   --   Value {cave_floor[row+1][col]}')
        if cave_floor[row + 1][col] == cave_floor[row][col] + 1:
            if cave_floor[row + 1][col] < 9:
                incremental_neighbours.append((row + 1, col))
    # print(f'L {col} - 1 >= 0')
    if col - 1 >= 0:
        # print(f'LEFT avaliable   --   @ ({row}, {col-1})   --   Value {cave_floor[row][col-1]}')
        if cave_floor[row][col - 1] == cave_floor[row][col] + 1:
            if cave_floor[row][col - 1] < 9:
                incremental_neighbours.append((row, col - 1))
    # print(f'R {col} + 1 < {len(cave_floor[row])}')
    if col + 1 < len(cave_floor[row]):
        # print(f'RIGHT avaliable   --   @ ({row}, {col+1})   --   Value {cave_floor[row][col+1]}')
        if cave_floor[row][col + 1] == cave_floor[row][col] + 1:
            if cave_floor[row][col + 1] < 9:
                incremental_neighbours.append((row, col + 1))
    # next_search = [find_basin_points(*i) for i in incremental_neighbours]
    # incremental_neighbours.extend([find_basin_points(*i) for i in incremental_neighbours])
    # return incremental_neighbours + [find_basin_points(*i) for i in incremental_neighbours]
    for searches in [find_basin_points(*i) for i in incremental_neighbours]:
        for s in searches:
            incremental_neighbours.append(s)
    return list(set(incremental_neighbours))

basin_sizes = []
for b in lowest_points_locs:
    print('-'* 25)
    print(f'Basin at centre {b} has points:')
    basin = find_basin_points(*b)

    # print([cave_floor[x][y] for x, y in basin])
    print(f'{basin}\nSize: {len(basin) + 1}\n---------------')
    basin_sizes.append(len(basin) + 1)

basin_sizes.sort()
print(f'3 largest basins are or sizes {basin_sizes[-3:]}')   
print(f'Answer = {functools.reduce(lambda x, y: x * y, basin_sizes[-3:])}') 


    
