import collections

example = """3   4
4   3
2   5
1   3
3   9
3   3"""

with open("input_day_1.txt", 'r') as file:
    # data = [line.split() for line in example.strip().split("\n")]
    data = [line.split() for line in file.read().strip().split("\n")]

# PART A

left_numbers = sorted([int(line[0]) for line in data])
right_numbers = sorted([int(line[1]) for line in data])
distances = 0

for index in range(len(left_numbers)):
    distances += abs(left_numbers[index] - right_numbers[index])

print("Part A answer :", distances)

# PART B

similarity_score = 0

for index in range(len(left_numbers)):
    counter = collections.Counter(right_numbers)
    similarity_score += left_numbers[index] * counter[left_numbers[index]]

print("Part B answer :", similarity_score)
