import time
import os
from collections import deque


def parse_input(string):
    grid = [list(line) for line in string.strip().splitlines()]
    rmax, cmax = (len(grid), len(grid[0]))
    S = tuple()
    E = tuple()
    for i in range(rmax):
        for j in range(cmax):
            if grid[i][j] == "S":
                S = (i, j)
            if grid[i][j] == "E":
                E = (i, j)
    return grid, (S, E), (rmax, cmax)


def bfs(grid, S, E, rmax, cmax):
    dist = []
    q = deque([S])
    # now ini weights and queue
    r, c = S
    dist = [[-1] * cmax for _ in range(rmax)]
    dist[r][c] = 0

    # print(dist)
    # exit()

    while q:
        (r, c) = q.popleft()

        for nr, nc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
            if nr < 0 or nr >= rmax or nc < 0 or nc >= cmax:
                continue
            # alt = dist[(cr, cc)] + 1
            if grid[nr][nc] == "#":
                continue
            if dist[nr][nc] != -1:
                continue

            dist[nr][nc] = dist[r][c] + 1

            q.append((nr, nc))

    return dist


def find_cheat_savings(grid, dist, S, E, rmax, cmax):

    # Find all possible positions that can be "cheated" through (walls).
    count = 0
    for r in range(rmax):
        for c in range(cmax):
            if grid[r][c] == "#":
                continue

            # just look in "one direction" - from upper left perspective, thereby you check every possible one
            for dr, dc in [(2, 0), (1, 1), (0, 2), (-1, 1)]:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= rmax or nc < 0 or nc >= cmax:
                    continue
                if grid[nr][nc] == "#":
                    continue

                if abs(dist[r][c] - dist[nr][nc]) >= 102:
                    count += 1

    return count


def part1(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here

    grid, (S, E), (rmax, cmax) = parse_input(input_str)
    # print(grid)
    # print(S, E)
    # print(rmax, cmax)
    # exit()

    dists = bfs(grid, S, E, rmax, cmax)
    best_time = dists[E[0]][E[1]]

    # for line in dists:
    #     print(*line, sep="\t")
    # print(dists)

    # Find the cheat savings
    count = find_cheat_savings(grid, dists, S, E, rmax, cmax)

    print(f"Part 1 result is: {count}")

    end_time = time.time()
    print(f"Part 1 execution time: {end_time - start_time} seconds")


def find_cheat_savings2(grid, dist, S, E, rmax, cmax):

    # Find all possible positions that can be "cheated" through (walls).
    count = 0
    for r in range(rmax):
        for c in range(cmax):
            if grid[r][c] == "#":
                continue

            # just look in "one direction" - from upper left perspective, thereby you check every possible one
            for radius in range(2, 21):
                for dr in range(radius + 1):
                    dc = radius - dr
                    for nr, nc in {
                        (r + dr, c + dc),
                        (r + dr, c - dc),
                        (r - dr, c + dc),
                        (r - dr, c - dc),
                    }:

                        if nr < 0 or nr >= rmax or nc < 0 or nc >= cmax:
                            continue
                        if grid[nr][nc] == "#":
                            # do not hit the wall
                            continue

                        if dist[r][c] - dist[nr][nc] >= 100 + radius:
                            # check all radii that save 20 ps
                            count += 1

    return count


def part2(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 2:")
    # Implement the logic here

    grid, (S, E), (rmax, cmax) = parse_input(input_str)
    # print(grid)
    # print(S, E)
    # print(rmax, cmax)
    # exit()

    dists = bfs(grid, S, E, rmax, cmax)
    best_time = dists[E[0]][E[1]]

    # for line in dists:
    #     print(*line, sep="\t")
    # print(dists)

    # Find the cheat savings
    count = find_cheat_savings2(grid, dists, S, E, rmax, cmax)

    print(f"Part 2 result is: {count}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")
