import string, textwrap
puzzle_input = 'hxbxwxba'

def string_chunker(string):
    arr = []
    current_char = string[0]
    count = 0
    for s in string:
        if s == current_char: count = count + 1
        else:
            app_string = current_char * count
            for a in textwrap.wrap(app_string, 2):
                arr.append(a)
            current_char = s
            count = 1
    app_string = current_char * count
    for a in textwrap.wrap(app_string, 2):
        arr.append(a)
    return arr

def password_iterator(string):
    if len(string) == 0: return 'a'
    if ord(string[-1]) < 122:
        return string[:-1] + chr(ord(string[-1]) + 1)
    elif ord(string[-1]) == 122:
        return password_iterator(string[:-1]) + 'a'

def password_validator(password):
    # Passwords must include one increasing straight of at least three letters, 
    # like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
    triplets = list(zip(password, password[1:], password[2:]))
    letter_distances = [(ord(c) - ord(b), ord(b) - ord(a)) for a, b, c in triplets]
    test_1 = (1, 1) in letter_distances

    # Passwords may not contain the letters i, o, or l, as these letters can be 
    # mistaken for other characters and are therefore confusing.
    check_i = not 'i' in password
    check_o = not 'o' in password
    check_l = not 'l' in password
    test_2 = check_i and check_o and check_l

    # Passwords must contain at least two different, non-overlapping pairs of 
    # letters, like aa, bb, or zz.
    chunks = [len(s) for s in string_chunker(password)]
    test_3 = chunks.count(2) >= 2

    return test_1 and test_2 and test_3

while not password_validator(puzzle_input):
    puzzle_input = password_iterator(puzzle_input)
print(f'Task 1 Password: {puzzle_input}')

puzzle_input = password_iterator(puzzle_input)

while not password_validator(puzzle_input):
    puzzle_input = password_iterator(puzzle_input)
print(f'Task 2 Password: {puzzle_input}')