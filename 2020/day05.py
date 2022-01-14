def boarding_pass_decode(boarding_pass):
    rows = list(range(128))
    cols = list(range(8))
    for bp in boarding_pass[:7]:
        if bp == 'F' : rows = rows[:int(len(rows) / 2)]
        elif bp == 'B' : rows = rows[int(len(rows) / 2):]
    for bp in boarding_pass[7:]:
        if bp == 'L' : cols = cols[:int(len(cols) / 2)]
        elif bp == 'R' : cols = cols[int(len(cols) / 2):]
    row = rows[0]
    col = cols[0]
    seat_id = (row * 8) + col
    return seat_id

with open('2020/data/input/day05.txt') as file:
    seat_ids = [boarding_pass_decode(bp.strip()) for bp in file]

print(f'Task One: {max(seat_ids)}')

seat = 0
while seat <= max(seat_ids):
    if seat - 1 in seat_ids and seat not in seat_ids and seat + 1 in seat_ids:
        break
    seat += 1
print(f'Task Two: {seat}')

