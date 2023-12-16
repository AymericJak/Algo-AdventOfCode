def get_card_informations(card):
    card_infos = card.split()
    card_number = int(card_infos[1].replace(':', ''))
    winning_numbers = card_infos[2:card_infos.index('|')]
    own_numbers = card_infos[card_infos.index('|') + 1:]

    winning_numbers = list(map(int, winning_numbers))
    own_numbers = list(map(int, own_numbers))
    return card_number, winning_numbers, own_numbers


def calculate_card_score(card: str) -> int:
    card_number, winning_numbers, own_numbers = get_card_informations(card)
    score = 0
    for number in own_numbers:
        if number in winning_numbers:
            if score == 0:
                score = 1
            else:
                score *= 2
    return score


def calculate_final_score(card_list: list) -> int:
    score = 0
    for card in card_list:
        score += calculate_card_score(card)
    return score


# --- Example ---
example = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]

print("Example A:", calculate_final_score(example))

# --- Problem A ---
with open("input_day_4.txt", 'r') as file:
    data = file.read()
lines = data.split('\n')
print("Problem A:", calculate_final_score(lines))
