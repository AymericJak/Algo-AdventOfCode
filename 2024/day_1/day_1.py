example = """3   4
4   3
2   5
1   3
3   9
3   3"""

with open("input_day_1.txt", 'r') as file:
    data = [line.split() for line in file.read().strip().split("\n")]

# PART A

left_numbers = sorted([int(line[0]) for line in data])
right_numbers = sorted([int(line[1]) for line in data])
distances = 0

for index in range(len(right_numbers)):
    distances += abs(left_numbers[index] - right_numbers[index])

print(distances)