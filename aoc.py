"""
AOC 2022
Utils file
"""

from collection import Collection


def get_data(filename: str):
    """
    Recupera los datos para ejecutar el programa
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        return Collection(file.read().split("\n"))
