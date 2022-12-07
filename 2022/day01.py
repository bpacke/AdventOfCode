elves_loadout = []

with open('2022/data/input/day01.txt', 'r') as file:
    loadout = []
    for line in file:
        if line.strip() == '':
            elves_loadout.append(loadout)
            loadout = []
        else:
            loadout.append(int(line.strip()))

elves_loadout.sort(key=lambda el: sum(el), reverse=True)

print(f'Task One\nTotal: {sum(elves_loadout[0])}\nLoadout: {elves_loadout[0]}\n')

print(f'Task Two\nTotal: {sum([sum(el) for el in elves_loadout[0:3]])}\nLoadouts: {elves_loadout[0:3]}\n')
