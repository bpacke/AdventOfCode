
from math import ceil
lines =[]

with open('input10.txt', 'r') as file:
    for line in file:
        l = line.strip()
        lines.append(l)
print(f'Line count: {len(lines)}')
# chars = []
# start_chars = '({[<'.split('')
# end_chars = list(')}]>')

char_pairs = {')': '(',
'}': '{',
']': '[',
'>': '<',
}

corrupted_chars = []
corrupted_lines = []
line_endings = []
for line in lines:
    chars = []
    for c in line:
        corrupt = False
        if c in list(char_pairs.values()):
            chars.append(c)
        elif c in list(char_pairs.keys()):
            if char_pairs[c] == chars[-1]:
                chars =  chars[:-1]
            else:
                # print(f'Line CORRUPTED @ {c}--- {line}')
                corrupted_chars.append(c)
                corrupted_lines.append(line)
                corrupt = True
                break
    if not corrupt:
        fix = ''
        for ch in reversed(chars):
            for e, s in char_pairs.items():
                if ch == s:
                    fix = fix + e
                    break
        line_endings.append(str(fix))
    

incomplete_lines = [l for l in lines if l not in corrupted_lines]
print(f'Corrupt line count: {len(corrupted_lines)}')
print(f'Incomplete line count: {len(incomplete_lines)}')

syntax_error_score = 0
for c in corrupted_chars:
    if c == ')':
        syntax_error_score = syntax_error_score + 3
    if c == '}':
        syntax_error_score = syntax_error_score + 1197
    if c == ']':
        syntax_error_score = syntax_error_score + 57
    if c == '>':
        syntax_error_score = syntax_error_score + 25137
print(f'syntax_error_score: {syntax_error_score}')

def score_fix(fix):
    # print('------------')
    # print(f'score_fix({fix})')
    char_base_points = {')': 1, '}': 3, ']': 2, '>': 4}
    score = 0
    for f in fix:
        # print(f'score = {score}')
        score = score * 5
        # print(f'score = {score}')
        score = score + char_base_points[f]
        # print(f'score = {score}')
    return score

scores = sorted([score_fix(le) for le in line_endings])
autocomplete_score = scores[int(len(scores) / 2)]
print(f'Autocomplete score  = {autocomplete_score}')
    






