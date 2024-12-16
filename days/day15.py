import time
import os
import numpy as np
import imageio
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def grid_to_string(grid, curr_pos):
    temp_grid = [row[:] for row in grid]  # Create a copy of the grid
    temp_grid[curr_pos[0]][curr_pos[1]] = "@"  # Mark the current position
    return "\n".join("".join(row) for row in temp_grid)


def move_next(curr_pos, arrow):
    ads = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    dd = ads[arrow]
    return (curr_pos[0] + dd[0], curr_pos[1] + dd[1])


def parse_input(string):
    grid = []
    dirs = []
    start = tuple()
    grid_str, dirs_str = string.split("\n\n")
    for i, line in enumerate(grid_str.splitlines()):
        if "@" in line:
            for j in range(len(line)):
                if line[j] == "@":
                    start = (i, j)

        grid.append(list(line))

    dirs = list(dirs_str.replace("\n", "").strip())
    return np.array(grid), np.array(dirs), np.array(start)


def move_robo(g, arrows, start):
    curr_pos = start
    for ar in arrows:

        # try to move in arrow direction
        next_pos = move_next(curr_pos, ar)

        if g[next_pos] == "#":
            continue
        elif g[next_pos] == ".":
            # moving is possible
            curr_pos = next_pos
        elif g[next_pos] == "O":
            # robot can move boxes, any count of them, if at the other end there is '.'
            temp_posi = next_pos
            steps = 0
            # boxes_to_be_moved = [next_pos]
            while True:
                # boxes_to_be_moved.append(next_pos)

                if g[next_pos] == ".":
                    # all boxes can move in arrow direction
                    g[next_pos] = "O"
                    g[temp_posi] = "."
                    curr_pos = temp_posi
                    break

                elif g[next_pos] == "#":
                    # nothing moves!
                    break
                else:
                    # it is an 'O'

                    next_pos = move_next(next_pos, ar)
        else:
            exit("This tile is not defined!")

        # pretty print grid to see its update
        # print(f"run={i} - arrow={ar}")
        # print(grid_to_string(g.copy(), curr_pos))
        # print()


