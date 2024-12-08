with open("input_day_5.txt", 'r') as file:
    data = file.read()

# PART A

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


def filter_updates_order(rules: dict, data_second_section: list, is_correct: bool = True) -> list:
    """Filter updates validating rules corresponding to is_correct."""
    updates = []
    for update in data_second_section:
        update_row = list(map(int, update.split(",")))
        if check_update_order(rules, update_row) == is_correct:
            updates.append(update_row)
    return updates


def calculate_middle_pages_sum(updates: list) -> int:
    """Calculate sum of middle pages of valid updates."""
    return sum([update[len(update) // 2] for update in updates])


rules = generate_rules(data_first_section)
correct_updates = filter_updates_order(rules, data_second_section)
print("Part A answer :", calculate_middle_pages_sum(correct_updates))  # 4135


# PART B


def fix_update(rules: dict, incorrect_updates: list) -> list:
    """Fix incorrect updates."""
    fixed_updates = []

    for update in incorrect_updates:
        fixed_update = []
        for page in update:
            for i in range(len(fixed_update) + 1):
                # Check if update is still valid after insertion
                temp_update = fixed_update[:i] + [page] + fixed_update[i:]
                if check_update_order(rules, temp_update):
                    fixed_update = temp_update
                    break
        fixed_updates.append(fixed_update)
    return fixed_updates


incorrect_updates = filter_updates_order(rules, data_second_section, False)
fixed_updates = fix_update(rules, incorrect_updates)
print("Part B answer :", calculate_middle_pages_sum(fixed_updates))  # 5285
