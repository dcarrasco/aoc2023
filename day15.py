"""
AOC Advent of code 2023
Day 15
"""

# from dataclasses import dataclass
from sys import argv
from aoc import get_data
from collection import Collection
# from mapa import Mapa


def proc_data(data: Collection) -> Collection:
    """
    Funcion para procesar archivo de input
    """
    return data.filter_blanks()


def hash(text: str) -> int:
    hash_number = 0
    for c in text:
        hash_number += ord(c)
        hash_number *= 17
        hash_number %= 256

    return hash_number


def part1(filename: str) -> None:
    """
    Primera parte
    """
    data = get_data(filename=filename).process(proc_data)
    data = Collection(data[0].split(","))
    print(data.map(lambda lin: hash(lin)).sum())


def print_boxes(boxes: list) -> None:
    for i, box in enumerate(boxes):
        if len(box) > 0:
            print(f"{i}) {box}")
    print()

def part2(filename: str) -> None:
    """
    Segunda parte
    """
    data = get_data(filename=filename).process(proc_data)
    data = Collection(data[0].split(","))
    print(data)

    boxes = [[] for _ in range(256)]
    for step in data:
        if "=" in step:
            label, number = step.split("=")
            # print(step, hash(label), label, number)
            found = False
            for i, lens in enumerate(boxes[hash(label)]):
                if lens[0] == label:
                    boxes[hash(label)][i] = (label, int(number))
                    found = True
            if not found:
                boxes[hash(label)].append((label, int(number)))

        if "-" in step:
            label, number = step.split("-")
            # print(step, hash(label), label, number)
            new_lenses = []
            for lens in boxes[hash(label)]:
                if lens[0] != label:
                    new_lenses.append(lens)
            boxes[hash(label)] = new_lenses
    print_boxes(boxes)

    power = 0
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            power += (i + 1) * (j + 1) * lens[1]
    print(f"Power: {power}")


if __name__ == "__main__":
    print('================================================')
    part1(argv[1])
    print('================================================')
    part2(argv[1])
