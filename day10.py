"""
AOC Advent of code 2023
Day 10
"""

from dataclasses import dataclass
from aoc import get_data
from collection import Collection

Pos = tuple[int, int]


def proc_data(data: Collection) -> 'Collection':
    """
    Funcion para procesar archivo de input
    """
    return data.filter_blanks()


@dataclass
class Mapa:
    mapa: list[str]
    dist: list[list[int]]

    def __init__(self, mapa: 'Collection'):
        self.mapa = mapa.all()
        self.dist = []
        for _ in range(len(self.mapa)):
            tmp_dist = []
            for _ in range(len(self.mapa[0])):
                tmp_dist.append(0)
            self.dist.append(tmp_dist)

    def find_init(self) -> Pos:
        pos = (-1, -1)
        for j, lin in enumerate(self.mapa):
            for i, c in enumerate(lin):
                if c == "S":
                    pos = (j, i)
        return pos

    def get_sign(self, pos: Pos) -> str:
        return self.mapa[pos[0]][pos[1]]

    def set_distance(self, pos: Pos, distance: int) -> None:
        self.dist[pos[0]][pos[1]] = distance

    def get_distance(self, pos: Pos) -> int:
        return self.dist[pos[0]][pos[1]]

    def neighbors(self, pos: Pos) -> list[Pos]:
        j, i = pos
        connected = self.pos_connected_to(pos)
        neigh = {"n": (-1, -1), "e": (-1, -1), "s": (-1, -1), "w": (-1, -1)}
        if j > 0 and "n" in connected:
            neigh["n"] = (j - 1, i)
        if i < len(self.mapa[0]) and "e" in connected:
            neigh["e"] = (j, i + 1)
        if j < len(self.mapa) - 1 and "s" in connected:
            neigh["s"] = (j + 1, i)
        if i > 0 and "w" in connected:
            neigh["w"] = (j, i - 1)
        # print(neigh)

        if self.mapa[j][i] == "S":
            # print(neigh)
            for direction, position in list(neigh.items()):
                # print(direction, position)
                if position != (-1, -1):
                    sign = self.get_sign(position)
                    # print(direction, position, sign)
                    if direction == "n":
                        neigh[direction] = position if sign in "|F7" else (-1, -1)
                    if direction == "e":
                        neigh[direction] = position if sign in "-J7" else (-1, -1)
                    if direction == "s":
                        neigh[direction] = position if sign in "|JL" else (-1, -1)
                    if direction == "w":
                        neigh[direction] = position if sign in "-LF" else (-1, -1)

        # print([p for d, p in neigh.items() if p != (-1, -1)])
        return [p for d, p in neigh.items() if p != (-1, -1)]

    def pos_connected_to(self, pos: Pos) -> str:
        j, i = pos
        sign = self.mapa[j][i]
        return self.sign_connections(sign)

    def sign_connections(self, sign: str) -> str:
        conn_dict = {
            "|": "ns", "-": "ew", "L": "ne", "J": "nw", "7": "sw", "F": "se", ".": "", "S": "nsew"
        }
        return conn_dict[sign]

    def max_dist(self) -> int:
        maximo = 0
        for d in self.dist:
            for i in d:
                if i > maximo:
                    maximo = i
        return maximo

    def walk(self) -> None:
        init = self.find_init()
        # print(f"init: {init}")
        self.set_distance(init, 0)

        for init_neigh in self.neighbors(init):
            pos = init_neigh
            last_pos = init
            distance = 0
            while not self.get_sign(pos) == "S":
                distance += 1
                if self.get_distance(pos) == 0:
                    self.set_distance(pos, distance)
                else:
                    if self.get_distance(pos) > distance:
                        self.set_distance(pos, distance)
                n = self.neighbors(pos)
                # print(f" > pos {pos} / sign {self.get_sign(pos)} / neigh {n}")
                next_pos = [next for next in n if next != last_pos][0]
                last_pos, pos = pos, next_pos

    def __repr__(self) -> str:
        rep = "Mapa\n"
        for m in self.mapa:
            rep += " ".join(list(m)) + "\n"
        rep += "\nDist\n"
        for d in self.dist:
            rep += " ".join([f"{i:02d}" for i in d]) + "\n"
        return rep


def part1(use_test_data: bool) -> None:
    """
    Primera parte
    """
    data = get_data(test=use_test_data).process(proc_data)
    mapa = Mapa(data)
    mapa.walk()
    print(mapa)
    print(mapa.max_dist())


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
