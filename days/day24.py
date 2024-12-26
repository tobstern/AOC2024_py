import time
import os


def part1(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here

    wires_str, ops_str = input_str.split("\n\n")

    ini_wires = {
        ws.split(": ")[0]: int(ws.split(": ")[1])
        for ws in wires_str.splitlines()
    }
    gates = {}
    output = {}
    for line in ops_str.splitlines():
        conw_str, gout = line.split(" -> ")
        conw = conw_str.split(" ")
        # if gout not in gates:
        #    gates[gout] = []
        gates[gout] = conw
        output[gout] = None

    # print(ini_wires)
    # print(gates)

    actives = ini_wires

    while gates:
        gcopy = gates.copy()
        for gate, conwire in gcopy.items():
            left, op, right = conwire
            if left in actives and right in actives:
                if op == "XOR":
                    output[gate] = actives[left] ^ actives[right]
                elif op == "AND":
                    output[gate] = actives[left] & actives[right]
                elif op == "OR":
                    output[gate] = actives[left] | actives[right]
                else:
                    raise RuntimeError("This operation is not implemented!")

                actives[gate] = output[gate]
                del gates[gate]  # -> got its output, so done with this gate

    # print(len(output))
    output_sorted = sorted(output.items(), key=lambda x: x[0], reverse=True)
    # print(output_sorted)
    result = []
    for gate, v in output_sorted:
        if not gate.startswith("z"):
            break
        result.append(v)

    result = "".join([str(v) for k, v in output_sorted if k.startswith("z")])
    result = int(result, 2)
    # print({wire: val for wire, val in output.items() if wire.startswith("z")})
    print(f"Part 1 result is: {result}")

    end_time = time.time()
    print(f"Part 1 execution time: {end_time - start_time} seconds")


def part2(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 2:")
    # Implement the logic here

    # this is a copy and paste from HyperNeutrinos solution
    # maybe I will try to get my approach to work later...

    file = open("./puzzle_inputs/day24.txt", "r")

    for line in file:
        if line.isspace():
            break

    formulas = {}

    for line in file:
        x, op, y, z = line.replace(" -> ", " ").split()
        formulas[z] = (op, x, y)

    def make_wire(char, num):
        return char + str(num).rjust(2, "0")

    def verify_z(wire, num):
        # print("vz", wire, num)
        if wire not in formulas:
            return False
        op, x, y = formulas[wire]
        if op != "XOR":
            return False
        if num == 0:
            return sorted([x, y]) == ["x00", "y00"]
        return (
            verify_intermediate_xor(x, num)
            and verify_carry_bit(y, num)
            or verify_intermediate_xor(y, num)
            and verify_carry_bit(x, num)
        )

    def verify_intermediate_xor(wire, num):
        # print("vx", wire, num)
        if wire not in formulas:
            return False
        op, x, y = formulas[wire]
        if op != "XOR":
            return False
        return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

    def verify_carry_bit(wire, num):
        # print("vc", wire, num)
        if wire not in formulas:
            return False
        op, x, y = formulas[wire]
        if num == 1:
            if op != "AND":
                return False
            return sorted([x, y]) == ["x00", "y00"]
        if op != "OR":
            return False
        return (
            verify_direct_carry(x, num - 1)
            and verify_recarry(y, num - 1)
            or verify_direct_carry(y, num - 1)
            and verify_recarry(x, num - 1)
        )

    def verify_direct_carry(wire, num):
        # print("vd", wire, num)
        if wire not in formulas:
            return False
        op, x, y = formulas[wire]
        if op != "AND":
            return False
        return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

    def verify_recarry(wire, num):
        # print("vr", wire, num)
        if wire not in formulas:
            return False
        op, x, y = formulas[wire]
        if op != "AND":
            return False
        return (
            verify_intermediate_xor(x, num)
            and verify_carry_bit(y, num)
            or verify_intermediate_xor(y, num)
            and verify_carry_bit(x, num)
        )

    def verify(num):
        return verify_z(make_wire("z", num), num)

    def progress():
        i = 0

        while True:
            if not verify(i):
                break
            i += 1

        return i

    swaps = []

    for _ in range(4):
        baseline = progress()
        for x in formulas:
            for y in formulas:
                if x == y:
                    continue
                formulas[x], formulas[y] = formulas[y], formulas[x]
                if progress() > baseline:
                    break
                formulas[x], formulas[y] = formulas[y], formulas[x]
            else:
                continue
            break
        swaps += [x, y]

    print(",".join(sorted(swaps)))

    # print(f"Part 2 result is: {result}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")
