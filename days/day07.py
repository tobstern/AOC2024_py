import time
import os

# from itertools import combinations_with_replacement as combswr
import itertools


def part1(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here

    result = []
    for line in input_str.splitlines():
        val = int(line.split(": ")[0].strip())
        nums = list(map(int, line.split(": ")[1].split(" ")))

        # print(val, nums)
        # print()
        # print(f"value {val} - numbers {nums}")

        # check combs of ops to get to val, if no comb results in it, do not sum this
        len_of_combs = len(nums) - 1

        str_of_ops = ["*", "+"]
        # str_of_ops = "+*"

        inter_res = []
        valid = False

        permutations = list(itertools.product(str_of_ops, repeat=len_of_combs))
        # for perm in permutations(str_of_ops):
        # print(list(combswr(str_of_ops, len_of_combs)))
        for perm in permutations:
            # print(f"perm {perm} - len_of_combs {len_of_combs}")

            perm_sum = nums[0]
            # perm_sum = 0
            for i, ch in enumerate(perm):
                # calc result:
                if ch == "+":
                    perm_sum += nums[i + 1]
                else:
                    # ch == *
                    if perm_sum == 0:
                        perm_sum = nums[i + 1]
                    else:
                        perm_sum *= nums[i + 1]

            inter_res.append(perm_sum)

            if perm_sum == val:
                # result matches the cal_value
                # print("This is valid!")
                valid = True
                result.append(val)

                break

    # print(f"resulting calibration values: {result}")
    print(f"Part 1 result is: {sum(result)}")

    end_time = time.time()
    print(f"Part 1 execution time: {end_time - start_time} seconds")


def part2(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here
    # Your part2 logic here

    result = []
    for line in input_str.splitlines():
        val = int(line.split(": ")[0].strip())
        nums = list(map(int, line.split(": ")[1].split(" ")))

        # print(val, nums)
        # print()
        # print(f"value {val} - numbers {nums}")

        # check combs of ops to get to val, if no comb results in it, do not sum this
        len_of_combs = len(nums) - 1

        str_of_ops = ["*", "+", "||"]
        # str_of_ops = "+*"

        inter_res = []
        valid = False

        permutations = list(itertools.product(str_of_ops, repeat=len_of_combs))
        # for perm in permutations(str_of_ops):
        # print(list(combswr(str_of_ops, len_of_combs)))
        for perm in permutations:
            # print(f"perm {perm} - len_of_combs {len_of_combs}")

            perm_sum = nums[0]
            # perm_sum = 0
            for i, ch in enumerate(perm):
                # calc result:
                if ch == "+":
                    perm_sum += nums[i + 1]
                elif ch == "||":
                    # combine numbers -> concat strings
                    # print(
                    #     f"perm_sum={perm_sum} - num={nums[i+1]} - res_str={str(perm_sum) + str(nums[i + 1])}"
                    # )
                    perm_sum = int(str(perm_sum) + str(nums[i + 1]))
                else:
                    # ch == *
                    if perm_sum == 0:
                        perm_sum = nums[i + 1]
                    else:
                        perm_sum *= nums[i + 1]

            inter_res.append(perm_sum)

            if perm_sum == val:
                # result matches the cal_value
                # print("This is valid!")
                valid = True
                result.append(val)

                break

    print(f"Part 2 result is: {sum(result)}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")
