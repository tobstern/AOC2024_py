import time
import os
import heapq


def parse_input(input_str, rcmax, L):
    grid = [["." for _ in range(rcmax)] for _ in range(rcmax)]
    graph = {(i, j): "." for j in range(rcmax) for i in range(rcmax)}
    # print(grid)
    byte_posis = []

    for i, line in enumerate(input_str.strip().splitlines()):
        if i >= L:
            # cut-off at how many bytes has beeen fallen into space
            break

        x, y = tuple(map(int, line.strip().split(",")))
        # print(x, y)
        grid[y][x] = "#"
        graph[(y, x)] = "#"

    for i, line in enumerate(input_str.strip().splitlines()):
        x, y = tuple(map(int, line.strip().split(",")))
        byte_posis.append((y, x))

    return graph, grid, byte_posis


def get_neighs(g, curr_pos):
    rcmax = len(g)
    # print(rcmax)
    r, c = curr_pos
    neighs = []
    # possible next directions: all if in bounds and not #

    for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        # in bounds, no need to check, all surrounded by #
        # if 0 <= nr < rmax and 0<=nc <cmax:
        nr, nc = r + dr, c + dc
        # if not #
        if 0 <= nr <= rcmax - 1 and 0 <= nc <= rcmax - 1:
            if g[nr][nc] != "#":
                neighs.append((nr, nc))

    return neighs


def dijkstra(graph, grid, S, E):
    dist = {}
    prev = {}
    all_best_paths = {}

    # now ini weights and queue
    for (r, c), v in graph.items():
        dist[(r, c)] = float("inf")
        prev[(r, c)] = []

    dist[S] = 0

    queue = [(0, S[0], S[1])]
    seen = set()
    while queue:
        (u, cr, cc) = heapq.heappop(queue)

        if (cr, cc) in seen:
            continue
        seen.add((cr, cc))

        # break if end is found:
        if (cr, cc) == E:
            # print(f"cost result = {u}")
            break

        # find possible! neighs here:
        poss_neighs = get_neighs(grid, (cr, cc))
        for nr, nc in poss_neighs:
            alt = u + 1
            # alt = dist[(cr, cc)] + 1

            if alt < dist[(nr, nc)]:
                dist[(nr, nc)] = alt
                prev[(nr, nc)].append((cr, cc))
            heapq.heappush(queue, (alt, nr, nc))

            # alt = dist[(cr, cc)] + dist[(nr, nc)]

    return dist, prev


def part1(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here
    # L = 12
    # rcmax = 7
    L = 1024
    rcmax = 71

    S = (0, 0)
    E = (rcmax - 1, rcmax - 1)

    graph, grid, byte_posis = parse_input(input_str, rcmax, L)

    # print(grid)
    # print(graph)
    # print(byte_posis)

    grid_str = ""
    for row in grid:
        for ch in row:
            grid_str += ch
        grid_str += "\n"
    # print(grid_str)
    # do dijkstra:
    dists, prevs = dijkstra(graph, grid, S, E)

    # print(dists)
    # print(prevs)
    result = dists[E]
    print(f"Part 1 result is: {result}")

    end_time = time.time()
    print(f"Part 1 execution time: {end_time - start_time} seconds")


def part2(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 2:")
    # Implement the logic here
    # Your part2 logic here
    # L = 12
    # rcmax = 7
    L = 1024
    rcmax = 71

    S = (0, 0)
    E = (rcmax - 1, rcmax - 1)

    graph, grid, byte_posis = parse_input(input_str, rcmax, L)

    # print(grid)
    # print(graph)
    # print(byte_posis)

    grid_str = ""
    for row in grid:
        for ch in row:
            grid_str += ch
        grid_str += "\n"
    # print(grid_str)
    # do dijkstra:
    # simulate falling bytes until way is blocked
    for i, byte_pos in enumerate(byte_posis):
        r, c = byte_pos
        # print(byte_pos)
        grid[r][c] = "#"
        graph[(r, c)] = "#"
        dists, prevs = dijkstra(graph, grid, S, E)

        if dists[E] == float("inf"):
            result = ",".join([str(byte_pos[1]), str(byte_pos[0])])
            break

    # print(dists)
    # print(prevs)
    # result = dists[E]

    print(f"Part 2 result is: {result}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")
    # 66 seconds...
