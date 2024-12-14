import time
import os
import numpy as np


def parse_input(input_str):
    games = []
    for block in input_str.split("\n\n"):
        Xeq = []
        Yeq = []
        for line in block.splitlines():
            # split ": ", ", " -> left is X and right is Y
            xstr, ystr = line.split(": ")[1].strip().split(", ")
            # print(f"xstr={xstr} - ystr={ystr}")
            Xeq.append(int(xstr[2:]))
            Yeq.append(int(ystr[2:]))

        eqs = [Xeq[:-1], Yeq[:-1], [Xeq[-1], Yeq[-1]]]
        games.append(eqs)

    return games


def part1(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here

    games = parse_input(input_str)

    # print(games)

    result = 0

    # solve for each linear equation: 2x2
    # x = np.linalg.solve(a, b)
    tolerance = 1e-4
    for game in games:
        # print()
        a = np.array([game[0], game[1]])
        b = np.array(game[2])
        res = np.linalg.solve(a, b)
        # print(f"press A, B = {np.round(res, 10)} times")

        # print(
        #    f"is_valid: A_res={is_valid(round(res[0], 10))} - B_res={is_valid(round(res[1], 10))}"
        # )
        if (
            abs(res[0] - round(res[0])) < tolerance
            and abs(res[1] - round(res[1])) < tolerance
        ):
            result += 3 * round(res[0]) + round(res[1])

    print(f"Part 1 result is: {result}")

    end_time = time.time()
    print(f"Part 1 execution time: {end_time - start_time} seconds")


def part2(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 2:")
    # Implement the logic here

    games = parse_input(input_str)

    # print(games)

    result = 0

    # solve for each linear equation: 2x2
    # x = np.linalg.solve(a, b)
    tolerance = 1e-4
    for game in games:
        a = np.array([game[0], game[1]])
        b = np.array(game[2]) + 10000000000000
        # print(f"b_vec = {b}")
        res = np.linalg.solve(a, b)
        # print(f"press A, B = {round(res[0], 7)} times")
        # print(f"press A, B = {np.int64(res)} times")

        rounded_res = [round(res[0], 7), round(res[1], 7)]

        if (
            abs(res[0] - round(res[0])) < tolerance
            and abs(res[1] - round(res[1])) < tolerance
        ):
            result += 3 * rounded_res[0] + rounded_res[1]

    print(f"Part 2 result is: {int(result)}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")