def part1(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 1:")
    # Implement the logic here

    grid, dirs, start = parse_input(input_str)
    # print(start)
    grid[start[0], start[1]] = "."  # start has @ sign
    # print(grid)

    # exit(0)
    # print(grid, dirs)
    # exit(0)

    # move through grid
    move_robo(grid, dirs, start)

    # result is position of 'O's -> 100*i + j
    result = 0
    for i, row in enumerate(grid):
        for j, ch in enumerate(row):
            if ch == "O":
                result += i * 100 + j

    print(f"Part 1 result is: {result}")

    end_time = time.time()
    print(f"Part 1 execution time: {end_time - start_time} seconds")


def parse_input2(string):
    # expand '#', '.', 'O'
    grid = []
    dirs = []
    start = tuple()
    grid_str, dirs_str = string.split("\n\n")
    for i, line in enumerate(grid_str.splitlines()):
        temp = []
        for j, ch in enumerate(line):
            if ch == "@":
                start = (i, j)

            # double all
            if ch == "#":
                temp += list("##")
            elif ch == ".":
                temp += list("..")
            elif ch == "@":
                temp += list("@.")
            elif ch == "O":
                temp += list("[]")
            else:
                exit("Character not defined!")
            # elif ch == '@':
            #     temp.append('@.')
        grid.append(temp)

    dirs = list(dirs_str.replace("\n", "").strip())
    return np.array(grid), np.array(dirs), np.array(start)


def move_robo2(g, arrows, start):
    curr_pos = start
    r, c = curr_pos

    ads = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

    for i, ar in enumerate(arrows):

        # try to move in arrow direction
        targets = [curr_pos]
        valid = True

        for cr, cc in targets:
            # tpos = (cr, cc)
            dr, dc = ads[ar]
            # next_tpos = move_next(tpos, ar)
            nr, nc = (cr + dr, cc + dc)

            # if next_pos is already included in targets, skip!
            if (nr, nc) in targets:
                continue

            ch = g[nr][nc]

            if ch == "#":
                valid = False
                break

            if ch == "[":
                targets.append((nr, nc))
                targets.append((nr, nc + 1))

            if ch == "]":
                targets.append((nr, nc))
                targets.append((nr, nc - 1))

        if not valid:
            continue

        r, c = curr_pos
        g[r][c] = "."

        copied_g = g.copy()
        # copied_g = np.array(
        #     [np.array(list(row)) for row in g]
        # )  # or from copy import deepcopy -> deepcopy is slow

        # update the boxes:
        for br, bc in set(targets[1:]):
            g[br][bc] = "."
        for br, bc in set(targets[1:]):
            # nbr, nbc = move_next((br, bc), ar)
            dr, dc = ads[ar]
            nbr, nbc = (br + dr, bc + dc)
            g[nbr][nbc] = copied_g[br][bc]

        curr_pos = move_next(curr_pos, ar)
        # update the @ of the robot?
        # would be: g[next_pos]

        # pretty print grid to see its update
        # print(f"run={i} - arrow={ar}")
        # print(grid_to_string(g.copy(), curr_pos))
        # print()


def part2(input_str):
    start_time = time.time()
    filename = os.path.basename(__file__)
    day_num = filename.replace("day", "").replace(".py", "").strip()
    print(f"Day {day_num}, Part 2:")
    # Implement the logic here

    grid, dirs, start = parse_input2(input_str)
    start = (start[0], start[1] * 2)
    print(start)
    # find pos of @ => start:
    # print(np.where(grid == "@"))

    grid[start[0], start[1]] = "."  # start has @ sign

    # move through grid (no video)
    # move_robo2(grid, dirs, start)

    # if you want to see what is happening:
    # fn = "lanternfish_robo_moves_boxes_part2_test.mp4"
    fn = "lanternfish_robo_moves_boxes_part2.mp4"
    fps = 30
    create_video(grid, dirs, start, filename=fn, fps=fps)

    # result is position of 'O's -> 100*i + j
    result = 0
    for i, row in enumerate(grid):
        for j, ch in enumerate(row):
            if ch == "[":
                result += i * 100 + j

    print(f"Part 2 result is: {result}")

    end_time = time.time()
    print(f"Part 2 execution time: {end_time - start_time} seconds")


def create_video(
    g,
    arrows,
    start,
    path="./videos",
    filename="lanternfish_robo_moves_boxes_part2.mp4",
    fps=60,
):
    os.makedirs(os.path.expanduser(path), exist_ok=True)
    filepath = os.path.join(os.path.expanduser(path), filename)

    images = []  # Create the video

    # - logic to move (code) starts here - #
    curr_pos = start
    r, c = curr_pos

    ads = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

    for i, ar in enumerate(arrows):

        fig, ax = plt.subplots()
        ax.set_facecolor("white")  # Set the background color to white

        # ax.imshow(g == "#", cmap="gray", interpolation="nearest")# Mark the walls with rectangular patches
        wall_positions = np.argwhere(g == "#")
        for pos in wall_positions:
            rect = patches.Rectangle(
                (pos[1] - 0.5, pos[0] - 0.5),
                1,
                1,
                linewidth=1,
                edgecolor="grey",
                facecolor="grey",
            )
            ax.add_patch(rect)

        # Mark the current position of the robot
        ax.scatter(curr_pos[1], curr_pos[0], color="red", label="Robot", s=100)

        # Mark the left boxes
        left_box_positions = np.argwhere(g == "[")
        for pos in left_box_positions:
            ax.scatter(pos[1], pos[0], color="blue", label="Box(left)", s=100)
        # Mark the right boxes
        right_box_positions = np.argwhere(g == "]")
        for pos in right_box_positions:
            ax.scatter(pos[1], pos[0], color="blue", label="Box(right)", s=100)

        # Mark the empty spaces
        empty_positions = np.argwhere(g == ".")
        for pos in empty_positions:
            ax.scatter(pos[1], pos[0], color="white", label="Empty", s=100)

        ax.set_aspect("equal")
        plt.axis("off")

        # Save the current frame
        frame_path = f"/tmp/frame_{i}.png"
        plt.savefig(frame_path)
        plt.close(fig)
        images.append(imageio.imread(frame_path))

        # try to move in arrow direction
        targets = [curr_pos]
        valid = True

        for cr, cc in targets:
            # tpos = (cr, cc)
            dr, dc = ads[ar]
            # next_tpos = move_next(tpos, ar)
            nr, nc = (cr + dr, cc + dc)

            # if next_pos is already included in targets, skip!
            if (nr, nc) in targets:
                continue

            ch = g[nr][nc]

            if ch == "#":
                valid = False
                break

            if ch == "[":
                targets.append((nr, nc))
                targets.append((nr, nc + 1))

            if ch == "]":
                targets.append((nr, nc))
                targets.append((nr, nc - 1))

        if not valid:
            continue

        r, c = curr_pos
        g[r][c] = "."

        copied_g = g.copy()
        # copied_g = np.array(
        #     [np.array(list(row)) for row in g]
        # )  # or from copy import deepcopy -> deepcopy is slow

        # update the boxes:
        for br, bc in set(targets[1:]):
            g[br][bc] = "."
        for br, bc in set(targets[1:]):
            # nbr, nbc = move_next((br, bc), ar)
            dr, dc = ads[ar]
            nbr, nbc = (br + dr, bc + dc)
            g[nbr][nbc] = copied_g[br][bc]

        curr_pos = move_next(curr_pos, ar)

    # - logic to move (code) ends here - #

    imageio.mimsave(filepath, images, fps=fps)
    print(f"Video saved to {filepath}")
