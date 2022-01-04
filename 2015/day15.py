# Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
# Candy: capacity 0, durability 5, flavor -1, texture 0, calories 8
# Butterscotch: capacity -1, durability 0, flavor 5, texture 0, calories 6
# Sugar: capacity 0, durability 0, flavor -2, texture 2, calories 1
from itertools import combinations_with_replacement
from re import findall
from collections import Counter

ingredients = {}
with open('2015/data/input/day15.txt') as file:
    for line in file:
        name = line.split(':')[0]
        vals = list(map(int, findall('-?\d+', line)))
        ingredients[name] = vals
spoons = 100
recipes = combinations_with_replacement(ingredients, spoons)
scores = []

demo = False

for r in recipes:
    counter = Counter(r)
    # if counter.get('Butterscotch') == 44 and counter.get('Cinnamon') == 56: print('DEMO')
    # print(r)
    cap = 0
    dur = 0
    fla = 0
    tex = 0
    cals = 0
    for i in counter.keys():
        cap += counter.get(i) * ingredients[i][0]
        dur += counter.get(i) * ingredients[i][1]
        fla += counter.get(i) * ingredients[i][2]
        tex += counter.get(i) * ingredients[i][3]
        cals += counter.get(i) * ingredients[i][4]
    if cap < 0: cap = 0
    if dur < 0: cap = 0
    if fla < 0: cap = 0
    if tex < 0: cap = 0
    score = (cap * dur * fla * tex, cals)
    scores.append(score)

scores.sort(key=lambda s: s[0])
print(f'Task One: {max(scores)[0]}')
scores_with_cals = [s for s, c in scores if c == 500]
print(f'Task One: {max(scores_with_cals)}')