import re

example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

with open("input_day_3.txt", 'r') as file:
    data = file.read().strip()

# PART A

search_result = re.findall("mul\(\d+,\d+\)", data)
sum_multiplies = 0

for res in search_result:
    first_nb, second_nb = map(int, res[4:-1].split(","))
    sum_multiplies += first_nb * second_nb

print("Part A answer :", sum_multiplies)

# PART B

example_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

search_result = re.findall("mul\(\d+,\d+\)|do\(\)|don\'t\(\)", data)
sum_multiplies = 0
is_doing = True

for res in search_result:
    if res == "don't()":
        is_doing = False
    elif res == "do()":
        is_doing = True
    elif is_doing:
        first_nb, second_nb = map(int, res[4:-1].split(","))
        sum_multiplies += first_nb * second_nb

print("Part B answer :", sum_multiplies)
