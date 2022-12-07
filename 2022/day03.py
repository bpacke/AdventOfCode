item_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
item_character_priorites = dict(zip(item_characters, range(1, 53)))

rucksacks = []
split_rucksacks = []

with open('2022/data/input/day03.txt', 'r') as file:
    for line in file:
        line = line.strip()
        split_point = int(len(line) / 2)
        compartment_1 = line[:split_point]
        compartment_2 = line[split_point:]
        duplicate = list(set(compartment_1).intersection(set(compartment_2)))[0]
        split_rucksacks.append((compartment_1, compartment_2, duplicate))
        rucksacks.append(line)

print(f'Task One = {sum(item_character_priorites[d] for _, _, d in split_rucksacks)}')

rucksack_groups = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]
elf_groups = [list(set(a).intersection(set(b), set(c)))[0] for a, b, c in rucksack_groups]

print(f'Task Two = {sum(item_character_priorites[eg] for eg in elf_groups)}')
