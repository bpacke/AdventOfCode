class Present():
    l = 0
    w = 0
    h = 0
    total_area = 0
    paper_needed = 0
    ribbon_needed = 0
    def __init__(self, input_string):
        input_dimensions = input_string.split('x')
        self.l = int(input_dimensions[0])
        self.w = int(input_dimensions[1])
        self.h = int(input_dimensions[2])
        area_x = 2*self.l*self.w
        area_y = 2*self.w*self.h
        area_z = 2*self.h*self.l
        self.total_area = area_x + area_y + area_z
        self.paper_needed = self.total_area + int(min([area_x, area_y, area_z]) / 2)
        self.ribbon_needed = (sum(sorted([self.l, self.w, self.h])[:2]) * 2) + (self.l * self.w * self.h)
    def __str__(self):
        return f'A Present with l, w, h {self.l}, {self.w}, {self.h} has area of {self.total_area} and needs paper of size {self.paper_needed}.'

presents = []

with open('2015/data/input/day02.txt', 'r') as file:
    for line in file:
        # print(f'line = {line}')
        presents.append(Present(line))

total_paper_needed = sum([p.paper_needed for p in presents])
total_ribbon_needed = sum([p.ribbon_needed for p in presents])
print(f'Total paper needed: {total_paper_needed}')
print(f'Total ribbon needed: {total_ribbon_needed}')
