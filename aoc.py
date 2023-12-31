"""
AOC 2022
Utils file
"""

import __main__
from collection import Collection


def get_data(test: bool = False, filename: str = "") -> 'Collection':
    """
    Recupera los datos para ejecutar el programa
    """

    def get_filename():
        file, ext = __main__.__file__.split(".")
        testfile = "-test" if test else ""
        return f"{file}{testfile}.txt"

    filename = get_filename() if filename == "" else filename
    with open(filename, mode="r", encoding="utf-8") as file:
        return Collection(file.read().split("\n"))
