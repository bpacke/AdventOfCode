puzzle_input = 3310000

def present_count(house_number):
    return sum([n for n in range(1, house_number + 1) if house_number % n == 0]) * 10

for house in range(1, puzzle_input):
    gifts = present_count(house)
    if gifts >= puzzle_input:
        print(f'House {house}: {gifts} presents')
        break
        
print('Done')