import time
import os
import numpy as np


def sum_tuples(x, y):
    return tuple(map(sum, (zip(x, y))))


def rotate90(d):
    if d == (1, 0):
        return (0, -1)
    elif d == (0, -1):
        return (-1, 0)
    elif d == (-1, 0):
        return (0, 1)
    elif d == (0, 1):
        return (1, 0)
    else:
        exit("Undefined direction!")


def move_guard(lab_grid, start, visited):
    rmax = len(lab_grid)
    cmax = len(lab_grid[0])
    # print(rmax, cmax)

    curr_pos = start
    curr_dir = (-1, 0)
    next_pos = sum_tuples(curr_pos, curr_dir)

    while True:

        # print(curr_pos)
        next_pos = sum_tuples(curr_pos, curr_dir)

        if next_pos[0] < 0 or next_pos[0] >= rmax or next_pos[1] < 0 or next_pos[1] >= cmax:
            return visited

        # time.sleep(1)
        if lab_grid[next_pos] == "#":
            # rotate 90° to right
            curr_dir = rotate90(curr_dir)
            curr_pos = sum_tuples(curr_pos, curr_dir)
        elif lab_grid[next_pos] == ".":
            # follow the direction
            curr_pos = sum_tuples(curr_pos, curr_dir)

        else:
            exit("Undefined tile ahead!!!")

        # visited.add(curr_pos)
        visited.add((curr_pos, curr_dir))


def part1(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here

    lab_grid = []
    start = (0, 0)
    for i, line in enumerate(input_str.splitlines()):
        lab_grid.append(list(line))
        # save start '^'
        for j, ch in enumerate(line):
            if ch == "^":
                start = (i, j)
                lab_grid[i][j] = "."

    print(start)
    lab_grid = np.asarray(lab_grid)
    print(lab_grid)

    # now follow the guards pattern: if hit bounds, stop - in front of #, 90° right, else straight
    # visited = set((start, (-1, 0)))
    visited = set()
    visited = move_guard(lab_grid, start, visited)

    result = set()
    for pos, di in visited:
        result.add(pos)

    print(f"Part 1 result is: {len(result)}")

    end_time = time.time()
    print(f"Part 1 execution time: {end_time - start_time} seconds")

    # return visited locs for part2 (locs to be looped)
    return visited, lab_grid, start


def pretty_print_grid(lab_grid, vis, try_pos):
    rmax = len(lab_grid)
    cmax = len(lab_grid[0])

    for r in range(rmax):
        for c in range(cmax):
            if (r, c) == try_pos:
                print("X", end="")
            elif (r, c) in [pos for pos, _ in vis]:
                directions = [d for (pos, d) in vis if pos == (r, c)]
                if len(directions) > 1:
                    print("+", end="")
                else:
                    direction = directions[0]
                    if direction in [(-1, 0), (1, 0)]:
                        print("|", end="")
                    elif direction in [(0, -1), (0, 1)]:
                        print("-", end="")
                    else:
                        print(".", end="")
            else:
                print(lab_grid[r][c], end="")
        print()  # Newline at the end of each row
    print("\n\n")


def test_circ(lab_grid, start, try_pos):
    # test for circles:
    vis = set()

    rmax = len(lab_grid)
    cmax = len(lab_grid[0])
    # print(rmax, cmax)

    curr_pos = start
    curr_dir = (-1, 0)
    next_pos = sum_tuples(curr_pos, curr_dir)

    while True:

        if ((curr_pos), (curr_dir)) in vis:
            # print(vis)
            pretty_print_grid(lab_grid, vis, try_pos)
            return True
        # visited.add(curr_pos)
        # if curr_pos != start:
        vis.add((curr_pos, curr_dir))

        # print(curr_pos)
        next_pos = sum_tuples(curr_pos, curr_dir)

        if next_pos[0] < 0 or next_pos[0] >= rmax or next_pos[1] < 0 or next_pos[1] >= cmax:
            break

        # time.sleep(1)
        if lab_grid[next_pos] == "#" or next_pos == try_pos:
            # rotate 90° to right
            curr_dir = rotate90(curr_dir)
            curr_pos = sum_tuples(curr_pos, curr_dir)
        elif lab_grid[next_pos] == ".":
            # follow the direction
            curr_pos = sum_tuples(curr_pos, curr_dir)

        else:
            exit("Undefined tile ahead!!!")

        # curr_pos = sum_tuples(curr_pos, curr_dir)

    # if went out of while loop -> no circle
    return False


def part2(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 2:")
    # Implement the logic here
    # Your part2 logic here
    # lab_grid = []
    # start = (0, 0)
    # for i, line in enumerate(input_str.splitlines()):
    #     lab_grid.append(list(line))
    #     # save start '^'
    #     for j, ch in enumerate(line):
    #         if ch == "^":
    #             start = (i, j)
    #             lab_grid[i][j] = "."

    # print(start)
    # lab_grid = np.asarray(lab_grid)
    # print(lab_grid)

    visited, lab_grid, start = part1(input_str)
    # print(visited, lab_grid, start)
    # visited = (pos, dir)

    circ_count = 0
    curr_dir = (-1, 0)
    for (i, j), (di, dj) in visited:

        # print()
        # print(((i, j), (di, dj)))
        # print(visited)

        try_pos = (i, j)
        if lab_grid[i, j] == "#" or (i, j) == start:
            continue
            # else:
            # exchange to #
            # lab_grid[i, j] = "#"

        if test_circ(lab_grid, start, try_pos):
            circ_count += 1
        # print(f"circ_count = {circ_count}")

    print(f"Part 2 result is: {circ_count}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")