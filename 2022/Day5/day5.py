import sys

data = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

with open("day5-a.txt", 'r') as file:
    data = [i for i in file.read().split("\n")]

class Pile:
    def __init__(self, maxSize=None):
        self.items = []
        self.MAX_SIZE = sys.maxsize if maxSize is None else maxSize

    def add(self, item):
        if type(item) is list:
            for it in item:
                if len(self.items) < self.MAX_SIZE:
                    self.items.append(it)
                else:
                    break
        else:
            if len(self.items) < self.MAX_SIZE:
                self.items.append(item)
            else:
                raise IndexError("Full stack")

    def nextItemPop(self):
        return self.items[-1]

    def pop(self):
        if len(self.items) <= 0:
            raise IndexError('pile vide')
        self.items.pop(-1)

    def isEmpty(self):
        return len(self.items) == 0

    def length(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

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
