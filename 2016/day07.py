from collections import Counter

def read_puzzle_input(filename):
    ipv7_addresses = []
    with open(filename) as file:
        for line in file:
            line = line.strip().replace('[', ' [').replace(']', '] ').split()
            supernets = [x for x in line if '[' not in x]
            hypernets = [x[1:-1] for x in line if '[' in x]
            ipv7_addresses.append((supernets, hypernets))
    return ipv7_addresses

def does_contain_ABBA(in_string):
    substrings = [in_string[s:e] for s in range(len(in_string)) for e in range(s + 1, len(in_string) + 1) if len(in_string[s:e]) == 4]
    for s in substrings:
        character_count = len(Counter(s).keys())
        if character_count == 2 and list(s) == list(reversed(s)): return True
    return False

def ipv7_supports_TLS(ipv7):
    supernets = [does_contain_ABBA(ip) for ip in ipv7[0]]
    hypernets = [does_contain_ABBA(ip) for ip in ipv7[1]]
    return any(supernets) and not any(hypernets)

def task_one(puzzle_input):
    supports_TLS = []
    for ip in puzzle_input:
        if ipv7_supports_TLS(ip):
            supports_TLS.append(ip)
    return supports_TLS

def task_two(puzzle_input):
    return []

if __name__ == '__main__':
    puzzle_input = read_puzzle_input('2016/data/input/day07.txt')
    t1 = task_one(puzzle_input)
    print(f'Task One: {len(t1)}')
    t2 = task_two(puzzle_input)
    print(f'Task Two: {len(t2)}')