
# from math import 
from re import findall

instructions = []
directions = ['N', 'E', 'S', 'W']
ferry_direction = 'E'
ferry_x = 0
ferry_y = 0
with open('2020/data/input/day12.txt') as file:
    for line in file:
        action = findall('[A-Z]', line)[0]
        value = int(findall('\d+', line)[0])

        if action == 'N':
            ferry_y += value
        elif action == 'S':
            ferry_y -= value
        elif action == 'E':
            ferry_x += value
        elif action == 'W':
            ferry_x -= value
        elif action == 'L':
            # print(f'Direction: {ferry_direction}')
            jump = -value // 90
            # print(action, value)
            ferry_direction = directions[(directions.index(ferry_direction) + jump) % len(directions)]
            # print(f'Direction: {ferry_direction}')
        elif action == 'R':
            # print(f'Direction: {ferry_direction}')
            jump = value // 90
            # print(action, value)
            ferry_direction = directions[(directions.index(ferry_direction) + jump) % len(directions)]
            # print(f'Direction: {ferry_direction}')
        elif action == 'F':
            if ferry_direction == 'N':
                ferry_y += value
            elif ferry_direction == 'S':
                ferry_y -= value
            elif ferry_direction == 'E':
                ferry_x += value
            elif ferry_direction == 'W':
                ferry_x -= value

        # instructions.append((action, value))
        # print((action, value))
mannhattan_distance = abs(ferry_x) + abs(ferry_y)
print(f'Task One: {mannhattan_distance}')


