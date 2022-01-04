#on x=10..12,y=10..12,z=10..12

co_ords = []
with open('2021/test22.txt', 'r') as file:
    for line in file:
        line = line.strip()
        cmd = line.split(' ')[0]
        line = line[len(cmd) + 1:]
        x = line.split(',')[0]
        x = [int(i) for i in x[2:].split('..')]
        y = line.split(',')[1]
        y = [int(i) for i in y[2:].split('..')]
        z = line.split(',')[2]
        z = [int(i) for i in z[2:].split('..')]
        co_ords.append((x, y, z, cmd))
        print((x, y, z, cmd))
