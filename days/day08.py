import time
import os
import numpy as np


def append2dict(d, k, v):
    if d.get(k) == None:
        d[k] = [v]
    else:
        d[k].append(v)
    return d


def get_all_pairs(list_of_poss):
    pairs = []
    for i, pos in enumerate(list_of_poss):
        for j in range(len(list_of_poss)):
            pair = (pos, list_of_poss[j])
            if pair != (pos, pos) and (list_of_poss[j], pos) not in pairs:
                pairs.append(pair)

    return pairs


def distances(pairs):
    dists = []
    for left, right in pairs:
        # one must be left - right and the other right - left:
        dists.append(
            (
                (left[0] - right[0], left[1] - right[1]),
                (right[0] - left[0], right[1] - left[1]),
            )
        )

    return dists


def get_all_pairs2(list_of_poss):
    pairs = []
    for i, pos in enumerate(list_of_poss):
        for j in range(len(list_of_poss)):
            pair = (pos, list_of_poss[j])
            if pair != (pos, pos):
                pairs.append(pair)

    return pairs


def distances2(pairs):
    dists = []
    for left, right in pairs:
        # one must be left - right and the other right - left:
        dists.append(
            (
                (left[0] - right[0], left[1] - right[1]),
                (right[0] - left[0], right[1] - left[1]),
            )
        )

    return dists


def part1(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here

    rmax = len(input_str.splitlines())
    cmax = len(input_str.splitlines()[0])
    antennas = dict()
    for i, line in enumerate(input_str.splitlines()):
        for j, ch in enumerate(list(line)):
            if ch != ".":
                antennas = append2dict(antennas, ch, (i, j))

    # print(antennas)

    # create antinodes for every antenna pair:
    antinode_poss = []
    for antenna_type, poss_list in antennas.items():
        pairs = get_all_pairs(poss_list)
        # print("Pairs:")
        # print(pairs)

        # now the distances
        dists = distances(pairs)
        # print("Distances:")
        # print(dists)

        # and now all antinode positions:  and save them to result
        for i, (p1, p2) in enumerate(pairs):
            ((p1_rd, p1_cd), (p2_rd, p2_cd)) = dists[i]
            a1 = (p1[0] + p1_rd, p1[1] + p1_cd)
            a2 = (p2[0] + p2_rd, p2[1] + p2_cd)

            if a1[0] >= 0 and a1[0] < rmax and a1[1] >= 0 and a1[1] < cmax:
                # is in bounds:

                if a1 not in poss_list:
                    antinode_poss.append(a1)
                else:
                    # matches an antenna pos
                    pass
            else:
                # OOB!
                pass

            if a2[0] >= 0 and a2[0] < rmax and a2[1] >= 0 and a2[1] < cmax:
                # is in bounds:

                if a2 not in poss_list:
                    antinode_poss.append(a2)
                else:
                    # matches an antenna pos
                    pass
            else:
                # OOB!
                pass

    result = len(set(antinode_poss))
    print(f"all antinodes: {antinode_poss}")
    print(f"Part 1 result is: {result}")

    end_time = time.time()
    print(f"Part 1 execution time: {end_time - start_time} seconds")


def part2(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here

    rmax = len(input_str.splitlines())
    cmax = len(input_str.splitlines()[0])
    antennas = dict()
    for i, line in enumerate(input_str.splitlines()):
        for j, ch in enumerate(list(line)):
            if ch != ".":
                antennas = append2dict(antennas, ch, (i, j))

    # print(antennas)

    # create antinodes for every antenna pair:
    antinode_poss = []
    for antenna_type, poss_list in antennas.items():
        all_antenna_posis = antennas.values()

        pairs = get_all_pairs2(poss_list)
        # print("Pairs:")
        # print(pairs)

        # now the distances
        dists = distances2(pairs)
        # print("Distances:")
        # print(dists)

        # and now all antinode positions:  and save them to result
        for i, (p1, p2) in enumerate(pairs):
            ((p1_rd, p1_cd), (p2_rd, p2_cd)) = dists[i]

            mtpl_count = (
                max([rmax, cmax])
                // min(list(map(abs, [p1_rd, p1_cd, p2_rd, p2_cd])))
                + 1
            )
            # print(f"mtpl_count {mtpl_count}")

            # do this for all multiples in bounds:
            oob_a1 = False
            oob_a2 = False
            for m in range(mtpl_count):
                # now loop

                a1 = (p1[0] + m * p1_rd, p1[1] + m * p1_cd)
                a2 = (p2[0] + m * p2_rd, p2[1] + m * p2_cd)

                if a1[0] >= 0 and a1[0] < rmax and a1[1] >= 0 and a1[1] < cmax:
                    # is in bounds:

                    if a1 not in all_antenna_posis:
                        antinode_poss.append(a1)
                    else:
                        # matches an antenna pos
                        pass
                else:
                    # OOB!
                    oob_a1 = True
                    pass

                if a2[0] >= 0 and a2[0] < rmax and a2[1] >= 0 and a2[1] < cmax:
                    # is in bounds:

                    if a2 not in all_antenna_posis:
                        antinode_poss.append(a2)
                    else:
                        # matches an antenna pos
                        pass
                else:
                    # OOB!
                    oob_a2 = True
                    pass

                if oob_a1 and oob_a2:
                    # do not follow these antinode rays
                    break

    result = len(set(antinode_poss))

    # debug antinode posis:
    # Assuming rmax and cmax are defined somewhere in your code
    grid = [["." for _ in range(cmax)] for _ in range(rmax)]

    # Mark the positions of the antinodes
    for antinode in antinode_poss:
        grid[antinode[0]][antinode[1]] = "#"

    # Print the grid
    print("Antinodes grid:")
    for row in grid:
        print(" ".join(row))

    result = len(set(antinode_poss))

    # print(f"all antinodes: {antinode_poss}")

    print(f"Part 2 result is: {result}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")
