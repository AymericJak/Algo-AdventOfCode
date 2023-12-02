def get_number(line: str) -> int:
    l_filtered = list(filter(lambda x: x.isdigit(), line))
    if len(l_filtered) == 0:
        return 0
    elif len(l_filtered) == 1:
        return int(l_filtered[0] + l_filtered[0])
    else:
        return int(l_filtered[0] + l_filtered[-1])


with open("input_day_1.txt", 'r') as file:
    data = file.read()

list_data = data.split('\n')
list_values = []

for input_line in list_data:
    list_values.append(get_number(input_line))

print(sum(list_values))
