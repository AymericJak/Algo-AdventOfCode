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
    "A X": 4, #1 + 3
    "A Y": 8, #2 + 6
    "A Z": 3, #3 + 0
    "B X": 1, #1 + 0
    "B Y": 5, #2 + 3
    "B Z": 9, #3 + 6
    "C X": 7, #1 + 6
    "C Y": 2, #2 + 0
    "C Z": 6 #3 + 3
}

with open("day2-a.txt", 'r') as file:
    data = [i for i in file.read().strip().split("\n")]


for round in data:
    score_sum_a += round_scores.get(round)

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

for round in data:
    if round[2] == 'X':
        round = round[:2] + defeat.get(round[0])
    elif round[2] == 'Z':
        round = round[:2] + win.get(round[0])
    else:
        round = round[:2] + equal.get(round[0])

    score_sum_b += round_scores.get(round)

print(score_sum_b)