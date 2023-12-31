"""
AOC Advent of code 2023
Day 08
"""

# from dataclasses import dataclass
from aoc import get_data
from collection import Collection


def proc_data(data: Collection):
    """
    Funcion para procesar archivo de input
    """
    instructions = data.all().pop(0)
    mapa_tmp = data.filter_blanks() \
        .map(lambda lin: lin.replace(" ", "").replace("(", "").replace(")", "")) \
        .map(lambda e: (e.split("=")[0], e.split("=")[1].split(","))) \
        .map(lambda e: (e[0], (e[1][0], e[1][1])))
    mapa = {}
    for e in mapa_tmp:
        mapa[e[0]] = e[1]
    return {"ins": instructions, "map": mapa}


def part1():
    """
    Primera parte
    """
    data = get_data("day08.txt").process(proc_data)
    print(data)
    pos = "AAA"
    found = False
    count = 0
    i = 0
    while not found:
        if not i < len(data["ins"]):
            i = 0
            # print(count)

        ins = data["ins"][i]
        count += 1
        idx = 0 if ins == "L" else 1

        new_pos = data["map"][pos][idx]
        # print(ins, pos, new_pos)
        if new_pos == "ZZZ":
            found = True
        pos = new_pos
        i += 1

    print(f"Found at movement {count}")


def lcm(x, y):
    return (x * y) // gcd(x, y)


def gcd(x, y):
    while (y):
        x, y = y, x % y
    return x


def part2():
    """
    Segunda parte
    """
    data = get_data("day08.txt").process(proc_data)
    start = Collection(list(data["map"].keys())).filter(lambda x: x[2] == "A").all()
    print(data)
    print(start)
    print(data["ins"])

    finished = {}
    for s in start:
        finished[s] = []
        pos = s
        found = False
        count = 0
        i = 0
        while not found:
            if not i < len(data["ins"]):
                i = 0
                # print("reset i", i)
            count += 1

            idx = 0 if data["ins"][i] == "L" else 1

            pos = data["map"][pos][idx]
            if pos[2] == "Z":
                # print(s, pos, i, count, pos)
                finished[s] = count
                found = True
                print(s, pos, i, count, len(data["ins"]), finished[s])

            i += 1

    print(finished)
    steps = [i for k, i in finished.items()]
    print(steps)
    print((steps[0], steps[1]))
    print(lcm(steps[0], steps[1]))
    init = -1
    for s in steps:
        if init == -1:
            init = s
        print(init, s)
        least = lcm(init, s)
        print(init, s, least)
        init = least


print('================================================')
# part1()
print('================================================')
part2()
