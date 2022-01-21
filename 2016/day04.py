from collections import Counter
def read_puzzle_input(filename):
    rooms = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            encrypted_name = line[:-11].replace('-', '')
            sector_id = int(line[-10:-7])
            checksum = line[-6:-1]
            rooms.append((encrypted_name, sector_id, checksum))
    return rooms

def is_real_room(room):
    encrypted_name = room[0]
    checksum = room[2]
    calculated_checksum = ''
    counter = Counter(encrypted_name)
    unique_character_counts = sorted(list(set(counter.values())), reverse=True)
    counter_items = sorted(counter.items(), key=lambda c:c[0])
    for ucc in unique_character_counts:
        for ci in counter_items:
            if ci[1] == ucc: calculated_checksum += ci[0]
    return calculated_checksum[:5] == checksum

def task_one(rooms):
    real_rooms = [room for room in rooms if is_real_room(room)]
    result = sum([room[1] for room in real_rooms])
    print(f'Task One: {result}')
    return real_rooms

def task_two(rooms):
    print('Task Two:', end=' - ')
    for room in rooms:
        key = room[1] % 26
        decoding = [ord(character) + key for character in room[0]]
        for index, value in enumerate(decoding):
            if value > 122: decoding[index] = value - 26
        decoding = [chr(value) for value in decoding]
        if 'northpole' in ''.join(decoding):
            print(f"{room[1]} - {''.join(decoding)}")

if __name__ == '__main__':
    rooms = read_puzzle_input('2016/data/input/day04.txt')
    real_rooms = task_one(rooms)
    task_two(real_rooms)