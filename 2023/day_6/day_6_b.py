def parsing_input(input_text: str) -> tuple:
    lines = input_text.splitlines()
    time = int("".join(lines[0].split()[1:]))
    distance = int("".join(lines[1].split()[1:]))
    return time, distance


def get_number_ways_to_beat_record(time: int, distance: int) -> int:
    number_ways = 0
    for holding_time in range(1, time):
        if (time - holding_time) * holding_time > distance:
            number_ways += 1
    return number_ways


print("--- Example ---")
example = """Time:      7  15   30
Distance:  9  40  200"""
print(get_number_ways_to_beat_record(*parsing_input(example)))

print("--- Problem B ---")
with open("input_day_6.txt", 'r') as file:
    data = file.read()
print(get_number_ways_to_beat_record(*parsing_input(data)))
