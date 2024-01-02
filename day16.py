"""
AOC Advent of code 2023
Day 16
"""

# from dataclasses import dataclass
from sys import argv
from aoc import get_data
from collection import Collection
from mapa import Mapa


def proc_data(data: Collection) -> Collection:
    """
    Funcion para procesar archivo de input
    """
    return data.filter_blanks()


class LightMap(Mapa):
    energized: Mapa
    energized_dir: Mapa

    def __init__(self, data: list):
        super().__init__(data)
        self.reset_energized()

    def reset_energized(self) -> None:
        energ = [["." for _ in range(self.ancho())] for _ in range(self.alto())]
        self.energized = Mapa(energ)
        energ_dir = [[dict() for _ in range(self.ancho())] for _ in range(self.alto())]
        self.energized_dir = Mapa(energ_dir)

    def count_energized(self, pos: tuple, dir: tuple) -> int:
        self.reset_energized()
        self.set_energized(pos, dir)

        suma = 0
        for linea in self.energized:
            for i in linea:
                suma += 1 if i == "#" else 0
        return suma

    def set_energized(self, pos: tuple, dir: tuple) -> None:
        finish = False
        while not finish \
                and 0 <= pos[0] < self.ancho() and 0 <= pos[1] < self.alto() \
                and dir not in self.energized_dir.get_value(pos):
            elem = self.get_value(pos)
            # print("  "*level, pos, dir, elem, self.energized_dir)
            self.energized.set_value(pos, "#")
            self.energized_dir.set_value(pos, {**self.energized_dir.get_value(pos), **{dir: 1}})
            # print(self.energized)
            if elem == "|" and dir in ((1, 0), (-1, 0)):
                self.set_energized((pos[0], pos[1] - 1), (0, -1))
                self.set_energized((pos[0], pos[1] + 1), (0, 1))
                finish = True
            elif elem == "-" and dir in ((0, 1), (0, -1)):
                self.set_energized((pos[0] - 1, pos[1]), (-1, 0))
                self.set_energized((pos[0] + 1, pos[1]), (1, 0))
                finish = True
            else:
                if elem == "/":
                    match dir:
                        case (1, 0): dir = (0, -1)
                        case (-1, 0): dir = (0, 1)
                        case (0, 1): dir = (-1, 0)
                        case (0, -1): dir = (1, 0)
                elif elem == "\\":
                    match dir:
                        case (1, 0): dir = (0, 1)
                        case (-1, 0): dir = (0, -1)
                        case (0, 1): dir = (1, 0)
                        case (0, -1): dir = (-1, 0)
                pos = (pos[0] + dir[0], pos[1] + dir[1])

    def max_energized(self):
        max_e = (0, (0, 0))
        for j in range(self.alto()):
            count = self.count_energized((0, j), (1, 0))
            if count > max_e[0]:
                max_e = (count, (0, j))

            count = self.count_energized((self.ancho() - 1, j), (-1, 0))
            if count > max_e[0]:
                max_e = (count, (self.ancho() - 1, j))

        for i in range(self.ancho()):
            count = self.count_energized((i, 0), (0, 1))
            if count > max_e[0]:
                max_e = (count, (i, 0))

            count = self.count_energized((i, self.alto() - 1), (0, -1))
            if count > max_e[0]:
                max_e = (count, (i, self.alto() - 1))
        return max_e


def part1(filename: str) -> None:
    """
    Primera parte
    """
    data = get_data(filename=filename).process(proc_data)
    print(data)
    mapa = LightMap(data.all())
    print(mapa)
    # mapa.set_energized((0, 0), (1, 0), 0)
    # print(mapa.count_energized())
    print(mapa.max_energized())




def part2(filename: str) -> None:
    """
    Segunda parte
    """
    data = get_data(filename=filename).process(proc_data)


if __name__ == "__main__":
    print('================================================')
    part1(argv[1])
    print('================================================')
    part2(argv[1])
