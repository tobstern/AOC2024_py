import time
import os
from warnings import warn


def get_combo_op(regis, num):
    # num = num
    if 0 <= num <= 3:
        return num
    elif 4 <= num <= 6:
        s = {4: "A", 5: "B", 6: "C"}
        return regis[s[num]]
    # else:
    #     return num
    else:
        # warn(f"This value {num} of combo operand is not valid/ is reserved!")
        # raise RuntimeError("Not a valid combo operation", num)
        return -1


def part1(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here

    regis_str, instrus_str = input_str.split("\n\n")
    regis = {}
    reg_ch = ["A", "B", "C"]
    for i, line in enumerate(regis_str.strip().splitlines()):
        # print(line)
        regis[reg_ch[i]] = int(line.strip().split(": ")[1])

    instrus = list(map(int, instrus_str.split(": ")[1].strip().split(",")))

    print(regis)
    print(instrus)

    regis["A"] = 100
    regis["B"] = 0
    regis["C"] = 0

    # start opcode:
    out = []
    ip = 0
    while ip < len(instrus):
        # i = ip

        # check current and next
        cn = instrus[ip]
        # print(f"ip-cn={ip}")
        ip += 1
        combo_op = instrus[ip]
        # print(f"ip-comb_op={ip}")
        ip += 1

        # print()
        # print(f"curr={cn} - next={combo_op}")
        # print(f"ip={ip}")

        # get combo operand:
        nn = get_combo_op(regis, combo_op)

        # impl opcodes
        if cn == 0:
            # adv:
            regis["A"] = regis["A"] >> nn
        elif cn == 1:
            # bxl
            regis["B"] ^= combo_op
        elif cn == 2:
            # bst
            regis["B"] = nn % 8  # == nn & 7
        elif cn == 3:
            # jnz
            if regis["A"] == 0:
                pass
            else:
                ip = nn

        elif cn == 4:
            # bxc
            # legacy reasons: read combo operand
            regis["B"] = regis["B"] ^ regis["C"]
        elif cn == 5:
            # out, output comma separated
            out.append(nn % 8)  # truncated to 3 bit == & 7
            # print(f"output: {out}")
        elif cn == 6:
            # bdv
            regis["B"] = regis["A"] >> nn
        elif cn == 7:
            # cdv
            regis["C"] = regis["A"] >> nn

        # ip += 2

    # result = ",".join(out)
    print(regis)
    print(f"Part 1 result is:")
    print(*out, sep=",")

    end_time = time.time()
    print(f"Part 1 execution time: {end_time - start_time} seconds")


import re


def part2(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 2:")
    # Implement the logic here

    # regis_str, instrus_str = input_str.split("\n\n")
    # regis = {}
    # reg_ch = ["A", "B", "C"]
    # for i, line in enumerate(regis_str.strip().splitlines()):
    #     # print(line)
    #     regis[reg_ch[i]] = int(line.strip().split(": ")[1])

    # instrus = list(map(int, instrus_str.split(": ")[1].strip().split(",")))
    inp = list(map(int, re.findall(r"\d+", input_str)[3:]))

    print(inp)
    # exit()
    # print(regis)
    # print(instrus)

    # start opcode:
    result = 0

    # for Aval in range(37_000_000_000_000, 38_000_000_000_000, 1): 266_932_601_404_433
    # THX to HyperNeutrino!
    # So, I did reverse engineer my program and then applied HyperNeutrinos recursive function,
    # for finding the next possible A register value - based on matching it to the program value.
    def find(program, ans):
        if program == []:
            return ans

        for t in range(8):
            a = ans << 3 | t

            b = a % 8
            b = b ^ 3
            c = a >> b
            # a = a >> 3 # this operation can be anywhere from here till end (so it moved first op here).
            b = b ^ 4

            b = b ^ c

            if b % 8 == program[-1]:
                sub = find(program[:-1], a)
                if sub == None:
                    continue
                return sub

    result = find(inp, 0)
    print(f"Part 2 result is: {result}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")
