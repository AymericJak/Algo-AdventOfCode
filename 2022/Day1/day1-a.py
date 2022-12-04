from collections import Counter

# Part A
with open("day1.txt", 'r') as file:
    data = file.read()

listData = data.split('\n')
elfes = {}
index = 1

for elem in listData:
    if elem == '':
        index += 1
    else:
        if index in elfes:
            elfes[index] += int(elem)
        else:
            elfes[index] = int(elem)

print(max(elfes.values()))

# Part B

max_values = Counter(elfes).most_common(3)

sum_max_values = 0
for i in max_values:
    sum_max_values += i[1]

print(sum_max_values)