import string, textwrap
puzzle_input = 'hxbxwxba'

def string_split(string):
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

def password_iterator(password):
    alphabet = list(string.ascii_lowercase)
    valid_alpha = alphabet
    valid_alpha.remove('i')
    valid_alpha.remove('o')
    valid_alpha.remove('l')
    print(valid_alpha)
    # chr_range = [ord(a) for a in alphabet]
    # c_tmp = ascii_password[0] + 1
    # c = c_tmp if c_tmp < chr_range[-1] else char_range[0]
    # print(chr(c))

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
    chunks = [len(s) for s in string_split(password)]
    test_3 = chunks.count(2) >= 2

    return test_1 and test_2 and test_3
