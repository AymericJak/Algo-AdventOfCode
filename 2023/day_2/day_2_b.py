import re

game_scores = []


def get_game_score(line: str) -> None:
    parts = re.split(":|;", line)
    colors = {
        "blue": [],
        "red": [],
        "green": []
    }

    for part in parts[1:]:
        values = [elem.split() for elem in map(str.strip, part.split(","))]
        for number, color in values:
            colors[color].append(int(number))

    product = 1
    for numbers_list in colors.values():
        product *= max(numbers_list)
    return product


with open("input_day_2.txt", 'r') as file:
    data = file.read()

lines = data.split('\n')

for line in filter(None, lines):
    game_scores.append(get_game_score(line))

print(sum(game_scores))
