circut = []
completed_circuit = []
signals = {}

with open('2015/data/input/day07.txt', 'r') as file:
    for line in file:
        steps = line.strip().split(' ')
        # print(steps)
        circut.append(steps)
while True:
    for step in circut:
        if step not in completed_circuit:
            try:
                if len(step) == 3: # 123 -> x
                    signals[step[-1]] = int(step[0])
                elif len(step) == 4: # NOT e -> f
                    signals[step[-1]] =  int(''.join(['1' if b == '0' else '0' for b in format(signals[step[1]], '016b')]), 2)
                else: # AND|OR|LSHIFT|RSHIFT     x AND y -> d
                    if step[1] == 'AND':
                        signals[step[-1]] = signals[step[0]] & signals[step[2]]
                    elif step[1] == 'OR':
                        signals[step[-1]] = signals[step[0]] | signals[step[2]]
                    elif step[1] == 'LSHIFT':
                        signals[step[-1]] = signals[step[0]] << int(step[2])
                    elif step[1] == 'RSHIFT':
                        signals[step[-1]] = signals[step[0]] >> int(step[2])
                completed_circuit.append(step)
                print(f'Completed step: {step}')
            except Exception:
                print('Exception')
        else:
            pass #step already happened
    if len(completed_circuit) == len(circut): break
        
a = signals['a']
print(f'Task One: Singal \'a\' = {a}')