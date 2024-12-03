import time
import os
import re


def part1(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here

    # regex matching mul(xxx,xxx) - can be 1-3 digits left and right
    result = 0
    for line in input_str.splitlines():
        # print([int(left) * int(right) for left, right in re.findall(r"mul\(([0-9]{1,3})\,([0-9]{1,3})\)", line)])
        result += sum(
            [int(left) * int(right) for left, right in re.findall(r"mul\(([0-9]{1,3})\,([0-9]{1,3})\)", line)]
        )

    print(f"Part 1 result is: {result}")

    end_time = time.time()
    print(f"Part 1 execution time: {end_time - start_time} seconds")


def part2(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here
    # Your part2 logic here

    # regex matching mul(xxx,xxx) - can be 1-3 digits left and right
    result = 0
    # print([int(left) * int(right) for left, right in re.findall(r"mul\(([0-9]{1,3})\,([0-9]{1,3})\)", line)])
    all_instructs = re.findall(r"(do\(\)|don\(\)|mul\([0-9]{1,3}\,[0-9]{1,3}\))*", input_str)
    print(all_instructs)
    # reg_res = all_instructs.group()
    # print(reg_res)

    # check if do()|don't() -> switch on|off sum
    switch = 1
    # for instr in all_instructs:
    #    print(instr)

    print(f"Part 2 result is: {result}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")


# 1096683498 too high
