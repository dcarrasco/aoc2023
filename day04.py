"""
AOC Advent of code 2023
Day 04
"""

from aoc import get_data
from collection import Collection
# from dataclasses import dataclass


def proc_data(data: Collection) -> dict:
    return data.map(lambda s: Card(s))

class Card:
    id: str = None
    winner: str = None
    game: str = None
    q_winning: int = 0
    copies: int = 0

    def __init__(self, text: str):
        id, card = text.split(":")
        self.id = id
        winner, game = card.strip().split("|")
        self.winner = [int(n) for n in winner.strip().split(" ") if n != ""]
        self.game = [int(n) for n in game.strip().split(" ") if n != ""]
        self.get_q_winning()

    def get_q_winning(self):
        for w in self.game:
            for g in self.winner:
                if g == w:
                    self.q_winning += 1

    def __str__(self):
        return f"id:{self.id} w:{self.winner} g:{self.game} q_w:{self.q_winning} c:{self.copies}"


def part1():
    """
    Primera parte
    """
    data = get_data("day04.txt").filter_blanks().process(proc_data).dump()
    print(data.map(lambda c: 2**(c.q_winning - 1) if c.q_winning > 0 else 0).sum())


def part2():
    """
    Segunda parte
    """
    data = get_data("day04.txt").filter_blanks().process(proc_data).dump()
    for i, c in data.enumerate():
        print(i, c)
        for j in range(c.q_winning):
            data[i + j + 1].copies += 1 + c.copies
    print(data.map(lambda c: c.copies + 1).sum())


print('================================================')
# part1()
print('================================================')
part2()
