import time
import os


class Counter:

    def __init__(self):
        self.counts = {}

    def increment(self, key, value=1):
        if key in self.counts:
            self.counts[key] += value
        else:
            self.counts[key] = value

    def decrement(self, key, value=1):
        if key in self.counts:
            self.counts[key] -= value

            if self.counts[key] <= 0:
                del self.counts[key]
        else:
            raise KeyError(f"Key {key} not found in counter!")

    def get_counts(self, key):
        return self.counts.get(key, 0)

    def get_keys(self):
        return self.counts.keys()

    def get_vals(self):
        return self.counts.vals()

    def __repr__(self):
        return str(self.counts)


def part1(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here

    inp_list = list(map(int, list(input_str.strip())))
    # print(inp_list)

    result = []  # index * filenum
    # sort from last, in empty spaces:
    id_num = 0
    empty_posis = []
    files = []
    file_posis = []
    for i, num in enumerate(inp_list):

        if i % 2 == 0:
            # even index:
            # is a file with num
            files += [id_num] * num
            file_posis += [sum(inp_list[:i]) + j for j in range(0, num)]
            id_num += 1
        else:
            # odd index:
            # is num of empty space
            empty_posis += [sum(inp_list[:i]) + j for j in range(0, num)]

    # print(empty_posis)
    # print(file_posis)
    # print(files)

    result = 0
    c = 0
    while empty_posis and file_posis:
        if c in file_posis:
            result += file_posis[0] * files[0]

            # remove
            file_posis = file_posis[1:]
            files = files[1:]
        else:
            result += empty_posis[0] * files[-1]
            # remove
            empty_posis = empty_posis[1:]
            file_posis = file_posis[:-1]
            files = files[:-1]

        c += 1

    print(f"Part 1 result is: {result}")

    end_time = time.time()
    print(f"Part 1 execution time: {end_time - start_time} seconds")


# 6330658883068 too low


def find_and_subtract_empty_spaces(inp_list, space_end, le):
    empty_space_length = 0
    for i in range(space_end - le, space_end):
        if inp_list[space_end - 1] == 0:
            empty_space_length += 1
    return space_end - empty_space_length


def part2(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 2:")
    # Implement the logic here
    # Your part2 logic here

    # inp_list = list(map(int, list(input_str.strip())))
    # print(inp_list)

    # my approach did only work for the test input, so this is takrn from Hyper Neutrino:

    files = {}
    blanks = []

    fid = 0
    pos = 0

    for i, ch in enumerate(input_str.strip()):
        num = int(ch)
        if i % 2 == 0:
            # file
            if num == 0:
                raise ValueError("Unexpected num = 0 for file!")

            files[fid] = (pos, num)
            fid += 1
        else:
            # blank
            if num != 0:
                blanks.append((pos, num))
        pos += num

    # start the logic:
    while fid > 0:
        fid -= 1  # go from last
        pos, size = files[fid]
        for i, (start, length) in enumerate(blanks):
            if start >= pos:
                blanks = blanks[:i]
                break
            if size <= length:
                files[fid] = (start, size)
                if size == length:
                    blanks.pop(i)
                else:
                    blanks[i] = (start + size, length - size)
                break

    result = 0
    for fid, (pos, size) in files.items():
        for idx in range(pos, pos + size):
            result += idx * fid
    print(f"Part 2 result is: {result}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")
