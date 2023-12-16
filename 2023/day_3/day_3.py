example = ["467..114..",
           "...*......",
           "..35..633.",
           "......#...",
           "617*......",
           ".....+.58.",
           "..592.....",
           "......755.",
           "...$.*....",
           ".664.598.."]


def check_number(data_list: list, positions_list: list) -> bool:
    """Check if all positions in positions_list are not a point"""
    for position in positions_list:
        if data_list[position[0]][position[1]] != ".":
            return True
    return False


def get_positions_to_check(data_list: list, number_positions: list) -> list:
    """
    With a list of positions, return a list of positions to check. Positions to check are the positions around the number.

    :param data_list: the data list.
    :param number_positions: the positions of the number.
    :return: list of positions to check.
    """
    positions_to_check = []
    for position in number_positions:
        # HAUT
        if position[0] - 1 >= 0:
            positions_to_check.append((position[0] - 1, position[1]))
        # BAS
        if position[0] + 1 < len(data_list):
            positions_to_check.append((position[0] + 1, position[1]))
        # GAUCHE
        if position[1] - 1 >= 0:
            positions_to_check.append((position[0], position[1] - 1))
        # DROITE
        if position[1] + 1 < len(data_list[position[0]]):
            positions_to_check.append((position[0], position[1] + 1))

    # DIAGONALES
    # HAUT GAUCHE
    if number_positions[0][0] - 1 >= 0 and number_positions[0][1] - 1 >= 0:
        positions_to_check.append((number_positions[0][0] - 1, number_positions[0][1] - 1))
    # BAS GAUCHE
    if number_positions[0][0] + 1 < len(data_list) and number_positions[0][1] - 1 >= 0:
        positions_to_check.append((number_positions[0][0] + 1, number_positions[0][1] - 1))

    # HAUT DROITE
    if number_positions[-1][0] - 1 >= 0 and number_positions[-1][1] + 1 < len(data_list[number_positions[-1][0]]):
        positions_to_check.append((number_positions[-1][0] - 1, number_positions[-1][1] + 1))
    # BAS DROITE
    if number_positions[-1][0] + 1 < len(data_list) and number_positions[-1][1] + 1 < len(
            data_list[number_positions[-1][0]]):
        positions_to_check.append((number_positions[-1][0] + 1, number_positions[-1][1] + 1))

    # Remove from positions to check the positions present in number_positions
    positions_to_check = [position for position in positions_to_check if position not in number_positions]

    return positions_to_check


def get_sum_for_data_list(data_list: list) -> int:
    numbers_sum = 0
    for ligne in range(len(data_list)):
        number = ""
        number_positions = []
        for colonne in range(len(data_list[ligne])):
            if data_list[ligne][colonne].isdigit():
                number += data_list[ligne][colonne]
                number_positions.append((ligne, colonne))
            elif len(number_positions) > 0:
                position_to_check = get_positions_to_check(data_list, number_positions)
                if check_number(data_list, position_to_check):
                    numbers_sum += int(number)
                number = ""
                number_positions = []
    return numbers_sum


print("example:", get_sum_for_data_list(example))

with open("input_day_3.txt", 'r') as file:
    data = file.read()

lines = data.split('\n')[:-1]
print("problem A:", get_sum_for_data_list(lines))
