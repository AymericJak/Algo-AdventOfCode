import itertools

example = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

with open("input_day_2.txt", 'r') as file:
    # data = [list(map(int, line.split())) for line in example.strip().split("\n")]
    data = [list(map(int, line.split())) for line in file.read().strip().split("\n")]


def is_valid_report(report):
    gaps = [a - b for a, b in itertools.pairwise(report)]

    if (all(gap > 0 for gap in gaps) or all(gap < 0 for gap in gaps)) and all(abs(gap) <= 3 and gap != 0 for gap in gaps):
        return True
    return False


# PART A


nb_safe_reports = 0

for report in data:
    if is_valid_report(report):
        nb_safe_reports += 1

print("Part A answer :", nb_safe_reports)


# PART B


nb_safe_reports = 0

for report in data:
    if is_valid_report(report):
        nb_safe_reports += 1
    else:
        for i in range(len(report)):
            modified_report = report[:i] + report[i+1:]
            if is_valid_report(modified_report):
                nb_safe_reports += 1
                break

print("Part B answer :", nb_safe_reports)
