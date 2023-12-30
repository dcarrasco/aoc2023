"""
AOC Advent of code 2023
Day 02
"""

from aoc import get_data
from collect import Collect
# from dataclasses import dataclass


class Game:
    id: int
    gamesets = None

    def __init__(self, line: str):
        self.gamesets = []
        (game_string, sets_string) = line.split(":")
        self.id = int(game_string.strip().split(" ")[1].strip())
        for i, sets in enumerate(sets_string.strip().split(";")):
            self.gamesets.append(Gameset(sets.strip()))

    def check(self, pack):
        checked = True
        for gs in self.gamesets:
            checked = checked and gs.check(pack)
        return checked

    def power(self):
        max_red: int = 0
        max_green: int = 0
        max_blue: int = 0

        for gs in self.gamesets:
            print(gs)
            if int(gs.red) > int(max_red):
                max_red = int(gs.red)
            if int(gs.green) > int(max_green):
                max_green = int(gs.green)
            if int(gs.blue) > int(max_blue):
                max_blue = int(gs.blue)

        return max_red * max_green * max_blue

    def __str__(self):
        return f"G:{self.id} [" + ",".join([str(gs) for gs in self.gamesets]) + "]"


class Gameset:
    red: int = 0
    green: int = 0
    blue: int = 0

    def __init__(self, line: str):
        # print(line)
        for d in line.split(","):
            self.add_color(d.strip().split(" "))

    def check(self, pack):
        return int(self.red) <= int(pack.red) and int(self.green) <= int(pack.green) and int(self.blue) <= int(pack.blue)

    def add_color(self, color_array):
        if color_array[1] == "red":
            self.red = color_array[0]
        elif color_array[1] == "green":
            self.green = color_array[0]
        elif color_array[1] == "blue":
            self.blue = color_array[0]

    def __str__(self):
        return f"R({self.red}) G({self.green}) B({self.blue})"


def part1():
    """
    Primera parte
    """
    data = get_data("day02.txt").filter_blanks()
    # print(data)
    games = []
    for line in data:
        # print(l)
        games.append(Game(line))
    pack = Gameset("12 red, 13 green, 14 blue")
    # print(pack)
    print(Collect(games).filter(lambda g: g.check(pack)).map(lambda g: g.id).sum())


def part2():
    """
    Segunda parte
    """
    data = get_data("day02.txt").filter_blanks()
    games = []
    for line in data:
        games.append(Game(line))
    print(Collect(games).map(lambda g: g.power()).sum())


print('================================================')
part1()
print('================================================')
part2()
