import time
import os


def part1(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here

    rules_str, instr_str = input_str.split("\n\n")
    # print(rules_str)
    # print("-------------")
    # print(instr_str)

    # save all rules to a dict keys are nums and values are list
    rules = dict()
    for i, line in enumerate(rules_str.strip().splitlines()):
        left, right = line.split("|")
        left, right = int(left), int(right)
        # rules[int(left)].append(int(right))
        if left not in rules.keys():
            rules[left] = [right]
        else:
            rules[left].append(right)

    # print(rules)

    # instructions to list of ints
    instr = []
    for line in instr_str.splitlines():
        # print(line.split(","))
        instr.append(list(map(int, line.split(","))))

    # print(instr)
    # check if next num is in current dict.values()
    result = 0
    for i, line in enumerate(instr):
        mid_idx = len(line) // 2

        # print(line)
        last_nums = [line[0]]
        valid = True
        for j in range(1, len(line)):

            # print(rules.get(line[j]))
            if rules.get(line[j]) == None:
                # the number is not existing as key - so no num has to be prior to it
                last_nums.append(line[j])
                continue

            # print(f"j={j} --- last_nums are:", last_nums, f"curr_num is: {line[j]}")
            if any([1 if ele in rules[line[j]] else 0 for ele in last_nums]):
                valid = False
                break

            last_nums.append(line[j])

        if valid:
            # print(f"line {i+1} is valid", line[mid_idx])
            # is valid line - save mid num
            result += line[mid_idx]

    print(f"Part 1 result is: {result}")

    end_time = time.time()
    print(f"Part 1 execution time: {end_time - start_time} seconds")


def part2(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here
    # Your part2 logic here

    result = ""
    print(f"Part 2 result is: {result}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")
