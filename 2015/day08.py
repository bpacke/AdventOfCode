string_lits = []
with open('2015/data/input/day08.txt', 'r') as file:
    for line in file:
        line = line.strip()
        a = len(line)
        b = len(line.encode('utf-8').decode('unicode-escape'))
        string_lits.append((line, a, b - 2))
str_value = sum([a for _, a, _ in string_lits])
mem_value = sum([b for _, _, b in string_lits])
print(f'Memory Value: {str_value - mem_value}')

new_mem_value = 0
for string, _, _ in string_lits:
    count = 2
    for s in string:
        if s == '"' or s == '\\':
            count = count + 2
        else: count = count + 1
    new_mem_value = new_mem_value + count

print(f'NEW Memory Value: {new_mem_value}')
print(f'Part 2: {new_mem_value - str_value}')
