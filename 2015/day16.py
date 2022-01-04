import re

# children: 3
# cats: 7
# samoyeds: 2
# pomeranians: 3
# akitas: 0
# vizslas: 0
# goldfish: 5
# trees: 3
# cars: 2
# perfumes: 1

sender = (3, 7, 2, 3, 0, 0, 5, 3, 2, 1)
aunts = []
candidates = []

with open('2015/data/input/day16.txt') as file:
    for line in file:
        aunt = re.findall('Sue \d+', line)[0]
        children = re.findall('children: \d+', line)
        cats = re.findall('cats: \d+', line)
        samoyeds = re.findall('samoyeds: \d+', line)
        pomeranians = re.findall('pomeranians: \d+', line)
        akitas = re.findall('akitas: \d+', line)
        vizslas = re.findall('vizslas: \d+', line)
        goldfish = re.findall('goldfish: \d+', line)
        trees = re.findall('trees: \d+', line)
        cars = re.findall('cars: \d+', line)
        perfumes = re.findall('perfumes: \d+', line)

        children = int(re.findall('\d+', children[0])[0]) if len(children) > 0 else 0
        cats = int(re.findall('\d+', cats[0])[0]) if len(cats) > 0 else 0
        samoyeds = int(re.findall('\d+', samoyeds[0])[0]) if len(samoyeds) > 0 else 0
        pomeranians = int(re.findall('\d+', pomeranians[0])[0]) if len(pomeranians) > 0 else 0
        akitas = int(re.findall('\d+', akitas[0])[0]) if len(akitas) > 0 else 0
        vizslas = int(re.findall('\d+', vizslas[0])[0]) if len(vizslas) > 0 else 0
        goldfish = int(re.findall('\d+', goldfish[0])[0]) if len(goldfish) > 0 else 0
        trees = int(re.findall('\d+', trees[0])[0]) if len(trees) > 0 else 0
        cars = int(re.findall('\d+', cars[0])[0]) if len(cars) > 0 else 0
        perfumes = int(re.findall('\d+', perfumes[0])[0]) if len(perfumes) > 0 else 0

        knowledge = len([a for a in [children, cats, samoyeds, pomeranians, akitas, vizslas, goldfish, trees, cars, perfumes] if a > 0])
        if knowledge < 3:
            pass
            # print(f'I don\'t know enough about {aunt}')
        else:
            aunts.append((aunt, children, cats, samoyeds, pomeranians, akitas, vizslas, goldfish, trees, cars, perfumes))

print('------   Task 1   ------')
for aunt, ch, ct, sa, po, ak, vi, go, tr, cr, pe in aunts:
    if (ch == sender[0] or ch == 0) and (ct == sender[1] or ct == 0) and (sa == sender[2] or sa == 0) and (po == sender[3] or po == 0) and (ak == sender[4] or ak == 0) and (vi == sender[5] or vi == 0) and (go == sender[6] or go == 0) and (tr == sender[7] or tr == 0) and (cr == sender[8] or cr == 0) and (pe == sender[9] or pe == 0):
            if ch + ct + sa + po + ak + vi + go + tr + cr + pe == 0:
                pass # I know nothing about them
            else: print((aunt, ch, ct, sa, po, ak, vi, go, tr, cr, pe))

print('------   Task 2   ------')
for aunt, ch, ct, sa, po, ak, vi, go, tr, cr, pe in aunts:
    if (ch == sender[0] or ch == 0) and (ct > sender[1] or ct == 0) and (sa == sender[2] or sa == 0) and (po < sender[3] or po == 0) and (ak == sender[4] or ak == 0) and (vi == sender[5] or vi == 0) and (go < sender[6] or go == 0) and (tr > sender[7] or tr == 0) and (cr == sender[8] or cr == 0) and (pe == sender[9] or pe == 0):
            if ch + ct + sa + po + ak + vi + go + tr + cr + pe == 0:
                pass #I know nothing about them
            else: print((aunt, ch, ct, sa, po, ak, vi, go, tr, cr, pe))
        
        