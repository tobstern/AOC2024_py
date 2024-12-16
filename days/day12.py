import time
import os


def parse_garden_map(garden_map):
    return [list(row) for row in garden_map.split()]


def dfs(garden, visited, i, j, ch):
    stack = [(i, j)]
    region = []
    perimeter = 0
    while stack:
        x, y = stack.pop()
        if (x, y) not in visited:
            visited.add((x, y))
            region.append((x, y))
            # Check all 4 directions
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(garden) and 0 <= ny < len(garden[0]):
                    if garden[nx][ny] == ch:
                        stack.append((nx, ny))
                    else:
                        perimeter += 1
                else:
                    perimeter += 1
    return region, perimeter


def find_regions(garden_map):
    garden = parse_garden_map(garden_map)
    visited = set()
    regions = {}
    peris = {}
    for i in range(len(garden)):
        for j in range(len(garden[0])):
            ch = garden[i][j]
            if (i, j) not in visited:
                region, perimeter = dfs(garden, visited, i, j, ch)
                if ch not in regions:
                    regions[ch] = []
                    peris[ch] = []
                regions[ch].append(region)
                peris[ch].append(perimeter)
    return regions, peris


def part1(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here

    regions, peris = find_regions(input_str)
    result = 0
    for ch, reg in regions.items():
        # print(f"Character: {ch}")
        for idx, r in enumerate(reg):
            # print(f"Region: {r}, Perimeter: {peris[ch][idx]}")
            result += peris[ch][idx] * len(r)

    print(f"Part 1 result is: {result}")

    end_time = time.time()
    print(f"Part 1 execution time: {end_time - start_time} seconds")


def sign(num):
    if num < 0:
        return -1
    elif num == 0:
        return 0
    else:
        return 1


def sides(region):
    edges = {}
    # print(region)
    for r, c in region:
        # check neighs
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            # if the neigh is in region - not an edge
            if (nr, nc) in region:
                continue
            er = (r + nr) / 2
            ec = (c + nc) / 2
            edges[(er, ec)] = (er - r, ec - c)

    seen = set()
    side_count = 0
    for edge, direc in edges.items():
        if edge in seen:
            continue
        seen.add(edge)
        side_count += 1

        er, ec = edge
        if er % 1 == 0:
            # if er is integer
            for dr in [-1, 1]:
                cr = er + dr
                while (cr, ec) in edges and edges[(cr, ec)] == direc:
                    # column here never changes
                    seen.add((cr, ec))
                    cr += dr
        else:
            # if er is not integer -> ec is int:
            for dc in [-1, 1]:
                cc = ec + dc
                while (er, cc) in edges and edges[(er, cc)] == direc:
                    # column here never changes
                    seen.add((er, cc))
                    cc += dc

    return side_count
    # print(edges)


def part2(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 2:")
    # Implement the logic here
    garden = parse_garden_map(input_str)

    regions, peris = find_regions(input_str)
    # print(regions)

    result = 0
    for char in regions:
        for region in regions[char]:
            # print("=" * 80)
            # print(char)
            # r, c = list(region)[0]
            # print(garden[r][c])
            result += len(region) * sides(region)

    # calc straight perimeters:

    print(f"Part 2 result is: {result}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")
