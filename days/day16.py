import time
import os
import heapq
from collections import deque


def get_dirs(g, curr_pos, curr_dir):
    # rmax, cmax = maxis
    r, c = curr_pos
    dr, dc = curr_dir
    dirs = []
    # possible next directions: +-90°
    pdc, pdr = -dr, dc  # plus90 - right
    mdc, mdr = dr, -dc  # minus90 left

    for ddr, ddc in [(dr, dc), (mdr, mdc), (pdr, pdc)]:
        # in bounds, no need to check, all surrounded by #
        # if 0 <= nr < rmax and 0<=nc <cmax:
        nr, nc = r + ddr, c + ddc
        # if not #
        if g[nr][nc] != "#":
            dirs.append((ddr, ddc))

    return dirs


def dijkstra(graph, grid, S, E):
    dist = {}
    prev = {}
    all_best_paths = {}
    direc = (0, 1)

    # now ini weights and queue
    for (r, c), v in graph.items():
        dist[(r, c)] = float("inf")
        prev[(r, c)] = []

    dist[S] = 0

    queue = [(0, S[0], S[1], direc[0], direc[1])]
    seen = set()
    while queue:
        (u, cr, cc, dr, dc) = heapq.heappop(queue)

        if (cr, cc, dr, dc) in seen:
            continue
        seen.add((cr, cc, dr, dc))

        # break if end is found:
        if (cr, cc) == E:
            print(f"cost result = {u}")
            break

        # find possible! neighs here:
        poss_dirs = get_dirs(grid, (cr, cc), (dr, dc))
        for dnr, dnc in poss_dirs:
            # if direction has changed: +1000, else + 1
            dir_changed = False
            if (dnr, dnc) != (dr, dc):
                nr, nc = (cr, cc)
                alt = u + 1000
                # alt = dist[(cr, cc)] + 1000 + 1
            else:
                # no dir change
                nr, nc = (cr + dnr, cc + dnc)
                alt = u + 1
                # alt = dist[(cr, cc)] + 1
                dir_changed = True

            if alt < dist[(nr, nc)]:
                dist[(nr, nc)] = alt
                prev[(nr, nc)].append((cr, cc))
            heapq.heappush(queue, (alt, nr, nc, dnr, dnc))

            # alt = dist[(cr, cc)] + dist[(nr, nc)]

    return dist, prev


def part1(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here

    maze = []
    graph = {}
    S = (0, 0)
    E = (0, 0)
    for r, line in enumerate(input_str.strip().splitlines()):
        for c, ch in enumerate(line):
            graph[(r, c)] = ch

            if ch == "S":
                S = (r, c)
            if ch == "E":
                E = (r, c)
        maze.append(list(line))

    rmax = r
    cmax = c
    print(f"S={S} - E={E}")
    # print(maze)

    # find shortest/cheapest path through the maze:
    # They can move forward one tile at a time (increasing their score by 1 point), but never into a wall (#).
    # They can also rotate clockwise or counterclockwise 90 degrees at a time (increasing their score by 1000 points).
    # Dijkstra?
    dists, nodes, path = dijkstra(graph, maze, S, E)

    # print(dists[E])
    # print(paths)
    # print(len(path))

    result = dists[E]
    print(f"Part 1 result is: {result}")

    end_time = time.time()
    print(f"Part 1 execution time: {end_time - start_time} seconds")


def dijkstra2(graph, grid, S, E, best_cost):
    dist = {}
    prev = {}
    all_best_paths = {}
    direc = (0, 1)

    # now ini weights and queue
    for (r, c), v in graph.items():
        dist[(r, c)] = float("inf")
        prev[(r, c)] = []

    dist[S] = 0

    queue = [(0, S[0], S[1], direc[0], direc[1])]
    seen = set()
    # paths = {}
    lowest_cost = {(S[0], S[1], direc[0], direc[1]): 0}
    best_cost = float("inf")
    backtrack = {}
    end_states = set()
    while queue:
        (u, cr, cc, dr, dc) = heapq.heappop(queue)

        if u > lowest_cost.get((cr, cc, dr, dc), float("inf")):
            continue

        # if (cr, cc, dr, dc) in seen:
        #    continue
        # seen.add((cr, cc, dr, dc))

        # break if end is found:
        if (cr, cc) == E:
            if u > best_cost:
                break
            # print(f"cost result = {u}")
            best_cost = u
            end_states.add((cr, cc, dr, dc))

        # find possible! neighs here:
        poss_dirs = get_dirs(grid, (cr, cc), (dr, dc))
        for dnr, dnc in poss_dirs:

            if (dnr, dnc) != (dr, dc):
                nr, nc = (cr, cc)
                new_cost = u + 1000
            else:
                # no dir change
                nr, nc = (cr + dnr, cc + dnc)
                new_cost = u + 1

            if new_cost < dist[(nr, nc)]:
                dist[(nr, nc)] = new_cost
                prev[(nr, nc)].append((cr, cc))

            lowest = lowest_cost.get((nr, nc, dnr, dnc), float("inf"))
            if new_cost > lowest:
                continue
            if new_cost < lowest:
                lowest_cost[(nr, nc, dnr, dnc)] = new_cost
                backtrack[(nr, nc, dnr, dnc)] = set()
            backtrack[(nr, nc, dnr, dnc)].add((cr, cc, dr, dc))
            heapq.heappush(queue, (new_cost, nr, nc, dnr, dnc))

            # alt = dist[(cr, cc)] + dist[(nr, nc)]

    return dist, prev, backtrack, end_states


def part2(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 2:")
    # Implement the logic here
    # Your part2 logic here
    maze = []
    graph = {}
    S = (0, 0)
    E = (0, 0)
    for r, line in enumerate(input_str.strip().splitlines()):
        for c, ch in enumerate(line):
            graph[(r, c)] = ch

            if ch == "S":
                S = (r, c)
            if ch == "E":
                E = (r, c)
        maze.append(list(line))

    rmax = r
    cmax = c
    print(f"S={S} - E={E}")
    # print(maze)

    # find shortest/cheapest path through the maze:
    # They can move forward one tile at a time (increasing their score by 1 point), but never into a wall (#).
    # They can also rotate clockwise or counterclockwise 90 degrees at a time (increasing their score by 1000 points).
    # Dijkstra?
    dists, nodes = dijkstra(graph, maze, S, E)
    best_cost = dists[E]

    dists, nodes, backtrack, end_states = dijkstra2(
        graph, maze, S, E, best_cost
    )

    # BFF
    # print(end_states)
    states = deque(end_states)
    seen = set(end_states)
    while states:
        key = states.popleft()
        for last in backtrack.get(key, []):
            if last in seen:
                continue
            seen.add(last)
            states.append(last)

    # print(seen)
    result = len({(r, c) for r, c, _, _ in seen})
    # print(f"Intersection positions of all cheapest paths: {intersec_posis}")
    # print(backtrack)

    # result = len(intersec_posis)
    print(f"Part 2 result is: {result}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")
