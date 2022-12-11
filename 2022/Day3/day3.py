import string

with open("day3.txt", 'r') as file:
    data = [i for i in file.read().strip().split("\n")]

# PART A

lettersValue = {letter: i + 1 for i, letter in enumerate(string.ascii_letters)}
commonLetters = []

for item in data:
    itemLength = int(len(item) / 2)
    part1 = set(item[0:itemLength])
    part2 = set(item[itemLength:])
    commonLetters.append(part1.intersection(part2).pop())

somme = 0
for letter in commonLetters:
    somme += lettersValue.get(letter)

print(somme)

# PART B

commonLetters2 = []

for index, item in enumerate(data):
    index += 1
    item = set(item)

    if index % 3 == 1:
        liste = [item]
    elif index % 3 == 2:
        liste.append(item)
    elif index % 3 == 0:
        liste.append(item)
        commonLetters2.append((liste[0] & liste[1] & liste[2]).pop())

sommeB = 0
for letter in commonLetters2:
    sommeB += lettersValue.get(letter)

print(sommeB)
