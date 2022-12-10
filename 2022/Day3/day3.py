import string

with open("day3-a.txt", 'r') as file:
    data = [i for i in file.read().strip().split("\n")]

# PART A

commonLetters = []

for item in data:
    itemLength = int(len(item)/2)
    part1 = set(item[0:itemLength])
    part2 = set(item[itemLength:])
    commonLetters.append(part1.intersection(part2).pop())

lettersValue = {letter:i+1 for i,letter in enumerate(string.ascii_letters)}

somme = 0
for letter in commonLetters:
    somme += lettersValue.get(letter)

print(somme)