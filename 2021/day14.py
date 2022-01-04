from collections import Counter
polymer_template = ''
insertion_rules = {}

with open('input14.txt', 'r') as file:
    for line in file:
        l = line.strip()
        if l != '' and '-' not in l:
            polymer_template = l
        elif '-' in l:
            k = l.split(' -> ')[0]
            v = l.split(' -> ')[-1]
            insertion_rules[k] = v

print(f'Polymer Template: {polymer_template}')
for i in insertion_rules.items():
    print(i)

steps = 40
for s in range(steps):
    print(s)
    new_polymer = polymer_template[:1]
    for a, b in zip(polymer_template, polymer_template[1:]):
        key = a + b
        new_polymer = new_polymer + insertion_rules[key] + b
    polymer_template = new_polymer

print('Most - Least Common Count')
counter = Counter(polymer_template)
print(max(counter.values()) - min(counter.values()))
