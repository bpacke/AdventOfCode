from functools import cache
import hashlib

first_interesting = 0

@cache
def md5_interesting_values(string_to_hash, index, task_two=False, leading_zeroes=5):
    global first_interesting
    zeroes = ''.join(['0' for _ in range(leading_zeroes)])
    md5_value = hashlib.md5(f'{string_to_hash}{index}'.encode('utf-8')).hexdigest()
    if md5_value[:len(zeroes)] == zeroes:
        if first_interesting == 0: first_interesting = index
        return (md5_value[5], md5_value[6])
    elif not task_two: return (False, False)
    else: return ('False', '') # implementation of task_two relies on ValueError when using int()

def task_one(key):
    print('Task One:')
    password = ''
    index = 0
    while len(password) < 8:
        password_character, _ = md5_interesting_values(key, index)
        if password_character:
            password += password_character
        index = index + 1
    print(password)

# I work, but I'm kinda slow
def task_two(key):
    global first_interesting
    print('Task Two:')
    password = [False for _ in range(8)]
    index = first_interesting
    while False in password:
        password_index, password_character = md5_interesting_values(key, index, task_two=True)
        try:
            password_index = int(password_index)
            if password_index in range(8) and not password[password_index]:
                password[int(password_index)] = password_character
        except ValueError: pass
        index = index + 1
    print(''.join(password))

if __name__ == '__main__':
    key = 'wtnhxymk'
    task_one(key)
    task_two(key)
