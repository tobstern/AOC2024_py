import time
import os
import numpy as np


def word_search(grid, word, counter):
    # loop left to right and right-down diagonal:
    (max_row, max_col) = grid.shape
    # print(max_row, max_col)
    for i, line in enumerate(grid):
        char_stack = ""
        char_stack_diag = ""

        # right
        for j, ch in enumerate(line):
            # collect next char till it contains 'XMAS'
            char_stack += ch
            if word in char_stack:
                # if included, count and clear stack
                counter += 1
                char_stack = ""

                # diagonal: right-down
                # chec for bounds
                if i == 0:
                    for l in range(0, max_row):
                        if 0 <= i + l < max_row and 0 <= j + l < max_col:
                            curr_char = grid[i + l, j + l]
                            char_stack_diag += curr_char

                            if word in char_stack:
                                # if included, count and clear stack
                                counter += 1
                                char_stack_diag = ""
                        else:
                            char_stack_diag = ""
                            break

                    else:
                        char_stack_diag = ""

        else:
            char_stack = ""

        if j == 0 and i > 0:
            for l in range(0, max_col):
                if 0 <= i + l < max_row and 0 <= j + l < max_col:
                    curr_char = grid[i + l, j + l]
                    char_stack_diag += curr_char

                    if word in char_stack:
                        # if included, count and clear stack
                        counter += 1
                        char_stack_diag = ""
                else:
                    char_stack_diag = ""
                    break

            else:
                char_stack_diag = ""
    # implement logic for searching diagonal

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
    print(np_word_map)

    # loop rows, transpose and loop columns (then they are rows) - also reverse

    # modify word map:
    all_word_maps = [
        np_word_map,
        np.transpose(np_word_map),
        np.fliplr(np_word_map),
        np.fliplr(np.transpose(np_word_map)),
    ]

    # exec all of them
    counter = 0
    for grid in all_word_maps:
        counter += word_search(grid, word, counter)

    print(f"Part 1 result is: {counter}")

    end_time = time.time()
    print(f"Part 1 execution time: {end_time - start_time} seconds")


def part2(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here
    # Your part2 logic here

    result = ""
    print(f"Part 2 result is: {result}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")
