# A --> Rock
# B --> Paper
# C --> Scissors

# X --> Rock 1
# Y --> Paper 2
# C --> Scissors 3

# 0 if you lost, 3 if the round was a draw, and 6 if you won

score_sum = 0

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
    score_sum += round_scores.get(round)

print(score_sum)
