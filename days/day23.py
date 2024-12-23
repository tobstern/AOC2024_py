import time
import os


def part1(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here

    comps = {}
    for conn in input_str.splitlines():
        left, right = conn.split("-")
        if left not in comps:
            comps[left] = set()
        if right not in comps:
            comps[right] = set()

        comps[left].add(right)
        comps[right].add(left)

    # -> with the set it did not work....
    # print(comps)
    # set of 3 with > 0 t count
    # threeset = set()
    count = 0
    # sets = set()
    for a in comps:
        for b in comps[a]:
            for c in comps[b]:
                if (
                    a != c
                    and a in comps[c]
                    and any(con.startswith("t") for con in [a, b, c])
                ):
                    # now it is back connected:
                    count += 1
                    # sets.add(tuple(sorted([a, b, c])))

    # print(threeset)
    # sets = set(tup for tup in sets if "t" in "".join(tup))
    # result = len(sets)
    result = count // 6
    print(f"Part 1 result is: {result}")

    end_time = time.time()
    print(f"Part 1 execution time: {end_time - start_time} seconds")


def part2(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 2:")
    # Implement the logic here

    comps = {}
    for conn in input_str.splitlines():
        left, right = conn.split("-")
        if left not in comps:
            comps[left] = set()
        if right not in comps:
            comps[right] = set()

        comps[left].add(right)
        comps[right].add(left)

    # print(comps)

    sets = set()

    def all_conns(node, requis):
        key = tuple(sorted(requis))  # avoid dublicates=sort it
        if key in sets:
            return  # avoid duble counting and end recursion
        sets.add(key)

        for neigh in comps[node]:
            # neigh not already in required nodes
            if neigh in requis:
                continue
            if not (requis <= comps[neigh]):
                continue

            all_conns(
                neigh, requis | {neigh}
            )  # search on neigh with new conn set

        # if neigh is connected to all - is valid
        # test_all = 0
        # for r in requis:
        #     if neigh in comps[r]:
        #         test_all += 1
        #     if test_all == len(requis):
        #         # it is connected to all in requis:
        #         all_conns(neigh, requis + [neigh])

    for s in comps:
        all_conns(s, {s})

    # print(sets)

    # max_conns = []
    # max_len = 0
    # for sub in sets:
    #     if len(sub) > max_len:
    #         max_len = len(sub)
    #         max_conns = list(sorted(sub))
    result = max(sets, key=len)

    result = ",".join(sorted(result))
    print(f"Part 2 result is: {result}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")
