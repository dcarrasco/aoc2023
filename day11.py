"""
AOC Advent of code 2023
Day 11
"""

from dataclasses import dataclass
from aoc import get_data
from collection import Collection


@dataclass
class Galaxy():
    mapa: list[str]
    galaxias: list[tuple[int, tuple[int, int]]]

    def expand_mapa(self) -> None:
        self.mapa = self.expand_mapa_y()
        self.mapa = self.expand_mapa_x()

    def expand_mapa_y(self) -> list[str]:
        new_mapa: list[str] = []
        for s in self.mapa:
            if len(s) == len([c for c in s if c == '.']):
                new_mapa.append(''.join(['e' for _ in s]))
            else:
                new_mapa.append(s)
        print(new_mapa)
        return new_mapa

    def expand_mapa_x(self) -> list[str]:
        new_mapa: list[str] = ['' for s in self.mapa]
        for i in range(len(self.mapa[0])):
            row = ''.join([s[i] for s in self.mapa])
            for j, _ in enumerate(self.mapa):
                if len(self.mapa) == len([c for c in row if c == '.' or c == 'e']):
                    new_mapa[j] += 'e'
                else:
                    new_mapa[j] += self.mapa[j][i]
        return new_mapa

    def get_galaxias(self) -> None:
        count = 0
        for j, linea in enumerate(self.mapa):
            for i, c in enumerate(list(linea)):
                if c == "#":
                    count += 1
                    self.galaxias.append((count, (j, i)))

    def path_lengths(self, expansion: int = 0) -> dict[tuple[int, int], int]:
        paths_dict = {}
        for p1 in self.galaxias:
            for p2 in self.galaxias:
                if p1[0] != p2[0]:
                    min_x = min(p1[1][1], p2[1][1])
                    max_x = max(p1[1][1], p2[1][1])
                    min_y = min(p1[1][0], p2[1][0])
                    max_y = max(p1[1][0], p2[1][0])
                    e_x = len([c for c in self.mapa[p1[1][0]][min_x + 1:max_x] if c == 'e'])
                    e_y = len([c for c in [self.mapa[j][p1[1][1]] for j in range(min_y + 1, max_y)] if c == 'e'])
                    paths_dict[(min(p1[0], p2[0]), max(p1[0], p2[0]))] = \
                        abs(p1[1][0] - p2[1][0]) + abs(p1[1][1] - p2[1][1]) + (e_x + e_y) * (expansion - 1)
        print(paths_dict)
        return paths_dict

    def __init__(self, mapa: list[str]):
        self.mapa = mapa
        # print(self)
        self.expand_mapa()
        self.galaxias = []
        self.get_galaxias()
        print(self.galaxias)
        # print(self)

    def __repr__(self) -> str:
        return "\n".join([s for s in self.mapa])


def proc_data(data: Collection) -> 'Collection':
    """
    Funcion para procesar archivo de input
    """
    return data.filter_blanks()


def part1(use_test_data: bool) -> None:
    """
    Primera parte
    """
    data = get_data(test=use_test_data).process(proc_data)
    galaxy = Galaxy(data.all())
    print(galaxy)
    print(sum([d for p,d in galaxy.path_lengths(1000000).items()]))


def part2(use_test_data: bool) -> None:
    """
    Segunda parte
    """
    data = get_data(test=use_test_data).process(proc_data)
    print(data)


if __name__ == "__main__":
    is_test = True
    print('================================================')
    part1(is_test)
    print('================================================')
    # part2(is_test)
