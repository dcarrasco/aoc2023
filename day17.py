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
    rows: int
    cols: int

    def __init__(self, mapa: list) -> None:
        super().__init__(mapa)
        self.cols = self.ancho()
        self.rows = self.alto()

    def dijkstra(self, init: Pos, target: Pos) -> int:
        INF = 1000000000

        heat_loss = Mapa([[INF for i in range(self.cols)] for j in range(self.rows)])
        heat_path = Mapa([[[] for i in range(self.cols)] for j in range(self.rows)])

        queue = set()
        for j in range(self.rows):
            for i in range(self.cols):
                queue.add((i, j))
        # print(queue)

        heat_loss.set_value(init, int(self.get_value(init)))
        heat_path.set_value(init, [init])

        while queue:
            position = self.get_min_heat_loss(queue, heat_loss, INF)
            print(position, len(queue))
            queue.remove(position)
            print(self.get_neighbors(position, queue))
            for neighbor, direction in self.get_neighbors(position, queue):
                # print(neighbor, direction)
                loss = heat_loss.get_value(self.add_position(neighbor, (-direction[0], -direction[1]))) + int(self.get_value(neighbor))
                print(neighbor, direction, loss, heat_loss.get_value(neighbor))
                if loss < heat_loss.get_value(neighbor):
                    heat_loss.set_value(neighbor, loss)
                    heat_path.set_value(neighbor, heat_path.get_value(position) + [neighbor])
                    # print(heat_path)

        # print(heat_loss, heat_path, queue)
        print(heat_path.get_value(target))
        self.print_path(heat_path.get_value(target))
        return heat_loss.get_value(target)

    def get_min_heat_loss(self, queue: set[Pos], heat_loss: Mapa, INF: int) -> Pos:
        minium = INF
        min_position = (-1, -1)
        for position in queue:
            if int(heat_loss.get_value(position)) < minium:
                minium = int(heat_loss.get_value(position))
                min_position = position

        return min_position

    def get_neighbors(self, position: Pos, queue: set[Pos]) -> list[tuple[Pos, Dir]]:
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        neighbors = []
        for d in dirs:
            new_pos = position
            for _ in range(3):
                new_pos = self.add_position(new_pos, d)
                if self.en_mapa(new_pos) and new_pos in queue:
                    neighbors.append((new_pos, d))

        return neighbors

    def optim2(self, init: Pos, target: Pos) -> int:
        pq: list[State] = [(0, init, EAST), (0, init, SOUTH)]
        visited = set()

        while pq:
            heat_loss, position, direction = heappop(pq)

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
    print(data.dijkstra((0, 0), (data.cols - 1, data.rows - 1)))


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
