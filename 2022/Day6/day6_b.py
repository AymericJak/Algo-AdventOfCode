with open("day6.txt", 'r') as file:
    data = file.read()


def indexMarker(nb):
    index = 0
    for letterIndex in range(len(data) - 3):
        letters = [data[letterIndex + i] for i in range(nb)]
        if len(set(letters)) == len(letters):
            return index + nb
            break
        else:
            index += 1


print(indexMarker(14))
