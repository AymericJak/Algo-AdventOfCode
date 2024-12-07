import re
import numpy as np

with open("input_day_4.txt", 'r') as file:
    data = file.read()


# PART A

def count_word(text: str, word: str) -> int:
    return len(re.findall(word, text)) + len(re.findall(word[::-1], text))


def search_horizontaly(text: str, word: str) -> int:
    return count_word(text, word)


def search_verticaly(text: str, word: str) -> int:
    rows = text.split("\n")
    numpy_matrix = np.array([list(row) for row in rows])
    transposed_matrix = numpy_matrix.T

    transposed_text = "\n".join("".join(row) for row in transposed_matrix)
    return count_word(transposed_text, word)


def search_diagonaly(text: str, word: str) -> int:
    rows = text.split("\n")
    numpy_matrix = np.array([list(row) for row in rows])

    diagonals = [
        "".join(numpy_matrix.diagonal(offset))
        for offset in range(-numpy_matrix.shape[0] + 1, numpy_matrix.shape[1])
    ]

    flipped_matrix = np.fliplr(numpy_matrix)
    diagonals += [
        "".join(flipped_matrix.diagonal(offset))
        for offset in range(-flipped_matrix.shape[0] + 1, flipped_matrix.shape[1])
    ]

    diagonal_text = "\n".join(diagonals)
    return count_word(diagonal_text, word)


def calculate_word_occurs(text: str, word: str) -> int:
    return (
            search_horizontaly(text, word)
            + search_verticaly(text, word)
            + search_diagonaly(text, word)
    )


print("Part A answer :", calculate_word_occurs(data, "XMAS"))


# PART B

def calculte_cross_mas(text: str) -> int:
    count = 0
    text_array = text.split("\n")
    patterns = {
        ("M", "M", "S", "S"),
        ("S", "S", "M", "M"),
        ("M", "S", "M", "S"),
        ("S", "M", "S", "M"),
    }

    for y in range(1, len(text_array) - 1):
        for x in range(1, len(text_array[y]) - 1):
            if text_array[x][y] == "A":
                top_left = text_array[x - 1][y - 1]
                bottom_left = text_array[x + 1][y - 1]
                top_right = text_array[x - 1][y + 1]
                bottom_right = text_array[x + 1][y + 1]

                if (top_left, top_right, bottom_left, bottom_right) in patterns:
                    count += 1

    return count


print("Part B answer :", calculte_cross_mas(data))
