"""
AOC Advent of code 2023
Day 12
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
    tmp_mapa = []
    mapas = []
    for linea in data:
        if linea == '':
            if len(tmp_mapa) > 0:
                mapas.append(Mapa(tmp_mapa))
            tmp_mapa = []
        else:
            tmp_mapa.append(linea)
    return Collection(mapas)


def find_split(mapa: Mapa) -> int:
    for i in range(mapa.alto() - 1):
        if reflects(mapa, i):
            return i + 1
    return 0


def reflects(mapa: Mapa, ini: int) -> bool:
    lower: int = ini
    upper: int = ini + 1
    fixed_one = False

    while lower >= 0 and upper < mapa.alto():
        if mapa.get_linea(lower) != mapa.get_linea(upper):
            if fixed_one:
                return False
            elif is_fixable(mapa.get_linea(lower), mapa.get_linea(upper)):
                fixed_one = True
            else:
                return False
        lower -= 1
        upper += 1

    return fixed_one


def is_fixable(lower: str, upper: str) -> bool:
    diffs = 0
    for a, b in zip(lower, upper):
        if a != b:
            diffs += 1
    return diffs == 1


def part1(filename: str) -> None:
    """
    Primera parte
    """
    data = get_data(filename=filename).process(proc_data)
    print(data)
    suma = 0
    for m in data:
        suma += 100 * find_split(m) + find_split(m.transpose())
    print(f"suma: {suma}")


def part2(use_test_data: bool) -> None:
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
