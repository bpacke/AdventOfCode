puzzle_input = 33100000
elf_visits = dict.fromkeys(list(range(1, 7761600)), 0)

def present_count(house_number):
    return sum([n for n in range(1, house_number + 1) if house_number % n == 0]) * 10

from functools import reduce

def factors(n):    
    facs = set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    to_return = []
    for f in facs:
        if elf_visits[f] < 50:
            elf_visits[f] += 1
            to_return.append(f)
    return to_return

def pres2(house_number):
    return sum(factors(house_number)) * 10
def pres_part2(house_number):
    return sum(factors(house_number)) * 11




for house in range(1, puzzle_input):
    gifts = pres_part2(house)
    if gifts >= puzzle_input:
        print(f'House {house}: {gifts} presents')
        break
        
print('Done') #83160 too low