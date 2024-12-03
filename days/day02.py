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
            (int((nums[i] - nums[i + 1]) / abs(nums[i] - nums[i + 1])) if 3 >= abs(nums[i] - nums[i + 1]) > 0 else 0)
            for i in range(0, len(nums) - 1)
        ]
        # print(curr_diffs)
        result += 1 if abs(sum(curr_diffs)) == len(curr_diffs) else 0

    print(f"Part 1 result is: {result}")

    end_time = time.time()
    print(f"Part 1 execution time: {end_time - start_time} seconds")


def check_grad(nums):
    signs = [sign(nums[i] - nums[i + 1]) for i in range(0, len(nums) - 1)]
    diffs = [nums[i] - nums[i + 1] for i in range(0, len(nums) - 1)]
    # check neighbouring gradients
    # where diffs are either 0 or changing
    # return 1 if all diffs are >0 and <=3 else 0
    for diff in diffs:
        if abs(diff) > 3 or diff == 0:
            return 0

    if abs(sum(signs)) == len(signs):
        return 1
    else:
        return 0


def sign(num):
    if num < 0:
        return -1
    elif num == 0:
        return 0
    else:
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
            (sign(nums[i] - nums[i + 1]) if abs(nums[i] - nums[i + 1]) <= 3 else 0)(
                sign(nums[i] - nums[i + 1]) if abs(nums[i] - nums[i + 1]) <= 3 else 0
            )
            for i in range(0, len(nums) - 1)
        ]
        print(curr_diffs)

        safe = 1 if abs(sum(curr_diffs)) == len(curr_diffs) else 0

        if safe:
            result += 1
            print("safe first", result)
        else:

            # remove "the" wrong digit
            temp_res = 0
            for i in range(0, len(nums) - 1):
                corrected_nums = nums[:i] + nums[i + 1 :]
                temp_res = check_grad(corrected_nums, curr_diffs)

                if temp_res:
                    break

            result += temp_res

    print(f"Part 2 result is: {result}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")


# 651 too low, 655
# 709, 714, 716, 875 too high
