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
    return data.filter_blanks()


def move_north(mapa: Mapa) -> Mapa:
    new_map = []
    for lin in mapa.transpose():
        new_lin = lin
        for i, rock in enumerate(lin):
            if i > 0:
                j = i
                while new_lin[j] == "O" and j > 0 and new_lin[j - 1] == ".":
                    # print(i, j, new_lin[j], new_lin[j - 1])
                    new_lin = new_lin[0:j - 1] + "O." + new_lin[j + 1:]
                    j -= 1
        new_map.append(new_lin)
    return Mapa(new_map).transpose()


def total_load(mapa: Mapa) -> int:
    suma = 0
    for i, linea in enumerate(mapa):
        rocks = len([c for c in linea if c == "O"])
        suma += (mapa.alto() - i) * rocks

    return suma


def part1(filename: str) -> None:
    """
    Primera parte
    """
    data = get_data(filename=filename).process(proc_data)
    mapa = Mapa(data.all())
    mapa = move_north(mapa)
    print(mapa)
    print(f"suma: {total_load(mapa)}")


def ciclo(mapa: Mapa) -> Mapa:
    mapa = move_north(mapa)

    mapa = mapa.turn_90().turn_90().turn_90()
    mapa = move_north(mapa)
    mapa = mapa.turn_90()

    mapa = mapa.turn_90().turn_90()
    mapa = move_north(mapa)
    mapa = mapa.turn_90().turn_90()

    mapa = mapa.turn_90()
    mapa = move_north(mapa)
    mapa = mapa.turn_90().turn_90().turn_90()

    return mapa


def find_ciclo(mapa: Mapa):
    mapas = dict()
    i = 1
    while i <= 1000:
        mapa = ciclo(mapa)
        hash = mapa.stringify()
        if hash in mapas:
            print("FOUND!!!!!!")
            return (mapa, i, i - mapas[hash])
        else:
            mapas[hash] = i
            i += 1


def finish_cicles(mapa: Mapa, n_ciclo: int, largo_ciclo: int):
    print(mapa, n_ciclo, largo_ciclo)
    ciclos_restantes = 1000000000 - n_ciclo
    full_ciclos_restantes = ciclos_restantes // largo_ciclo
    ciclos_restantes -= full_ciclos_restantes * largo_ciclo
    print(ciclos_restantes)
    for i in range(ciclos_restantes):
        mapa = ciclo(mapa)
    return mapa


def part2(filename: str) -> None:
    """
    Segunda parte
    """
    data = get_data(filename=filename).process(proc_data)
    # print(data)
    mapa = Mapa(data.all())
    print(mapa)
    # print(find_ciclo(mapa))
    print(total_load(finish_cicles(*find_ciclo(mapa))))


if __name__ == "__main__":
    print('================================================')
    # part1(argv[1])
    print('================================================')
    part2(argv[1])
