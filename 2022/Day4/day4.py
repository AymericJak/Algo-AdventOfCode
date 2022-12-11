import re

with open("day4.txt", 'r') as file:
    data = [i for i in file.read().strip().split("\n")]

# PART A

fullyContainsNumber = 0
for section in data:
    numbers = list(map(int, re.split('-|,', section)))
    assignment1 = [i for i in range(numbers[0], numbers[1] + 1)]
    assignment2 = [i for i in range(numbers[2], numbers[3] + 1)]

    if len(assignment1) >= len(assignment2):
        if all(number in assignment1 for number in assignment2):
            fullyContainsNumber += 1
    else:
        if all(number in assignment2 for number in assignment1):
            fullyContainsNumber += 1

print(fullyContainsNumber)

# PART B

overlappingAssignment = 0
for section in data:
    numbers = list(map(int, re.split('-|,', section)))
    assignment1 = [i for i in range(numbers[0], numbers[1] + 1)]
    assignment2 = [i for i in range(numbers[2], numbers[3] + 1)]

    if len(assignment1) >= len(assignment2):
        for elem in assignment2:
            if elem in assignment1:
                overlappingAssignment += 1
                break
    else:
        for elem in assignment1:
            if elem in assignment2:
                overlappingAssignment += 1
                break

print(overlappingAssignment)
