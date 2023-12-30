"""
AOC Advent of code 2023
Day 09
"""

from dataclasses import dataclass
from aoc import get_data
from collection import Collection


def proc_data(data: Collection):
    """
    Funcion para procesar archivo de input
    """
    return data.filter_blanks().map(lambda x: [[int(y) for y in x.split(" ")]])


def get_differences(data):
    new_data = data
    for report in new_data:
        rep_n = 0

        finished = False
        while not finished:
            new_report = []
            for i in range(len(report[rep_n])):
                if i > 0:
                    new_report.append(report[rep_n][i] - report[rep_n][i-1])
            report.append(new_report)

            check_zeroes = True
            for item in new_report:
                if item != 0:
                    check_zeroes = False

            if not check_zeroes:
                rep_n += 1
            else:
                finished = True

    return new_data


def part1():
    """
    Primera parte
    """
    data = get_data("day09-test.txt").process(proc_data).all()
    data = get_differences(data)
    for report in data:
        last = 0
        for j in range(len(report), 0, -1):
            # print(j, report[j-1], report[j-1][-1])
            report[j-1].append(report[j-1][-1] + last)
            last = report[j-1][-1]

    print(data)
    print(Collection(data).map(lambda h: h[0][-1]).sum())


def part2():
    """
    Segunda parte
    """
    data = get_data("day09.txt").process(proc_data)
    data = get_differences(data.all())

    for report in data:
        last = 0
        for j in range(len(report), 0, -1):
            # print(j, report[j-1], report[j-1][-1])
            new_report = [report[j-1][0] - last]
            new_report.extend(report[j-1])
            report[j-1] = new_report
            last = report[j-1][0]

    print(data)
    print(Collection(data).map(lambda h: h[0][0]).sum())


print('================================================')
# part1()
print('================================================')
part2()
