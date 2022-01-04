input_coordinates = []
input_folds = []

#read in input file and add the coordinates and fold directions into corresponding lists
with open('input13.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line != '' and ' ' not in line:
            coords_str = line.split(',')
            input_coordinates.append((int(coords_str[0]), int(coords_str[1])))
        elif line != '' and '=' in line:
            fold_str = line.split(' ')[-1]
            fold_dir = fold_str.split('=')[0]
            fold_loc = fold_str.split('=')[-1]
            input_folds.append((fold_dir, int(fold_loc)))

# a grid the correct size for all the points
paper_width = 1 + max([x for x, _ in input_coordinates])
paper_height = 1 + max([y for _, y in input_coordinates])
grid = [[False for _ in range(paper_width)] for _ in range(paper_height)]


def print_grid(g):
    for a in range(len(g)):
        for b in range(len(g[a])):
            if g[a][b] is True: print('⬜️', end='')
            else: print('⬛️', end='')
        print()


for x, y in input_coordinates:
    grid[y][x] = True

# print_grid(grid)

for fold_dir, fold_loc in input_folds:
    if fold_dir == 'x':
        temp_grid = []
        new_grid = []
        for r in grid:
            temp_grid.append(r[::-1])
        for r in range(len(grid)):
            row = []
            for g, t, in zip(grid[r][:fold_loc], temp_grid[r][:fold_loc]):
                row.append(g or t)
            new_grid.append(row)
        grid = new_grid


        
    elif fold_dir == 'y':
        temp_grid = grid[::-1]
        new_grid = []
        for i in range(fold_loc):
            row = []
            for g, t in zip(grid[i], temp_grid[i]):
                row.append(g or t)

            new_grid.append(row)
        grid = new_grid
    # print('%' * 25)
    # print_grid(grid)
    dot_count = 0
    # for r in grid:
    #     for i in r:
    #         if i == True: dot_count = dot_count + 1
    # print(f'Dot count = {dot_count}')
print_grid(grid)