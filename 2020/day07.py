from functools import cache
import re
bag_rules = {}
puzzle = 'shiny gold'

with open('2020/data/input/day07.txt') as file:
    for line in file:
        bag_split = line.split(' bags contain')
        bag_type = bag_split[0]
        bags_insde = [b[:-4] for b in re.findall('\w+ \w+ bag',bag_split[1].strip())]
        if bags_insde == ['no other']: bags_insde = []
        bag_rules[bag_type] = bags_insde

@cache
def bag_contents(bag):
    if bag == []: return []
    to_return = bag_rules[bag]
    for b in bag_rules[bag]:
        to_return += bag_contents(b)
    return list(set(to_return))

bag_matryoshka = [(bag, bag_contents(bag)) for bag in bag_rules.keys()]
task_1_bags = [bag for bag, contents in bag_matryoshka if puzzle in contents]
print(len(task_1_bags))
