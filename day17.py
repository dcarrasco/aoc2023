"""
AOC Advent of code 2023
Day 17
"""

# from dataclasses import dataclass
from sys import argv
from heapq import heappop, heappush
from aoc import get_data
from collection import Collection
from mapa import Mapa


def proc_data(data: Collection) -> Collection:
    """
    Funcion para procesar archivo de input
    """
    return data.filter_blanks()


Pos = tuple[int, int]
Dir = tuple[int, int]
State = tuple[int, Pos, Dir]
EAST: Dir = (1, 0)
SOUTH: Dir = (0, -1)


class LavaMap(Mapa):
    def optim2(self, init: Pos, target: Pos) -> int:
        pq: list[State] = [(0, init, EAST), (0, init, SOUTH)]
        visited = set()

        while pq:
            heat_loss, position, direction = heappop(pq)
            print(position)

            if (position, direction) in visited:
                continue

            visited.add((position, direction))
            if position == target:
                # print(pq)
                return heat_loss

            for state in self.get_reachable_states(position, direction, heat_loss):
                heappush(pq, state)

        return -1

    def get_reachable_states(self, position: Pos, direction: Dir, heat_loss: int) -> list[State]:
        states = []
        states.extend(self.get_line_of_states(position, self.rotate_left(direction), heat_loss))
        states.extend(self.get_line_of_states(position, self.rotate_right(direction), heat_loss))

        return states

    def get_line_of_states(self, position: Pos, direction: Dir, heat_loss: int) -> list[State]:
        neighbors: list[State] = []
        for i, pos in enumerate(self.get_line_of_positions(position, direction)):
            heat_loss += int(self.get_value(pos))
            if i >= 4:
                neighbors.append((heat_loss, pos, direction))

        return neighbors

    def get_line_of_positions(self, position: Pos, direction: Dir) -> list[Pos]:
        adjacents = []
        for _ in range(10):
            position = self.add_position(position, direction)
            if self.en_mapa(position):
                adjacents.append(position)

        return adjacents

    def add_position(self, pos1: Pos, pos2: Pos) -> Pos:
        return (pos1[0] + pos2[0], pos1[1] + pos2[1])

    def rotate_left(self, direction: Dir) -> Dir:
        return (-direction[1], direction[0])

    def rotate_right(self, direction: Dir) -> Dir:
        return (direction[1], -direction[0])

    def en_mapa(self, position: Pos) -> bool:
        return 0 <= position[0] < self.ancho() and 0 <= position[1] < self.alto()

    def print_path(self, path: list) -> None:
        repr = ""
        for j in range(self.alto()):
            for i in range(self.ancho()):
                if (i, j) in path:
                    repr += "(" + self.get_value((i, j)) + ") "
                else:
                    repr += " " + self.get_value((i, j)) + "  "
            repr += "\n"
        print(repr)


def part1(filename: str) -> None:
    """
    Primera parte
    """
    data = get_data(filename=filename).process(proc_data)
    data = LavaMap(data.all())
    print(data)
    # print(data.optim((data.ancho() - 1, data.alto() - 1)))
    print(data.optim2((0, 0), (data.ancho() - 1, data.alto() - 1)))


def part2(filename: str) -> None:
    """
    Segunda parte
    """
    data = get_data(filename=filename).process(proc_data)


if __name__ == "__main__":
    print('================================================')
    part1(argv[1])
    print('================================================')
    # part2(argv[1])
