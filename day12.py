"""
AOC Advent of code 2023
Day 12
"""

# from dataclasses import dataclass
from aoc import get_data
from collection import Collection


def proc_data(data: Collection) -> 'Collection':
    """
    Funcion para procesar archivo de input
    """
    return data.filter_blanks() \
        .map(lambda line: line.split(' ')) \
        .map(lambda elem: (elem[0], tuple([int(n) for n in elem[1].split(',')])))


cache = {}


def count(cfg: str, nums: tuple, indent: int) -> int:
    # print(f"Called count: cfg:{cfg}  nums:{nums}")
    if cfg == '':
        return 1 if nums == () else 0

    if nums == ():
        return 0 if "#" in cfg else 1

    key = (cfg, nums)
    if key in cache:
        return cache[key]

    result = 0

    if cfg[0] in ".?":
        # print(f"   Cond 1: cfg[0] {cfg[0]} in .?")
        result += count(cfg[1:], nums, indent + 1)

    if cfg[0] in "#?":
        if nums[0] <= len(cfg) and "." not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != "#"):
            # print(f"   Cond 2:")
            # print(f"   Cond 2: nums[0] {nums[0]} <= len(cfg) {len(cfg)} AND . not in {cfg[:nums[0]]} AND (nums[0] {nums[0]} == len(cfg) {len(cfg)} OR cfg[nums[0]] {cfg[nums[0]]} != #)")
            result += count(cfg[nums[0] + 1:], nums[1:], indent + 1)

    spaces = "  " * (indent + 1)
    # print(f"{spaces}Called count: cfg:{cfg}  nums:{nums}  result:{result}")
    # print(f"   Called count return: result:{result}")
    cache[key] = result

    return result


def part1(use_test_data: bool) -> None:
    """
    Primera parte
    """
    data = get_data(test=use_test_data).process(proc_data)
    print(data)
    total = 0
    for springs, datos in data:
        print(springs, datos)
        print(count(springs, datos, 0))
        total += count(springs, datos, 0)
    print(total)


def part2(use_test_data: bool) -> None:
    """
    Segunda parte
    """
    data = get_data(test=use_test_data).process(proc_data)
    print(data)
    total = 0
    for springs, datos in data:
        springs = "?".join([springs] * 5)
        datos *= 5
        print(springs, datos)
        print(count(springs, datos, 0))
        total += count(springs, datos, 0)
    print(total)


if __name__ == "__main__":
    is_test = False
    print('================================================')
    # part1(is_test)
    print('================================================')
    part2(is_test)
