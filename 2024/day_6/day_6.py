example = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

direction = {
    "^": (-1, 0),  # Haut
    "v": (1, 0),  # Bas
    "<": (0, -1),  # Gauche
    ">": (0, 1)  # Droite
}

with open("input_day_6.txt", 'r') as file:
    data = file.read()


# PART A


def next_guard_direction(guard: str) -> str:
    directions = ["^", ">", "v", "<"]
    current_index = directions.index(guard)
    return directions[(current_index + 1) % 4]


def do_one_step(map_str: str, guard: str) -> str:
    map_list = [list(row) for row in map_str.split("\n")]
    nb_row = len(map_list)
    nb_col = len(map_list[0])

    guard_index = map_str.index(guard)
    current_y, current_x = divmod(guard_index, nb_col + 1)

    dy, dx = direction[guard]
    while True:
        new_y, new_x = current_y + dy, current_x + dx
        if (new_y <= 0 or new_y > nb_col or new_x <= 0 or new_x >= nb_row or current_y in {nb_col - 1, 0}
                or current_x in {nb_row - 1, 0}):
            break
        if map_list[new_y][new_x] == "#":
            break

        map_list[current_y][current_x] = "X"
        map_list[new_y][new_x] = next_guard_direction(guard)
        current_y, current_x = new_y, new_x

    return "\n".join("".join(row) for row in map_list)


def calculate_distinct_positions(map_str: str) -> int:
    return map_str.count("X") + 1


def execute_all_steps(map_str: str, guard: str) -> str:
    while True:
        new_map = do_one_step(map_str, guard)
        if new_map == map_str:  # If the map don't change, guard is locked
            break
        map_str = new_map
        guard = next_guard_direction(guard)
    return map_str


final_map = execute_all_steps(example, "^")
print("Example :", calculate_distinct_positions(final_map))  # 41

final_map = execute_all_steps(data, "^")
print("Part A answer :", calculate_distinct_positions(final_map))  # 5131
