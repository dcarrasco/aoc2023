"""
AOC Advent of code 2023
Day 06
"""

from aoc import get_data
from collection import Collection
from dataclasses import dataclass
from math import sqrt


def proc_data(data: Collection) -> dict:
    data2 = data.filter_blanks() \
        .map(lambda lin: lin.split(":")[1].strip().split(" ")) \
        .map(lambda lst: [int(e) for e in lst if e != ""])
    return list(zip(data2[0], data2[1]))


def proc_data2(data: Collection):
    return data.filter_blanks() \
        .map(lambda lin: lin.split(":")[1].strip().split(" ")) \
        .map(lambda lst: "".join([e for e in lst if e != ""])) \
        .all()



def part1():
    """
    Primera parte
    """
    data = get_data("day06-test.txt").process(proc_data)
    print(data)
    data2 = [[(i,i*(race[0]-i)) for i in range(race[0]+1) if i*(race[0]-i) > race[1]] for race in data]
    print(data2)
    print(Collection([len(race) for race in data2]).mult())


def part2():
    """
    Segunda parte
    """
    data = get_data("day06.txt").process(proc_data2)
    print(data)
    data3 = Collection([(int(data[0]), int(data[1]))]) \
        .dump() \
        .map(lambda r: ((r[0] - sqrt(r[0]**2 - 4*r[1]))/2, (r[0] + sqrt(r[0]**2 - 4*r[1]))/2)) \
        .dump() \
        .map(lambda r: (int(r[0]) + (1 if r[0] - int(r[0]) != 0 else 0), int(r[1]) + (1 if r[1] - int(r[1]) != 0 else -1))) \
        .dump() \
        .map(lambda r: r[1] - r[0]) \
        .dump()
    print(data3.mult())


print('================================================')
# part1()
print('================================================')
part2()
