def get_card_informations(card):
    card_infos = card.split()
    card_number = int(card_infos[1].replace(':', ''))
    winning_numbers = card_infos[2:card_infos.index('|')]
    own_numbers = card_infos[card_infos.index('|') + 1:]

    winning_numbers = set(map(int, winning_numbers))
    own_numbers = set(map(int, own_numbers))
    return card_number, winning_numbers, own_numbers


def get_collection_card(card_list: list) -> dict:
    card_collection = {i: 1 for i in range(1, len(card_list) + 1)}
    for card in card_list:
        card_number, winning_numbers, own_numbers = get_card_informations(card)
        number_matching = len(winning_numbers.intersection(own_numbers))
        for i in range(card_number + 1, card_number + number_matching + 1):
            card_collection[i] += card_collection[card_number]
    return card_collection


def get_number_of_cards(card_collection: dict) -> int:
    return sum(card_collection.values())


# --- Example B ---
example = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]

print("Example B:", get_number_of_cards(get_collection_card(example)))

# --- Problem B ---
with open("input_day_4.txt", 'r') as file:
    data = file.read()
lines = data.split('\n')
print("Problem B:", get_number_of_cards(get_collection_card(lines)))
