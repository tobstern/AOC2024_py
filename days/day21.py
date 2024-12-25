import time
import os

from collections import deque
import re
from functools import cache
from itertools import product


def part1(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here

    # Define keypads
    numpad = [
        ["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        [None, "0", "A"],
    ]

    dirpad = [
        [None, "^", "A"],
        ["<", "v", ">"],
    ]

    def solve(string, keypad):
        pos = {}
        for r in range(len(keypad)):
            for c in range(len(keypad[r])):
                if keypad[r][c] is not None:
                    pos[keypad[r][c]] = (r, c)
        seqs = {}
        for x in pos:
            for y in pos:
                if x == y:
                    seqs[(x, y)] = ["A"]
                    continue

                possis = []
                q = deque([(pos[x], "")])
                optimal = float("inf")
                while q:
                    (r, c), moves = q.popleft()

                    for nr, nc, nm in [
                        (r - 1, c, "^"),
                        (r + 1, c, "v"),
                        (r, c - 1, "<"),
                        (r, c + 1, ">"),
                    ]:
                        if (
                            nr < 0
                            or nc < 0
                            or nr >= len(keypad)
                            or nc >= len(keypad[0])
                        ):
                            continue
                        if keypad[nr][nc] == None:
                            continue
                        if keypad[nr][nc] == y:
                            if optimal < len(moves) + 1:
                                break
                            optimal = len(moves) + 1
                            possis.append(moves + nm + "A")
                        else:
                            q.append(((nr, nc), moves + nm))
                    else:
                        continue
                    break

                seqs[(x, y)] = possis

        options = [seqs[(x, y)] for x, y in zip("A" + string, string)]
        # print(options)
        # print(list(product(*options)))
        return ["".join(x) for x in product(*options)]

    result = 0
    for line in input_str.splitlines():
        print(line)
        # print(solve(line, numpad))
        robot1 = solve(line, numpad)

        possible_robot2 = []
        for seq in robot1:
            possible_robot2 += solve(seq, dirpad)
        minlen = min(map(len, possible_robot2))
        # print(possible_robot2)
        robot2 = [string for string in possible_robot2 if len(string) == minlen]

        possible_robot3 = []
        for seq in robot2:
            possible_robot3 += solve(seq, dirpad)
        minlen = min(map(len, possible_robot3))
        numeric_part = int(re.findall(r"\d+", line)[0])

        result += minlen * numeric_part

    print(f"\nTotal Complexity: {result}")

    end_time = time.time()
    print(f"Part 1 execution time: {end_time - start_time} seconds")


def part2(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 2:")
    # Implement the logic here

    def compute_seqs(keypad):
        pos = {}
        for r in range(len(keypad)):
            for c in range(len(keypad[r])):
                if keypad[r][c] is not None:
                    pos[keypad[r][c]] = (r, c)
        seqs = {}
        for x in pos:
            for y in pos:
                if x == y:
                    seqs[(x, y)] = ["A"]
                    continue

                possis = []
                q = deque([(pos[x], "")])
                optimal = float("inf")
                while q:
                    (r, c), moves = q.popleft()

                    for nr, nc, nm in [
                        (r - 1, c, "^"),
                        (r + 1, c, "v"),
                        (r, c - 1, "<"),
                        (r, c + 1, ">"),
                    ]:
                        if (
                            nr < 0
                            or nc < 0
                            or nr >= len(keypad)
                            or nc >= len(keypad[0])
                        ):
                            continue
                        if keypad[nr][nc] == None:
                            continue
                        if keypad[nr][nc] == y:
                            if optimal < len(moves) + 1:
                                break
                            optimal = len(moves) + 1
                            possis.append(moves + nm + "A")
                        else:
                            q.append(((nr, nc), moves + nm))
                    else:
                        continue
                    break

                seqs[(x, y)] = possis
        return seqs

    def solve(string, seqs):
        options = [seqs[(x, y)] for x, y in zip("A" + string, string)]
        # print(options)
        # print(list(product(*options)))
        return ["".join(x) for x in product(*options)]

    # Define keypads
    numpad = [
        ["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        [None, "0", "A"],
    ]
    num_seqs = compute_seqs(numpad)

    dirpad = [
        [None, "^", "A"],
        ["<", "v", ">"],
    ]
    dir_seqs = compute_seqs(dirpad)

    dir_lengths = {key: len(value[0]) for key, value in dir_seqs.items()}

    @cache
    def compute_len(x, y, depth=25):
        if depth == 1:
            return dir_lengths[(x, y)]
        optimal = float("inf")
        for seq in dir_seqs[(x, y)]:
            length = 0
            for a, b in zip("A" + seq, seq):
                length += compute_len(a, b, depth - 1)

            optimal = min(optimal, length)

        return optimal

    result = 0
    for line in input_str.splitlines():
        print(line)
        # print(solve(line, numpad))
        inputs = solve(line, num_seqs)

        optimal = float("inf")

        for _ in range(25):
            for seq in inputs:
                length = 0
                for x, y in zip("A" + seq, seq):
                    length += compute_len(x, y)
                optimal = min(optimal, length)

        print(optimal)
        numeric_part = int(re.findall(r"\d+", line)[0])

        result += optimal * numeric_part

    print(f"\nTotal Complexity: {result}")

    result = 0
    print(f"Part 2 result is: {result}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")
