import time
import os
import numpy as np


def part1(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here

    # calc diff 1st order
    result = 0
    for line in input_str.splitlines():
        nums = list(map(int, line.split(" ")))
        # print(nums)
        curr_diffs = [
            int((nums[i] - nums[i + 1]) / abs(nums[i] - nums[i + 1])) if 3 >= abs(nums[i] - nums[i + 1]) > 0 else 0
            for i in range(0, len(nums) - 1)
        ]
        # print(curr_diffs)
        result += 1 if abs(sum(curr_diffs)) == len(curr_diffs) else 0

    print(f"Part 1 result is: {result}")

    end_time = time.time()
    print(f"Part 1 execution time: {end_time - start_time} seconds")


def check_grad(nums, diffs):
    # check neighbouring gradients
    # where diffs are either 0 or changing
    # return 1 if all diffs are >0 and <=3 else 0
    for diff in diffs:
        if 0 < abs(diff) > 3:
            return 0
    return 1


def part2(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here

    result = 0
    for line in input_str.splitlines():
        nums = list(map(int, line.split(" ")))
        print(nums)
        curr_diffs = [
            (int((nums[i] - nums[i + 1]) / abs(nums[i] - nums[i + 1])) if 3 >= abs(nums[i] - nums[i + 1]) > 0 else 0)
            for i in range(0, len(nums) - 1)
        ]
        print(curr_diffs)

        safe = 1 if abs(sum(curr_diffs)) == len(curr_diffs) else 0

        if safe:
            result += 1
            print("safe first", result)
        else:
            # check if tolerable:
            curr_diffs = [
                (int(nums[i] - nums[i + 1]) if 3 >= abs(nums[i] - nums[i + 1]) > 0 else nums[i] - nums[i + 1])
                for i in range(0, len(nums) - 1)
            ]
            print(curr_diffs)
            result += check_grad(nums, curr_diffs)

        # result += 1 if abs(sum(curr_diffs)) == len(curr_diffs) else 0

    print(f"Part 2 result is: {result}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")


# 651 too low, 655
# 714, 716, 875 too high
