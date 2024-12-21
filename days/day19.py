import time
import os


def part1(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here

    towels_str, combis_str = input_str.strip().split("\n\n")

    towels = set(towels_str.strip().split(", "))
    combis = [line for line in combis_str.splitlines()]

    # print(combis)
    # print(towels)

    def is_possible(combo):
        dp = [False] * (len(combo) + 1)
        dp[0] = True  # base case: empty combo, can be formed always

        # cut-off invalids
        argm = set(s for s in towels if s in combo)

        for i in range(1, len(combo) + 1):
            # try every pattern:
            for tow in argm:
                if i >= len(tow) and combo[i - len(tow) : i] == tow:
                    if dp[i - len(tow)]:
                        dp[i] = True
                        break

        # last element shows if combo could be formed by available towels
        # print(dp)
        return dp[len(combo)]

    # check if towel combi is possible
    result = 0
    i = 0
    for comb in combis:
        i += 1
        # print(f"i={i}")
        if is_possible(comb):
            # print("valid!")
            result += 1

    print(f"Part 1 result is: {result}")

    end_time = time.time()
    print(f"Part 1 execution time: {end_time - start_time} seconds")
    # too high 280


def part2(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 2:")
    # Implement the logic here
    # Your part2 logic here

    towels_str, combis_str = input_str.strip().split("\n\n")

    towels = set(towels_str.strip().split(", "))
    combis = [line for line in combis_str.splitlines()]

    # print(combis)
    # print(towels)

    def get_variants(combo):
        # dp = [[] for _ in range(len(combo) + 1)]
        dp = [0] * (len(combo) + 1)

        # dp[0] = [[]]  # base case: empty combo, can be formed always
        dp[0] = 1

        # cut-off invalids
        argm = set(s for s in towels if s in combo)

        for i in range(1, len(combo) + 1):
            # Early exit if dp[i] is already populated (no need to process it further)
            # if dp[i]:
            #    continue
            # try every pattern:
            for tow in argm:
                if i >= len(tow) and combo[i - len(tow) : i] == tow:
                    # for prev_vari in dp[i - len(tow)]:
                    # dp[i].append(prev_vari + [combo])
                    dp[i] += dp[i - len(tow)]

                    # Since we are adding valid patterns, we can break early
                    # break

        # last element shows if combo could be formed by available towels
        # print(dp)
        return dp[len(combo)]

    # check if towel combi is possible
    result = 0

    all_varis = {}
    for comb in combis:
        all_varis[comb] = get_variants(comb)

    # print(all_varis)
    for combo, vari_list in all_varis.items():
        result += vari_list
        # result += len(vari_list)

    print(f"Part 2 result is: {result}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")


# too low 246
