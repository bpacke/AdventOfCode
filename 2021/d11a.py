class Dumbo():
    energy_level = None
    did_flash = None
    co_ordinates = ()
    neighbours = []
    def __init__(self, energy):
        self.energy_level = energy
        self.did_flash = False

    def set_neighbours(self, neigh):
        self.neighbours = neigh

    # def increment_energy_by_one(self):
    #     self.energy_level = self.energy_level + 1
    def increment_energy_by_one(self):
        if self.energy_level < 9:
            self.energy_level = self.energy_level + 1
        elif not self.did_flash:
            self.flash()

    def flash(self):
        global flash_counter
        flash_counter =  flash_counter + 1
        self.did_flash = True
        for n_row, n_col in self.neighbours:
            grid[n_row][n_col].increment_energy_by_one()

    def __str__(self):
        return(str(self.energy_level))
    

def print_grid(g):
    print('-' * 33)
    for a in g:
        for b in a:
            print(f'{b}', end='\t')
        print('\n')
    print('-' * 33)

flash_counter = 0
grid =[]

#populate grid with dumbos and then tell it its coordinates and neighbours
with open('input11.txt', 'r') as file:
    for line in file:
        l = line.strip()
        grid.append([Dumbo(int(x)) for x in list(l)])
for r, row in enumerate(grid):
    for c, dumbo in enumerate(row):
        dumbo.co_ordinates = (r, c)
        neighbours = []
        if r - 1 >= 0 and c - 1 >= 0: neighbours.append((r -1 , c -1))
        if r - 1 >= 0: neighbours.append((r -1 , c))
        if r - 1 >= 0 and c + 1 < len(row): neighbours.append((r -1 , c + 1))
        if c - 1 >= 0: neighbours.append((r, c - 1))
        if c + 1 < len(row): neighbours.append((r, c + 1))
        if r + 1 < len(grid) and c - 1 >= 0: neighbours.append((r + 1 , c -1))
        if r + 1 < len(grid): neighbours.append((r + 1, c))
        if r + 1 < len(grid) and c + 1 < len(row): neighbours.append((r + 1 , c + 1))

        print(f'Dumbo {dumbo} has neighbours count: {len(neighbours)}')
        dumbo.set_neighbours(neighbours)

print_grid(grid)

# Step A  -- Increase values by 1
for i in range(1000):
    print(f'^^^   Step {i}   ^^^   -   FC:{flash_counter}')
    for r in grid:
        for d in r:
            d.increment_energy_by_one()
    for r in grid:
        for d in r:
            if d.did_flash:
                d.did_flash = False
                d.energy_level = 0
    # print_grid(grid)
    energy_sum = 0
    for r in grid:
        for d in r:
            energy_sum = energy_sum + d.energy_level
    if energy_sum == 0: break
print(f'^^^   Step {i +  1}   ^^^   -   FC:{flash_counter}')
print_grid(grid)
