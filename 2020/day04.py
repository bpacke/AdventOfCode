import re
passports = []

with open('2020/data/input/day04.txt') as file:
    passport_lines = []
    for line in file:
        line = line.strip()
        if line != '': passport_lines.append(line)
        else:
            passports.append(' '.join(passport_lines))
            passport_lines = []
    passports.append(' '.join(passport_lines))

def task_1_validate(passport):
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    x = all(map(lambda f: f + ':' in passport, fields))
    return x

valid_passports_1 = [p for p in passports if task_1_validate(p)]
print(f'Task One: {len(valid_passports_1)}')

def task_2_validate(passport):
    valid = True
    try:
        byr = int(re.findall('byr:\d\d\d\d', passport)[0][4:])
        valid = valid and byr >= 1920 and byr <= 2002

        iyr = int(re.findall('iyr:\d\d\d\d', passport)[0][4:])
        valid = valid and iyr >= 2010 and iyr <= 2020

        eyr = int(re.findall('eyr:\d\d\d\d', passport)[0][4:])
        valid = valid and eyr >= 2020 and eyr <= 2030

        hgt = re.findall('hgt:\d\d\d?[cm|in]', passport)[0][4:]
        if hgt[-1] == 'c':
            valid = valid and int(hgt[:-1]) >= 150 and int(hgt[:-1]) <= 193
        elif hgt[-1] == 'i':
            valid = valid and int(hgt[:-1]) >= 59 and int(hgt[:-1]) <= 76

        hcl = re.findall('hcl:#[0-9a-f]+', passport)[0][4:]
        valid = valid and len(hcl) == 7

        ecl_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        ecl = re.findall('ecl:\w\w\w', passport)[0][4:]
        valid = valid and ecl in ecl_list
   
        pid = re.findall('pid:\d+', passport)[0][4:]
        valid = valid and len(pid) == 9
    except IndexError:

        valid = False

    return valid
    
    
count = 0
for v in valid_passports_1:
    if task_2_validate(v): count += 1
print(f'Task Two: {count}')