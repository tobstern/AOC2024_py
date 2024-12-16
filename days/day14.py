import time
import os
import numpy as np
from scipy.stats import entropy


def parse_input(input_str):
    robo_velos = []
    curr_robo_posis = []
    for robo, line in enumerate(input_str.splitlines()):
        # split, ' ' -> '=' -> ','
        posi_str, velo_str = line.split(" ")
        # print(posi_str)
        pc, pr = list(map(int, posi_str.split("=")[1].split(",")))
        vc, vr = list(map(int, velo_str.split("=")[1].split(",")))
        # print(f"pr, pc={(pr, pc)} - vr, vc={(vr, vc)}")

        # insert into grid:
        # grid[pr, pc] += 1

        # save velocities
        robo_velos.append((vr, vc))
        curr_robo_posis.append([pr, pc])

    return curr_robo_posis, robo_velos


def move_robots(ps, vs, rmax, cmax):
    for robo in range(len(vs)):
        vi, vj = vs[robo]
        pi, pj = ps[robo]

        # print(f"pi,pj={(pi, pj)} - vi,vj={(vi, vj)}")
        # robos move by its velocity and if reached boundary, it is wrapped, so %(modulo)
        ps[robo] = [(pi + vi) % rmax, (pj + vj) % cmax]

    # all robos have been moved this second

    # return ps


def pretty_print_grid(grid, rmax, cmax):
    grid_str = ""
    for i in range(rmax):
        for j in range(cmax):
            grid_str += str(grid[i][j]) + " "
        grid_str += "\n"
    return grid_str


def part1(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here

    seconds = 100
    # rmax, cmax = 7, 11
    rmax, cmax = 103, 101

    curr_posis, velos = parse_input(input_str)

    # loop and move_robos for 100 seconds
    for _ in range(seconds):
        # curr_posis = move_robots(curr_posis, velos, rmax, cmax)
        move_robots(curr_posis, velos, rmax, cmax)

    # sum each quadrant - without horizopntal and vertical middle line
    grid = np.zeros((rmax, cmax), dtype=int)
    for robo, (i, j) in enumerate(curr_posis.copy()):
        grid[i, j] += 1

    print(pretty_print_grid(grid, rmax, cmax))

    grid[rmax // 2, :] = 0
    grid[:, cmax // 2] = 0

    # print(
    #     f"quadrant results: {(
    #     np.sum(grid[: rmax // 2, : cmax // 2])  # top left
    #     , np.sum(grid[rmax // 2 + 1 :, : cmax // 2])  # bottom left
    #     , np.sum(grid[rmax // 2 + 1 :, cmax // 2 + 1 :])  # bottom right
    #     , np.sum(grid[: rmax // 2, cmax // 2 + 1 :])  # top right
    # )}"
    # )
    result = (
        np.sum(grid[: rmax // 2, : cmax // 2])  # top left
        * np.sum(grid[rmax // 2 + 1 :, : cmax // 2])  # bottom left
        * np.sum(grid[rmax // 2 + 1 :, cmax // 2 + 1 :])  # bottom right
        * np.sum(grid[: rmax // 2, cmax // 2 + 1 :])  # top right
    )
    print(f"Part 1 result is: {result}")

    end_time = time.time()
    print(f"Part 1 execution time: {end_time - start_time} seconds")


def part2(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 2:")
    # Implement the logic here

    # rmax, cmax = 7, 11
    rmax, cmax = 103, 101
    seconds = rmax * cmax

    curr_posis, velos = parse_input(input_str)

    starting_posis = curr_posis

    # loop and move_robos for 100 seconds
    result = None
    min_sfac = float("inf")
    max_sfac = 0
    safety_facs = []
    HR = rmax // 2
    HC = cmax // 2
    RB = rmax // 2
    CB = cmax // 2

    for sec in range(1, seconds):
        # print()
        # print(f"second: {sec}")
        # curr_posis = move_robots(curr_posis, velos, rmax, cmax)
        move_robots(curr_posis, velos, rmax, cmax)

        # check if xmas tree:
        # grid = np.zeros((rmax, cmax), dtype=int)
        tl, tr, bl, br = (0, 0, 0, 0)
        hor, ver = (0, 0)
        for i, j in curr_posis:
            if i == HR or j == HC:
                hor += 1
                continue
            if RB // 4 < i < RB and CB // 4 < j < CB:
                tl += 1
            elif RB // 4 < i < RB and HC + CB // 4 > j > CB:
                tr += 1
            elif HR + RB // 4 > i > RB and CB // 4 < j < CB:
                bl += 1
            elif HR + RB // 4 > i > RB and HC + CB // 4 > j > CB:
                br += 1
        sfac = tl * tr * bl * br
        # sfac = hor

        if sec == 100:
            print(f"sfac={sfac}")
        if sfac > max_sfac:
            max_sfac = sfac
            result = sec
            safety_facs.append((sfac, sec))

            grid = np.array([["."] * cmax] * rmax, dtype=str)
            print(grid.shape)
            for i, j in curr_posis:
                grid[i, j] = "#"

            print(pretty_print_grid(grid, rmax, cmax))

    print(safety_facs)

    print(f"Part 2 result is: {result}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")
