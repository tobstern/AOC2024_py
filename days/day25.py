import time
import os


def parse_input(string):
    keys, locs = [], []
    for scheme in string.split("\n\n"):
        counts = [-1, -1, -1, -1, -1]
        is_key = False
        for i, line in enumerate(scheme.splitlines()):
            if i == 0 and "#" not in line:
                # it s a lock
                is_key = True

            for j, s in enumerate(line):
                if s == "#":
                    counts[j] += 1

        if is_key:
            keys.append(counts)
        else:
            locs.append(counts)
    return keys, locs


def part1(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here

    keys, locks = parse_input(input_str)
    # print(keys)
    # print(locks)

    result = 0
    for lock in locks:
        # test every key:
        for key in keys:
            keylocksum = [1 if k + l <= 5 else 0 for k, l in zip(key, lock)]

            if all(keylocksum):
                result += 1

    print(f"Part 1 result is: {result}")

    end_time = time.time()
    print(f"Part 1 execution time: {end_time - start_time} seconds")
