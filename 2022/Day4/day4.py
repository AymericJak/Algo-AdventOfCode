import re

data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

# PART A

l = data.split('\n')

with open("day4-a.txt", 'r') as file:
    data = [i for i in file.read().strip().split("\n")]


fullyContainsNumber = 0
for section in data:
    numbers = list(map(int,re.split('-|,', section)))
    assignment1 = [i for i in range(numbers[0], numbers[1]+1)]
    assignment2 = [i for i in range(numbers[2], numbers[3]+1)]

    if len(assignment1) >= len(assignment2):
        if all(number in assignment1 for number in assignment2):
            fullyContainsNumber += 1
    else:
        if all(number in assignment2 for number in assignment1):
            fullyContainsNumber += 1

print(fullyContainsNumber)