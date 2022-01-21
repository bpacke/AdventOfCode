import re
def read_puzzle_input(filename, task_two=False):
    potential_triangles = []
    side_one = []
    side_two = []
    side_three = []
    with open(filename) as file:
        for line in file:
            line_triangle = [int(side) for side in re.findall('\d+', line)]
            if task_two:
                side_one.append(line_triangle[0])
                side_two.append(line_triangle[1])
                side_three.append(line_triangle[2])
            else: potential_triangles.append(line_triangle)
    if task_two: 
        all_sides = side_one + side_two + side_three
        for index in range(0, len(all_sides), 3):
            potential_triangles.append(all_sides[index:index + 3])     
    return potential_triangles

def is_valid_triangle(potential_triangle):
    potential_triangle.sort()
    return sum(potential_triangle[:-1]) > potential_triangle[-1]

def do_task(triangles):
    valid_triangles = []
    for t in triangles:
        if is_valid_triangle(t): valid_triangles.append(t)
    return len(valid_triangles)

if __name__ == '__main__':
    potential_triangles_one = read_puzzle_input('2016/data/input/day03.txt')
    print(f'Task One: {do_task(potential_triangles_one)}')
    potential_triangles_two = read_puzzle_input('2016/data/input/day03.txt', task_two=True)
    print(f'Task Two: {do_task(potential_triangles_two)}')