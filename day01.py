"""
AOC Advent of code 2023
Day 01
"""

from aoc import get_data
from collect import Collect


def filter_numbers(s: str):
    return Collect([c for c in s]).filter(lambda c: "0" <= c <= "9").map(lambda c: int(c))


def filter_numbers2(s: str):
    # print(s, len(s))
    orig = s
    num_dict = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digits = []
    for i, c in enumerate(s):
        if c.isdigit():
            digits.append(int(c))
        for d, val in enumerate(num_dict):
            if s[i:].startswith(val):
                digits.append(d)
    print(digits)
    return digits

    print(orig, filter_numbers(s))
    return filter_numbers(s)


def sum_list(lista):
    return lista.map(lambda x: 10*int(x[0]) + int(x[-1])) \
        .sum()


def part1():
    """
    Primera parte
    """
    data = get_data("day01_test.txt").filter_blanks()
    data = sum_list(data.map(lambda x: filter_numbers(x)))
    print(data)


def part2():
    """
    Segunda parte
    """
    data = get_data("day01.txt").filter_blanks()
    data = sum_list(data.map(lambda x: filter_numbers2(x)))
    print(data)


print('================================================')
# part1()
print('================================================')
part2()
