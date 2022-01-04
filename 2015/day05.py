from collections import Counter
strings = []

with open('2015/data/input/day05.txt', 'r') as file:
    for line in file:
        line = line.strip()
        c = Counter(line)
        rule_1 = c['a'] + c['e'] + c['i'] + c['o'] + c['u'] >= 3
        rule_3 = not ('ab' in line or 'cd'in line or  'pq'in line or  'xy'in line)
        rule_2 = any([a == b for a, b in zip(line, line[1:])])
        strings.append((line, rule_1 and rule_2 and rule_3))

nice = [s for s, n in strings if n is True]
naughty = [s for s, n in strings if n is False]

print(f'TASK 1   -   There are {len(nice)} nice strings and {len(naughty)} naughty strings')

strings = [s for s, _ in strings]
strings_new = []

for s in strings:
    string_zipped = list(zip(s, s[1:]))
    pairs = []
    for i, z in enumerate(string_zipped):
        list_end = string_zipped[i + 2:]
        if z in list_end: pairs.append(z)
    new_rule_1 = any(pairs)
    new_rule_2 = any([a == b for a, b in zip(s, s[2:])])
    strings_new.append((s, new_rule_1 and new_rule_2))

nice_new = [s for s, n in strings_new if n is True]
naughty_new = [s for s, n in strings_new if n is False]

print(f'Task 2   -   There are {len(nice_new)} nice strings and {len(naughty_new)} naughty strings')
