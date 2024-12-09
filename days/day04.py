import time
import os
import numpy as np


def word_search(grid, word):
    max_row = len(grid)
    max_col = len(grid[0])
    word_len = len(word)
    counter = 0

    def check_word_in_line(line):
        return line.count(word)

    # Check horizontal and reverse horizontal
    for row in grid:
        line = "".join(row)
        counter += check_word_in_line(line)
        counter += check_word_in_line(line[::-1])

    # Check vertical and reverse vertical
    for col in range(max_col):
        line = "".join(grid[row][col] for row in range(max_row))
        counter += check_word_in_line(line)
        counter += check_word_in_line(line[::-1])

    # Check diagonal (top-left to bottom-right) and reverse diagonal
    for start in range(max_row + max_col - 1):
        line = "".join(grid[i][start - i] for i in range(max_row) if 0 <= start - i < max_col)
        counter += check_word_in_line(line)
        counter += check_word_in_line(line[::-1])

    # Check diagonal (bottom-left to top-right) and reverse diagonal
    for start in range(-max_row + 1, max_col):
        line = "".join(grid[i][i - start] for i in range(max_row) if 0 <= i - start < max_col)
        counter += check_word_in_line(line)
        counter += check_word_in_line(line[::-1])

    return counter


def cross_mas_search(grid):
    max_row = len(grid)
    max_col = len(grid[0])
    counter = 0

    words = ["MAS", "SAM"]
    # Check horizontal and reverse horizontal
    for i, row in zip(range(1, len(grid) - 1), grid[1:-1, :]):
        for j, ch in zip(range(1, len(row) - 1), row[1:-1]):

            diag1 = grid[i - 1, j - 1] + grid[i, j] + grid[i + 1, j + 1]
            diag2 = grid[i + 1, j - 1] + grid[i, j] + grid[i - 1, j + 1]

            if diag1 in words and diag2 in words:
                # found an X-MAS (MAS cross)
                counter += 1

    return counter


def part1(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here

    word = "XMAS"
    word_map = []
    for i, line in enumerate(input_str.splitlines()):
        # print(list(line))
        word_map.append(list(line))

    np_word_map = np.asarray(word_map)
    # print(np_word_map)

    # loop rows, transpose and loop columns (then they are rows) - also reverse

    # exec all of them
    result = word_search(np_word_map, word)

    print(f"Part 1 result is: {result}")

    end_time = time.time()
    print(f"Part 1 execution time: {end_time - start_time} seconds")


def part2(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 2:")
    # Implement the logic here
    # Your part2 logic here

    word = "MAS"
    word_map = []
    for i, line in enumerate(input_str.splitlines()):
        # print(list(line))
        word_map.append(list(line))

    np_word_map = np.asarray(word_map)
    # print(np_word_map)

    # loop rows, transpose and loop columns (then they are rows) - also reverse

    # exec all of them
    result = cross_mas_search(np_word_map)

    print(f"Part 2 result is: {result}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")
