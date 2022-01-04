import hashlib

key = ''

with open('2015/data/input/day04.txt', 'r') as file:
    for line in file:
        key = line.strip()

index = 0
while True:
    # print(f'Trying {key}{index}')
    md5_value = hashlib.md5(f'{key}{index}'.encode('utf-8')).hexdigest()
    if md5_value[:6] == '000000':
        print(index)
        break
    index = index + 1
