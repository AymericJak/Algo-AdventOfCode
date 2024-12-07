import re
import numpy as np

should_4 = """..X...
.SAMX.
.A..A.
XMAS.S
.X...."""

example = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

with open("input_day_4.txt", 'r') as file:
    data = file.read()


# PART A

def count_word(text: str, word: str) -> int:
    return len(re.findall(word, text)) + len(re.findall(word[::-1], text))


def search_horizontaly(text: str) -> int:
    return count_word(text, "XMAS")


def search_verticaly(text: str) -> int:
    rows = text.split("\n")
    numpy_matrix = np.array([list(row) for row in rows])
    transposed_matrix = numpy_matrix.T

    transposed_text = "\n".join("".join(row) for row in transposed_matrix)
    return count_word(transposed_text, "XMAS")


def search_diagonaly(text: str) -> int:
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
    return count_word(diagonal_text, "XMAS")


def calculate_xmas_occurs(text: str) -> int:
    return (
            search_horizontaly(text)
            + search_verticaly(text)
            + search_diagonaly(text)
    )


print("should_4 :", calculate_xmas_occurs(should_4))
print("example_shoul_18 :", calculate_xmas_occurs(example))
print("Part A answer :", calculate_xmas_occurs(data))
