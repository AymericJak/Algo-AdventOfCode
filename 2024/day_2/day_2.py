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



# PART A


nb_safe_reports = 0

for report in data:
    gaps = [a - b for a, b in itertools.pairwise(report)]

    if all(gap > 0 for gap in gaps) or all(gap < 0 for gap in gaps):
        if all([i in {nb for nb in range(-3, 4)} for i in gaps]):
            nb_safe_reports += 1

print("Part A answer :", nb_safe_reports)
