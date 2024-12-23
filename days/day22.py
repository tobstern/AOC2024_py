import time
import os


def mix(n, sn):
    return n ^ sn


def prune(sn):
    return sn % 16777216


def next_secret(sn):
    # n = sn * 64
    # sn = mix(n, sn)
    # sn = prune(sn)
    sn = ((sn * 64) ^ sn) % 16777216

    # n = sn // 32
    # sn = mix(n, sn)
    # sn = prune(sn)
    sn = ((sn // 32) ^ sn) % 16777216

    # n = sn * 2048
    # sn = mix(n, sn)
    # sn = prune(sn)
    sn = ((sn * 2048) ^ sn) % 16777216
    return sn


def part1(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here

    sec_nums = list(map(int, input_str.splitlines()))
    # print(sec_nums)

    nsn = []
    for r in range(2000):
        for num in sec_nums:
            nsn.append(next_secret(num))

        sec_nums = nsn
        nsn = []
        # print(sec_nums)
    # print(sec_nums)

    print(f"Part 1 result is: {sum(sec_nums)}")

    end_time = time.time()
    print(f"Part 1 execution time: {end_time - start_time} seconds")


def part2(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 2:")
    # Implement the logic here

    sec_nums = list(map(int, input_str.splitlines()))
    # print(sec_nums)

    # changes = {i: [] for i in range(len(sec_nums))}
    # buyers = []
    seq_totals = {}
    for num in sec_nums:
        nsn = [num % 10]
        for r in range(2000):
            num = next_secret(num)
            nsn.append(num % 10)
            # print(sn)

        seen = set()
        for i in range(len(nsn) - 4):
            a, b, c, d, e = nsn[i : i + 5]
            seq = (b - a, c - b, d - c, e - d)

            if seq in seen:
                continue
            seen.add(seq)

            if seq not in seq_totals:
                seq_totals[seq] = 0
            seq_totals[seq] += e

    result = max(seq_totals.values())

    # buyers.append(nsn)

    # print(buyers[0][:10])

    print(f"Part 2 result is: {result}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")
