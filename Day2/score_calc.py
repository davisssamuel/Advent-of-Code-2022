# Part 1
# A and X = ROCK        (1 point)
# B and Y = PAPER       (2 points)
# C and Z = SCISSORS    (3 points) 
# 0 points for loss, 3 for draw, 6 for win

# Part 2
# A = ROCK        (1 point)
# B = PAPER       (2 points)
# C = SCISSORS    (3 points)
# X = LOSS
# Y = DRAW
# Z = WIN
# 0 points for loss, 3 for draw, 6 for win

SYMBOLS = {'X':'A', 'Y':'B', 'Z':'C'}
POINTS = {'A':1, 'B':2, 'C':3}
total = 0
with open("input.txt") as infile:
    data = infile.readlines()
    for line in data:
        round = line.strip().split(' ')
        
        # Part 1
        # round[1] = SYMBOLS[round[1]]
        # total += POINTS[round[1]]
        # if round[0]==round[1]:
        #     total += 3
        # if round[0]=='A' and round[1]=='B':
        #     total += 6
        # if round[0]=='B' and round[1]=='C':
        #     total += 6
        # if round[0]=='C' and round[1]=='A':
        #     total += 6

        # Part 2
        if round[1]=='X': # LOSE
            if round[0]=='A':
                total += 3 # 3 for playing scissors
            if round[0]=='B':
                total += 1
            if round[0]=='C':
                total += 2
        if round[1]=='Y': # DRAW
            total += 3 + POINTS[round[0]]
        if round[1]=='Z': # WIN
            if round[0]=='A':
                total += 8 # 2 for playing paper, 6 for winning
            if round[0]=='B':
                total += 9
            if round[0]=='C':
                total += 7

print(f"SCORE: {total}")
