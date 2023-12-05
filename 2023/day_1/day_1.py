def get_number(line: str) -> int:
    l_filtered = list(filter(lambda x: x.isdigit(), line))
    if len(l_filtered) == 0:
        return 0
    elif len(l_filtered) == 1:
        return int(l_filtered[0] + l_filtered[0])
    else:
        return int(l_filtered[0] + l_filtered[-1])


numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def get_number_v2(line: str) -> int:
    line = line.lower()
    list_nb = []

    if len(line) > 0:
        for i in range(len(line)):
            if line[i].isdigit():
                list_nb.append(line[i])
            if len(line) - i >= 3:
                if line[i:i + 3] in numbers:
                    list_nb.append(numbers[line[i:i + 3]])
            if len(line) - i >= 4:
                if line[i:i + 4] in numbers:
                    list_nb.append(numbers[line[i:i + 4]])
            if len(line) - i >= 5:
                if line[i:i + 5] in numbers:
                    list_nb.append(numbers[line[i:i + 5]])

    if len(list_nb) == 0:
        return 0
    elif len(list_nb) == 1:
        return int(str(list_nb[0]) + str(list_nb[0]))
    else:
        return int(str(list_nb[0]) + str(list_nb[-1]))


with open("input_day_1.txt", 'r') as file:
    data = file.read()

list_data = data.split('\n')

list_values = []
for input_line in list_data:
    list_values.append(get_number(input_line))
print("Version 1:", sum(list_values))

# -----
print("----")

list_values = []
for input_line in list_data:
    list_values.append(get_number_v2(input_line))
print("Version 2:", sum(list_values))
