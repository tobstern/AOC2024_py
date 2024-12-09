import time
import os
import copy


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


def bubble_sort(arr, rules):
    n = len(arr)

    # last_nums = [arr[0]]

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        # print(f"prior: {arr}")
        for j in range(0, n - i - 1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            # if arr[j] > arr[j+1]:

            # print(f"left={arr[j]} - right={arr[j+1]}")
            if rules.get(arr[j + 1]) == None:
                # the number is not existing as key - so no num has to be prior to it
                # last_nums.append(arr[j + 1])
                continue

            last_nums = arr[: j + 1]

            # print(f"i={i} - j={j}")
            # print(f"last_nums: {last_nums}")
            if any([1 if ele in rules[arr[j + 1]] else 0 for ele in last_nums]):

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                swapped = True

            # print(f"after: {arr}")
            # last_nums.append(arr[j + 1])

        if swapped == False:
            break


def part2(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 2:")
    # Implement the logic here
    # Your part2 logic here

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
    copied_instr = copy.deepcopy(instr)
    for i, line in enumerate(copied_instr):

        # is_valid = compare(rules, line)
        # last_nums = [line[0]]

        # print()
        # print(f"line={i+1}")
        bubble_sort(instr[i], rules)

        # instr[i] = sorted(instr[i], key=cmp_to_key(compare))
        # instr[i].sorted(instr[i], key=cmp_to_key(lambda left, right: compare(left, right, rules, last_nums)))

    for untouched, sorted_list in zip(copied_instr, instr):
        # has been changed, was invalid, add result
        # print("untouched", untouched)
        # print("sorted", sorted_list)
        if not (untouched == sorted_list):

            mid_idx = len(untouched) // 2
            result += sorted_list[mid_idx]

    print(f"Part 2 result is: {result}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")
