import time
import os
from collections import Counter


def part1(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here

    # stone logic on pluto:
    nums_int = list(map(int, (input_str.split(" "))))
    # nums_str = input_str.split(" ")

    # print(nums_int)
    # print(nums_str)

    # stones = Counter(nums_str)
    stones = Counter(nums_int)
    # print(f"starting stones: {stones}")

    result = 0
    for blink in range(25):
        stones_copied = stones.copy()
        for digi in stones_copied.keys():
            for x in range(stones_copied[digi]):
                digi_str = str(digi)
                digi_len = len(str(digi))
                # print(f"digi_len={digi_len} - digi_str={digi_str}")
                if digi == 0:
                    stones[digi] -= 1
                    stones[1] += 1
                elif digi_len % 2 == 0:
                    # even len of digits
                    left = digi_str[: digi_len // 2]
                    right = digi_str[digi_len // 2 :]
                    # print(f"left={left} - right={right} - digi={digi}")
                    stones[int(left)] += 1
                    stones[int(right)] += 1
                    stones[digi] -= 1
                else:
                    stones[digi] -= 1
                    stones[digi * 2024] += 1

                # check if count is now 0 at digi, and drop this stone
                if stones[digi] == 0:
                    del stones[digi]

        # print(f"current stones: {stones}")

    # remove keys with 0 value from Counter
    # stones = Counter({k: v for k, v in stones.items() if v > 0})

    result = stones.total()

    print(f"Part 1 result is: {result}")

    end_time = time.time()
    print(f"Part 1 execution time: {end_time - start_time} seconds")


def part2(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 2:")
    # Implement the logic here

    nums_int = list(map(int, (input_str.split(" "))))
    # nums_str = input_str.split(" ")

    # print(nums_int)
    # print(nums_str)

    # stones = Counter(nums_str)
    stones = Counter(nums_int)
    # print(f"starting stones: {stones}")

    result = 0
    for blink in range(75):
        stones_copied = stones.copy()
        for digi in stones_copied.keys():
            # for x in range(stones_copied[digi]):
            digi_str = str(digi)
            digi_len = len(str(digi))

            same_stone_count = stones_copied[digi]
            # print(f"digi_len={digi_len} - digi_str={digi_str}")
            if digi == 0:
                stones[digi] -= same_stone_count
                stones[1] += same_stone_count
            elif digi_len % 2 == 0:
                # even len of digits
                left = digi_str[: digi_len // 2]
                right = digi_str[digi_len // 2 :]
                # print(f"left={left} - right={right} - digi={digi}")
                stones[int(left)] += same_stone_count
                stones[int(right)] += same_stone_count
                stones[digi] -= same_stone_count
            else:
                stones[digi] -= same_stone_count
                stones[digi * 2024] += same_stone_count

            # check if count is now 0 at digi, and drop this stone
            if stones[digi] == 0:
                del stones[digi]

        # print(f"current stones: {stones}")

    # remove keys with 0 value from Counter
    # stones = Counter({k: v for k, v in stones.items() if v > 0})

    result = stones.total()
    print(f"Part 2 result is: {result}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")
