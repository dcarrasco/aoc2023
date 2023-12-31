"""
AOC Advent of code 2023
Day 03
"""

# from dataclasses import dataclass
from aoc import get_data
from collection import Collection


def proc_data(data: Collection) -> dict:
    numbers = []
    symbols = []
    for i, line in data.enumerate():
        number = ''
        pos = -1
        for p, c in enumerate(line):
            if c.isdigit():
                if pos == -1:
                    pos = p
                number += c
            else:
                if number != '':
                    numbers.append((number, (i, pos)))
                    number = ''
                    pos = -1
            if not c.isdigit() and c != '.':
                symbols.append((c, (i, p)))
        if number != '':
            numbers.append((number, (i, pos)))

    return {"numbers": numbers, "symbols": symbols}


def part1():
    """
    Primera parte
    """
    data = get_data("day03.txt").filter_blanks().process(proc_data)
    sum_part_numbers = 0
    for number in data["numbers"]:
        pos_min = (number[1][0] - 1, number[1][1] - 1)
        pos_max = (number[1][0] + 1, number[1][1] + len(str(number[0])) - 1 + 1)
        has_adjacent = False
        for symbol in data["symbols"]:
            if symbol[1][0] >= pos_min[0] and symbol[1][0] <= pos_max[0] \
                    and symbol[1][1] >= pos_min[1] and symbol[1][1] <= pos_max[1]:
                has_adjacent = True
        if has_adjacent:
            sum_part_numbers += int(number[0])
            print(number[0])
        # print(number[0], pos_min, pos_max, has_adjacent)
    # print(data)
    print(sum_part_numbers)


def part2():
    """
    Segunda parte
    """
    data = get_data("day03.txt").filter_blanks().process(proc_data)
    gears = Collection(data["symbols"]).filter(lambda s: s[0] == '*').all()
    for i, g in enumerate(gears):
        adjacents = []
        for n in data["numbers"]:
            pos_min = (n[1][0] - 1, n[1][1] - 1)
            pos_max = (n[1][0] + 1, n[1][1] + len(str(n[0])) - 1 + 1)
            if g[1][0] >= pos_min[0] and g[1][0] <= pos_max[0] and g[1][1] >= pos_min[1] \
                    and g[1][1] <= pos_max[1]:
                adjacents.append(n)
        gears[i] = (g[0], g[1], adjacents)

    gear_ratio = Collection(gears) \
        .filter(lambda g: len(g[2]) == 2) \
        .map(lambda g: (int(g[2][0][0]), int(g[2][1][0]))) \
        .map(lambda g: g[0] * g[1])

    print(gear_ratio.sum())


print('================================================')
# part1()
print('================================================')
part2()
