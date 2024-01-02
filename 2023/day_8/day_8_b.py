import re
import time
from itertools import cycle

example = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


def get_number_steps_v2(_input: list):
    instructions = _input[0]
    start_nodes = []
    rules = {}
    for rule in _input[2:]:
        matches = re.match(r'(\w+) = \((\w+), (\w+)\)', rule).groups()
        rules[matches[0]] = (matches[1], matches[2])
        if matches[0].endswith('A'):
            start_nodes.append(matches[0])

    all_ends_with_z = False
    nb_steps = 0

    start_time = time.time()

    instructions_cycle = cycle(instructions)
    while not all_ends_with_z and nb_steps < 10_000_000:
        current_instruction = next(instructions_cycle)
        start_nodes = [rules[node][1 if current_instruction == 'R' else 0] for node in start_nodes]

        nb_steps += 1

        all_ends_with_z = True
        for node in start_nodes:
            if not node.endswith('Z'):
                all_ends_with_z = False
                break

    end_time = time.time()
    elapsed_time_1_million = end_time - start_time
    estimation_14_billions = (elapsed_time_1_million / 10_000_000) * 14_000_000_000

    print(f"Le temps estimé pour 14 milliards d'itérations est d'environ {estimation_14_billions / 60} minutes.")

    return nb_steps


print("--- Example 1 | expected 6 ---")
print(get_number_steps_v2(example.splitlines()))

print("--- Problem B ---")
with open("input_day_8.txt", 'r') as file:
    data = file.read()
print(get_number_steps_v2(data.splitlines()))
