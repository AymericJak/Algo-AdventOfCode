import re

colors_requirements = {
    "red": 12,
    "green": 13,
    "blue": 14
}

id_lists = []


def check_game_and_update_id_list(line: str) -> None:
    parts = re.split(":|;", line)
    game_id = parts[0].split()[1]

    for part in parts[1:]:
        values = [elem.split() for elem in map(str.strip, part.split(","))]
        for number, color in values:
            if int(number) > colors_requirements[color]:
                return
    id_lists.append(int(game_id))


with open("input_day_2.txt", 'r') as file:
    data = file.read()

lines = data.split('\n')

for line in filter(None, lines):
    check_game_and_update_id_list(line)

print(sum(id_lists))
