in_data = []
with open('input7.txt', 'r') as file:
    for line in file:
        in_data.extend(line.strip().split(','))
start_pos = [int(i) for i in in_data]

fuel = sum(start_pos)
h_pos = 0

for pos in range(min(start_pos), max(start_pos)):
    total_fuel = sum([abs(s - pos) for s in start_pos])
    if total_fuel < fuel:
        fuel = total_fuel
        h_pos = pos
print(f'Position: {h_pos}\nFuel: {fuel}')
