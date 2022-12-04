with open("day1.txt", 'r') as file:
    data = file.read()

otherData = data.split('\n')
elfes = {}
index = 1

for elem in otherData:
    if elem == '':
        index += 1
    else:
        if index in elfes:
            elfes[index] += int(elem)
        else:
            elfes[index] = int(elem)


print(max(elfes.values()))
#print(max(elfes, key=elfes.get))