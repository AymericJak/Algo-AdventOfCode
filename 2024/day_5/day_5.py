example = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

with open("input_day_5.txt", 'r') as file:
    data = file.read()

# PART A

# data_first_section, data_second_section = example.split("\n\n")
data_first_section, data_second_section = data.split("\n\n")
data_first_section = data_first_section.split("\n")
data_second_section = data_second_section.split("\n")


def generate_rules(data_first_section: list) -> dict:
    """Generate rules from first section."""
    rules = {}
    for line in data_first_section:
        key, value = map(int, line.split("|"))
        rules.setdefault(key, set()).add(value)
    return rules


def check_update_order(rules: dict, updates: list) -> bool:
    """Check one update. It checks execution order is respected."""
    for index, current in enumerate(updates):
        previous, after = updates[:index], updates[index + 1:]
        for prev in previous:
            if prev in rules and current not in rules[prev]: return False
            if current in rules and prev in rules[current]: return False
        for aft in after:
            if current in rules and aft not in rules[current]: return False
    return True


def filter_all_updates_order(rules: dict, data_second_section: list) -> list:
    """Filter valid updates validating rules."""
    correct_updates = []
    for update in data_second_section:
        update_row = list(map(int, update.split(",")))
        if check_update_order(rules, update_row):
            correct_updates.append(update_row)
    return correct_updates


def calculate_middle_pages_sum(correct_updates: list) -> int:
    """Calculate sum of middle pages of valid updates."""
    return sum([update[len(update) // 2] for update in correct_updates])


rules = generate_rules(data_first_section)
correct_updates = filter_all_updates_order(rules, data_second_section)
print("Part A answer :", calculate_middle_pages_sum(correct_updates))  # 4135
