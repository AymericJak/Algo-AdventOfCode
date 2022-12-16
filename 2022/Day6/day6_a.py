with open("day6.txt", 'r') as file:
    data = file.read()

index = 0
for letterIndex in range(len(data) - 3):
    letters = [data[letterIndex], data[letterIndex + 1], data[letterIndex + 2], data[letterIndex + 3]]
    if len(set(letters)) == len(letters):
        print(index + 4)
        break
    else:
        index += 1
