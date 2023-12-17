def associate_time_distance(input_text: str) -> dict:
    lines = input_text.splitlines()
    times = [int(x) for x in lines[0].split()[1:]]
    distances = [int(x) for x in lines[1].split()[1:]]
    return dict(zip(times, distances))


def get_number_ways_to_beat_record(time: int, distance: int) -> int:
    number_ways = 0
    for holding_time in range(1, time):
        if (time - holding_time) * holding_time > distance:
            number_ways += 1
    return number_ways


def get_ways_multiplication(input_text: str) -> int:
    product = 1
    for time, distance in associate_time_distance(input_text).items():
        product *= get_number_ways_to_beat_record(time, distance)
    return product


print("--- Example ---")
example = """Time:      7  15   30
Distance:  9  40  200"""
print(get_ways_multiplication(example))

print("--- Problem A ---")
with open("input_day_6.txt", 'r') as file:
    data = file.read()
print(get_ways_multiplication(data))
