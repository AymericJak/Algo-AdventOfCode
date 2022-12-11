from Pile import Pile

with open("day5.txt", 'r') as file:
    data = [i for i in file.read().split("\n")]
index = 0
while data[index] != '':
    index += 1
allStacks = []
for i in range(index - 1, -1, -1):
    if i == (index - 1):
        numberOfStacks = int(data[i].strip()[-1])
        for _ in range(numberOfStacks):
            allStacks.append(Pile())
    else:
        idx = 0
        for j in range(1, numberOfStacks * 4, 4):
            if data[i][j] != ' ':
                allStacks[idx].add(data[i][j])
            idx += 1

for line in range(index + 1, len(data)):
    values = data[line].split()

    nbIterations = int(values[1])
    fromIndex = int(values[3]) - 1
    toIndex = int(values[5]) - 1

    for _ in range(nbIterations):
        nb = allStacks[fromIndex].nextItemPop()
        allStacks[fromIndex].pop()
        allStacks[toIndex].add(nb)

message = ''
for stack in allStacks:
    message += stack.nextItemPop()

print(message)
