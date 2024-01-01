import re

example_1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

example_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""


def manage_rule(base_rule: str, rules: dict, instruction: str):
    if instruction == 'R':
        return rules[base_rule][1]
    elif instruction == 'L':
        return rules[base_rule][0]


def get_number_of_steps(_input: list):
    instructions = _input[0]
    base_rule = "AAA"
    rules = {}
    for rule in _input[2:]:
        matches = re.match(r'(\w+) = \((\w+), (\w+)\)', rule).groups()
        rules[matches[0]] = (matches[1], matches[2])
    is_find = False
    nb_steps = 0
    while not is_find:
        base_rule = manage_rule(base_rule, rules, instructions[nb_steps % len(instructions)])
        nb_steps += 1
        if base_rule == 'ZZZ':
            is_find = True
    return nb_steps


print("--- Example 1 | expected 2 ---")
print(get_number_of_steps(example_1.splitlines()))

print("--- Example 2 | expected 6 ---")
print(get_number_of_steps(example_2.splitlines()))

print("--- Problem A ---")
with open("input_day_8.txt", 'r') as file:
    data = file.read()
print(get_number_of_steps(data.splitlines()))
