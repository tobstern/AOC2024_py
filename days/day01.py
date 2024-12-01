import time
import os
import unittest


def part1(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # print(input_str, "Hi")
    # Implement the logic here

    # get columns to list of integers
    left, right = [], []
    for line in input_str.splitlines():
        # print(line.split(" "))
        left.append(int(line.split(" ")[0].strip()))
        right.append(int(line.split(" ")[-1].strip()))

    # sort the numbers:
    # print(left, right)

    # Inline test for checking list population
    # input_str = "1 8\n2 7\n3 6\n4 5"
    # left, right = [], []
    # for line in input_str.splitlines():
    #     left.append(int(line.split(" ")[0].strip()))
    #     right.append(int(line.split(" ")[-1].strip()))
    # assert left == [1, 2, 3, 4], f"Expected [1, 2, 3, 4], but got {left}"
    # assert right == [8, 7, 6, 5], f"Expected [8, 7, 6, 5], but got {right}"

    sorted_left = sorted(left)
    sorted_right = sorted(right)

    results = [abs(l - r) for l, r in zip(sorted_left, sorted_right)]
    result = sum(results)

    print(f"Part 1 result is: {result}")

    end_time = time.time()
    print(f"Part 1 execution time: {end_time - start_time} seconds")


def part2(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here

    # get columns to list of integers
    left, right = [], []
    for line in input_str.splitlines():
        # print(line.split(" "))
        left.append(int(line.split(" ")[0].strip()))
        right.append(int(line.split(" ")[-1].strip()))

    # count the appearances of numbers in a HashMap/dict
    right_counts = dict()
    for ele in right:
        occ = right_counts.get(ele, None)
        if occ:
            right_counts[ele] += 1
        else:
            right_counts[ele] = 1

    # now lookup if and how many of left in right
    result = 0
    for ele in left:
        occ = right_counts.get(ele, None)
        if occ:
            result += ele * occ

    print(f"Part 2 result is: {result}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")
