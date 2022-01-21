
def read_in_file(filename):
    instructions = []
    with open(filename) as file:
        for line in file:
            instructions += line.strip().split(', ')
    return instructions

def do_task(instructions, task_two=False):
        x_travelled = 0
        y_travelled = 0
        directions = ['N', 'E', 'S', 'W']
        current_direction = 'N'
        visited_locations = [(0, 0)]

        found = False
        index = 0
        while found == False and index < len(instructions):
            i = instructions[index]
            travel_direction = i[0]
            travel_distance = int(i[1:])
            if travel_direction == 'R': current_direction = directions [(directions.index(current_direction) + 1) % len(directions)]
            elif travel_direction == 'L': current_direction = directions [(directions.index(current_direction) - 1) % len(directions)]
            if current_direction == 'N':
                for _ in range(travel_distance):
                    y_travelled += 1
                    coords = (y_travelled, x_travelled)
                    visited_locations.append(coords)
                    if task_two and visited_locations[-1] in visited_locations[:-1]: 
                        visited_locations.append(coords)
                        found = True
                        break

            elif current_direction == 'S':
                for _ in range(travel_distance): 
                    y_travelled -= 1
                    coords = (y_travelled, x_travelled)
                    visited_locations.append(coords)
                    if task_two and visited_locations[-1] in visited_locations[:-1]: 
                        visited_locations.append(coords)
                        found = True
                        break

            elif current_direction == 'E':
                for _ in range(travel_distance):
                    x_travelled += 1
                    coords = (y_travelled, x_travelled)
                    visited_locations.append(coords)
                    if task_two and visited_locations[-1] in visited_locations[:-1]: 
                        visited_locations.append(coords)
                        found = True
                        break

            elif current_direction == 'W':
                for _ in range(travel_distance):
                    x_travelled -= 1
                    coords = (y_travelled, x_travelled)
                    visited_locations.append(coords)
                    if task_two and visited_locations[-1] in visited_locations[:-1]: 
                        visited_locations.append(coords)
                        found = True
                        break
            index += 1
        return abs(visited_locations[-1][0])  + abs(visited_locations[-1][1])

if __name__ == '__main__':
    steps = read_in_file('2016/data/input/day01.txt')
    print(f'Task One: {do_task(steps)}')
    print(f'Task Two: {do_task(steps, task_two=True)}')
