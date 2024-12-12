import time
import os


def neighs(pos, rmax, cmax):
    neigh_posis = []
    for i, j in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        neigh_pos = (pos[0] + i, pos[1] + j)
        if (
            neigh_pos[0] >= 0
            and neigh_pos[0] < rmax
            and neigh_pos[1] >= 0
            and neigh_pos[1] < cmax
        ):
            neigh_posis.append(neigh_pos)
    return neigh_posis


def find_paths(grid, path, pos, rmax, cmax, paths):
    if grid[pos[0]][pos[1]] == 9:
        paths.add(tuple(path.copy()))
        # paths.append(path.copy())
        return

    neighs_posis = neighs(pos, rmax, cmax)
    hit = False
    for ni, nj in neighs_posis:
        if grid[ni][nj] - grid[pos[0]][pos[1]] == 1:
            hit = True
            # next tile is 1 higher -> go there, possible path
            path.append((ni, nj))

            # call recursive find_paths
            find_paths(grid, path, (ni, nj), rmax, cmax, paths)

            # backtrack
            path.pop()
    # return []


def part1(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here

    topo_map = []
    for line in input_str.splitlines():
        topo_map.append(list(map(int, list(line))))

    # print(topo_map)
    # print(input_str)

    trail_head_posis = []
    for i, line in enumerate(topo_map):
        for j, num in enumerate(line):
            if num == 0:
                trail_head_posis.append((i, j))

    #
    rmax = len(topo_map)
    cmax = len(topo_map[0])
    all_paths = []

    score = []
    for start in trail_head_posis:
        paths = set()
        # print()

        find_paths(topo_map, [start], start, rmax, cmax, paths)
        # print(paths)
        # print(f"len(paths)={len(paths)}")

        score.append(len(set([tup_li[-1] for tup_li in paths])))
        # all_paths.append(list(paths))

    print(f"scores: {score}")
    print(f"Part 1 result is: {sum(score)}")

    end_time = time.time()
    print(f"Part 1 execution time: {end_time - start_time} seconds")


def part2(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 2:")
    # Implement the logic here
    # Your part2 logic here

    topo_map = []
    for line in input_str.splitlines():
        topo_map.append(list(map(int, list(line))))

    # print(topo_map)
    # print(input_str)

    trail_head_posis = []
    for i, line in enumerate(topo_map):
        for j, num in enumerate(line):
            if num == 0:
                trail_head_posis.append((i, j))

    #
    rmax = len(topo_map)
    cmax = len(topo_map[0])
    all_paths = []

    ratings = []
    for start in trail_head_posis:
        paths = set()
        # print()

        find_paths(topo_map, [start], start, rmax, cmax, paths)
        # print(paths)
        # print(f"len(paths)={len(paths)}")

        ratings.append(len(paths))
        # all_paths.append(list(paths))

    print(f"scores: {ratings}")
    print(f"Part 2 result is: {sum(ratings)}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")
