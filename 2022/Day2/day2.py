# A --> Rock
# B --> Paper
# C --> Scissors

# X --> Rock 1
# Y --> Paper 2
# Z --> Scissors 3

# 0 if you lost, 3 if the round was a draw, and 6 if you won

# Part A
score_sum_a = 0

round_scores = {
    "A X": 4,  # 1 + 3
    "A Y": 8,  # 2 + 6
    "A Z": 3,  # 3 + 0
    "B X": 1,  # 1 + 0
    "B Y": 5,  # 2 + 3
    "B Z": 9,  # 3 + 6
    "C X": 7,  # 1 + 6
    "C Y": 2,  # 2 + 0
    "C Z": 6  # 3 + 3
}

with open("day2.txt", 'r') as file:
    data = [i for i in file.read().strip().split("\n")]

for gameRound in data:
    score_sum_a += round_scores.get(gameRound)

print(score_sum_a)

# Part B

# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.

score_sum_b = 0

win = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

defeat = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

equal = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

for gameRound in data:
    if gameRound[2] == 'X':
        gameRound = gameRound[:2] + defeat.get(gameRound[0])
    elif gameRound[2] == 'Z':
        gameRound = gameRound[:2] + win.get(gameRound[0])
    else:
        gameRound = gameRound[:2] + equal.get(gameRound[0])

    score_sum_b += round_scores.get(gameRound)

print(score_sum_b)
