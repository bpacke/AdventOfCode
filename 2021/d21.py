class DeterministicDie():
    value = None
    rolls = None
    def __init__(self):
        self.value = -1
        self.rolls = 0
    def roll(self):
        self.value = (self.value + 1) % 10
        self.rolls = self.rolls + 1
        return self.value + 1


die = DeterministicDie()
finish_score = 1000
p1_pos = 8
p2_pos = 4
p1_score = 0
p2_score = 0

# while p1_score < 1000 and p2_score < 1000:

#player 1 goes
while True:
    #Player 1 rolls 1+2+3 and moves to space 10 for a total score of 10.
    print (f'Player 1 rolls ', end='')
    rolls = [die.roll() for i in range(3)]
    print (f'{rolls}', end='')
    move = sum(rolls)
    p1_pos = ((p1_pos + move -1 ) % 10) + 1
    print (f' and moves to space {p1_pos} for a total score of ', end='')
    p1_score = p1_score + p1_pos
    print(f'{p1_score}.')
    if p1_score >= finish_score:
        print(f'Player 1 WINS\nP1 Score: {p1_score}\nP2 Score: {p2_score}\nDice Rolls: {die.rolls}')
        print(f'Game Score: {p2_score * die.rolls}')
        break


    #player 2 goes
    #Player 2 rolls 4+5+6 and moves to space 3 for a total score of 3.
    print (f'Player 2 rolls ', end='')
    rolls = [die.roll() for i in range(3)]
    print (f'{rolls}', end='')
    move = sum(rolls)
    p2_pos = ((p2_pos + move) % 10)
    print (f' and moves to space {p2_pos} for a total score of ', end='')
    p2_score = p2_score + p2_pos
    print(f'{p2_score}.')
    if p2_score >= finish_score:
        print(f'Player 2 WINS\nP1 Score: {p1_score}\nP2 Score: {p2_score}\nDice Rolls: {die.rolls}')
        print(f'Game Score: {p2_score * die.rolls}')
        break