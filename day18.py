"""
AOC Advent of code 2023
Day 18
"""

# from dataclasses import dataclass
from sys import argv
from aoc import get_data
from collection import Collection
from mapa import Mapa, Pos



def proc_data(data: Collection) -> Collection:
    """
    Funcion para procesar archivo de input
    """
    return data.filter_blanks()


class PoolMap(Mapa):
    data: Collection

    def __init__(self, data: Collection):
        self.data = data
        grid = self.grid_from_instructions(data)
        super().__init__(grid)

    def grid_from_instructions(self, data: Collection) -> Mapa:
        dirs = {'R': 1, 'L': -1, 'U': -1, 'D': 1}
        max_x: int = 0
        max_y: int = 0
        x: int = 0
        y: int = 0
        for direction, steps, color in data:
            if direction in "RL":
                x += steps * dirs[direction]
                max_x = max(max_x, x)
            if direction in "UD":
                y += steps * dirs[direction]
                max_y = max(max_y, y)
        return Mapa.new(".", max_x + 1, max_y + 1).mapa

    def process_borders(self) -> "PoolMap":
        dirs = {'R': Pos(1, 0), 'L': Pos(-1, 0), 'U': Pos(0, -1), 'D': Pos(0, 1)}
        position = Pos(0, 0)
        self.set_value(position, "#")
        for direction, steps, color in self.data:
            for _ in range(steps):
                position += dirs[direction]
                self.set_value(position, "#")
        return self

    def dig(self) -> "PoolMap":
        for j in range(self.rows):
            interior = False
            for i in range(self.cols):
                elem = self.get_value(Pos(i, j))
                if elem == "#":
                    interior = not interior
                if elem == "." and interior:
                    self.set_value(Pos(i, j), "#")

        return self

    def count_digs(self) -> int:
        count = 0
        for line in self.mapa:
            for elem in line:
                if elem == "#":
                    count += 1
        return count


def part1(filename: str) -> None:
    """
    Primera parte
    """
    data = get_data(filename=filename).process(proc_data) \
        .map(lambda line: tuple(line.split(" "))) \
        .map(lambda line: (line[0], int(line[1]), line[2]))
    print(data)
    mapa = PoolMap(data).process_borders()
    print(mapa)
    mapa.dig()
    print(mapa, mapa.count_digs())


def part2(filename: str) -> None:
    """
    Segunda parte
    """
    data = get_data(filename=filename).process(proc_data)
    print(data)


if __name__ == "__main__":
    print('================================================')
    part1(argv[1])
    print('================================================')
    # part2(argv[1])
