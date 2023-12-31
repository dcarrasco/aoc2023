"""
AOC Advent of code 2023
Day 05
"""

from aoc import get_data
from collection import Collection
# from dataclasses import dataclass


def proc_data(data: Collection) -> dict:
    n_map = last_map = -1
    maps = []
    for i, line in data.enumerate():
        if i == 0:
            seeds = [int(s) for s in line.split(":")[1].strip().split(" ")]
            # print(seeds)
        else:
            if line == "":
                n_map += 1
            else:
                if n_map != last_map:
                    maps.append(Map(line.split(" ")[0]))
                else:
                    maps[n_map].add_rule(line)
                # print("map:", n_map, line)
                last_map = n_map

    return {"seeds": seeds, "almanaq": Almanaq(maps)}


class Almanaq:
    maps: None

    def convert(self, number):
        for m in self.maps:
            number = m.convert(number)
        return number

    def convert_range(self, range):
        if type(range) is tuple:
            range = [(range[0], range[0] + range[1] - 1, 0)]
        for m in self.maps:
            # print(f"almanaq {m}")
            new_range = []
            for r in range:
                new_range += m.convert_range(r)
            range = new_range
            # print(f"\tend map --> range: {range}")
            range2 = [(r[0]+r[2], r[1]+r[2], 0) for r in range]
            # print(f"\tend map --> range2: {range2}")
            range = range2

        # print(range, type(range), self.maps)
        return range

    def __init__(self, maps):
        self.maps = maps

    def __repr__(self):
        return f"{self.maps}"


class Map:
    name: str = None
    map_from: str = None
    map_to: str = None
    rules = None

    def add_rule(self, rule):
        self.rules.append(Rule([int(r) for r in rule.split(" ")]))

    def convert(self, number):
        new_number = number
        for r in self.rules:
            if r.has_number(number):
                new_number = r.convert(number)
        return new_number

    def convert_range(self, range):
        # print(f"{type(range)}")
        if type(range) is tuple:
            range = [range]
        # print(f"\tmap range: {range}")
        for r in self.rules:
            map_new_range = []
            for ran in range:
                map_new_range += r.convert_range(ran)
            range = map_new_range
            # print(f"\tmap finish ranges: {map_new_range}")
        return map_new_range

    def __init__(self, name):
        self.rules = []
        self.name = name
        self.map_from = name.split("-")[0]
        self.map_to = name.split("-")[2]

    def __str__(self):
        rules = [str(r) for r in self.rules]
        return f"{self.name} {rules}"

    def __repr__(self):
        return str(self)


class Rule:
    source: int = 0
    dest: int = 0
    rule_range: int = 0

    def has_number(self, number):
        return self.source <= number <= self.source + self.rule_range - 1

    def convert(self, number):
        return self.dest - self.source + number

    def convert_range(self, range):
        delta_orig = range[2]
        delta = self.dest - self.source
        rule_min = self.source
        rule_max = self.source + self.rule_range - 1
        range_min = range[0]
        range_max = range[1]
        rule_ranges = []
        if rule_max < range_min or rule_min > range_max:
            return [range]
        else:
            if rule_min >= range_min:
                rule_ranges.append((range_min, rule_min, delta_orig))
                if rule_max <= range_max:
                    rule_ranges.append((rule_min, rule_max, delta_orig + delta))
                    rule_ranges.append((rule_max, range_max, delta_orig))
                else:
                    rule_ranges.append((rule_min, range_max, delta_orig + delta))
            else:
                if rule_max <= range_max:
                    rule_ranges.append((range_min, rule_max, delta_orig + delta))
                    rule_ranges.append((rule_max, range_max, delta_orig))
                else:
                    rule_ranges.append((range_min, range_max, delta_orig + delta))
        return rule_ranges

    def __init__(self, datos):
        self.dest = int(datos[0])
        self.source = int(datos[1])
        self.rule_range = int(datos[2])

    def __str__(self):
        return f"s:{self.source} d:{self.dest} r:{self.rule_range}"


def part1():
    """
    Primera parte
    """
    data = get_data("day05.txt").process(proc_data)
    print(data, data["almanaq"])
    result = Collection([data["almanaq"].convert(s) for s in data["seeds"]]).min()
    print(result)


def part2():
    """
    Segunda parte
    """
    data = get_data("day05.txt").process(proc_data)
    seeds = []
    i = 0
    while i < len(data["seeds"]):
        seeds.append((data["seeds"][i], data["seeds"][i + 1]))
        i += 2
    print(seeds)
    new_seeds = []
    for s in seeds:
        new_seeds += data["almanaq"].convert_range(s)
    print(new_seeds)
    for ns in new_seeds:
        print(ns)
    print(Collection(new_seeds).filter(lambda ns: ns[0] != 0).map(lambda e: e[0] + e[2]).min())


print('================================================')
# part1()
print('================================================')
part2()
