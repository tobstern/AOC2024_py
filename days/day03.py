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
    pattern = r"do\(\)|don't\(\)|mul\([0-9]{1,3}\,[0-9]{1,3}\)"

    result = 0
    all_instructs = re.findall(pattern, input_str)
    print(all_instructs)
    state = 1
    for item in all_instructs:
        print(item)
        if item == "do()":
            state = 1
        elif item == "don't()":
            state = 0
        else:
            if state:
                left = re.findall(r"([0-9]{1,3}),", item)[0]
                right = re.findall(r",([0-9]{1,3})", item)[0]
                print(left, right)
                result += int(left) * int(right)

    print(f"Part 2 result is: {result}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")


# 1096683498 too high
