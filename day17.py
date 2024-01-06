"""
AOC Advent of code 2023
Day 17
"""

# from dataclasses import dataclass
from sys import argv
from heapq import heappop, heappush
from aoc import get_data
from collection import Collection
from mapa import Mapa, Pos


def proc_data(data: Collection) -> Collection:
    """
    Funcion para procesar archivo de input
    """
    return data.filter_blanks()


State = tuple[int, Pos, Pos]
Queue = dict[Pos, tuple[Pos, int]]
EAST: Pos = Pos(1, 0)
SOUTH: Pos = Pos(0, -1)
PrioQueue = list[int, Pos, Pos, int]


class LavaMap(Mapa):

    def dijkstra(self, start: Pos, target: Pos) -> int:
        INF = 1000000000
        heat_loss = Mapa.new(INF, self.cols, self.rows)
        heat_path = Mapa.new([], self.cols, self.rows)

        queue: Queue = {}
        for j in range(self.rows):
            for i in range(self.cols):
                queue[Pos(i, j)] = (Pos(0, 0), 0)

        heat_loss.set_value(start, int(self.get_value(start)))
        heat_path.set_value(start, [start])
        queue[start] = (Pos(1, 0), 1)

        ii = 0
        while queue and ii < INF:
            ii += 1
            position = self.get_min_heat_loss(queue, heat_loss)
            direction, count_straight = queue.pop(position)
            print("pos dir q:", position, direction, count_straight)
            for neighbor, d, s in self.get_neighbors(position, direction, count_straight, queue):
                queue[neighbor] = (d, s)
                loss = heat_loss.get_value(position) + int(self.get_value(neighbor))
                if loss < heat_loss.get_value(neighbor):
                    heat_loss.set_value(neighbor, loss)
                    heat_path.set_value(neighbor, heat_path.get_value(position) + [neighbor])

        self.print_path(heat_path.get_value(target))
        return heat_loss.get_value(target)

    def get_min_heat_loss(self, queue: Queue, heat_loss: Mapa) -> Pos:
        minium = 1000000000
        min_position = Pos(-1, -1)
        for position in queue:
            if int(heat_loss.get_value(position)) < minium:
                minium = int(heat_loss.get_value(position))
                min_position = position

        return min_position

    def get_neighbors(self, position: Pos, direction: Pos, straight: int, queue: Queue) -> list[tuple[Pos, Pos, int]]:
        # print("get neighbors for:", position, direction, straight)
        dirs = ((direction, straight + 1), (direction.rotate_left(), 0), (direction.rotate_right(), 0))

        neighbors = []
        for d, s in dirs:
            if self.en_mapa(position + d) and s < 4 and (position + d) in queue:
                neighbors.append((position + d, d, s))

        return neighbors

    def optim3(self, start: Pos, target: Pos) -> int:
        max_straight = 10
        min_turn = 4
        pq = [(0, start, Pos(0, 0), 0)]
        seen = set()

        while pq:
            loss, position, direction, step = heappop(pq)

            if position == target:
                break

            if not self.en_mapa(position):
                continue

            if (position, direction, step) in seen:
                continue

            seen.add((position, direction, step))

            if step < max_straight and direction != Pos(0, 0):
                next_position = position + direction
                if self.en_mapa(next_position):
                    heappush(pq, (loss + int(self.get_value(next_position)), next_position, direction, step + 1))

            if step >= min_turn or direction == Pos(0, 0):
                for turn_direction in (Pos(1, 0), Pos(-1, 0), Pos(0, 1), Pos(0, -1)):
                    if turn_direction != direction and turn_direction != Pos(-direction.x, -direction.y):
                        next_position = position + turn_direction
                        if self.en_mapa(next_position):
                            heappush(pq, (loss + int(self.get_value(next_position)), next_position, turn_direction, 1))

        return loss

    def en_mapa(self, position: Pos) -> bool:
        return 0 <= position.x < self.ancho() and 0 <= position.y < self.alto()

    def print_path(self, path: list[Pos]) -> None:
        repr = ""
        for j in range(self.alto()):
            for i in range(self.ancho()):
                if Pos(i, j) in path:
                    repr += "(" + self.get_value(Pos(i, j)) + ") "
                else:
                    repr += " " + self.get_value(Pos(i, j)) + "  "
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
    # print(data.optim2(Pos(0, 0), (data.ancho() - 1, data.alto() - 1)))
    # print(data.dijkstra(Pos(0, 0), Pos(data.cols - 1, data.rows - 1)))
    print(data.optim3(Pos(0, 0), Pos(data.cols - 1, data.rows - 1)))


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
