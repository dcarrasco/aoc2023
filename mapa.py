from typing import Any, Iterator


class Mapa:
    mapa: list

    def ancho(self) -> int:
        return len(self.mapa[0])

    def alto(self) -> int:
        return len(self.mapa)

    def get_linea(self, nlin: int) -> str:
        return self.mapa[nlin]

    def get_columna(self, ncol: int) -> str:
        col = ""
        col += "".join([linea[ncol] for linea in self.mapa])
        return col

    def transpose(self) -> "Mapa":
        return Mapa(["".join(list(r)) for r in zip(*self.mapa)])

    def turn_90(self) -> "Mapa":
        new_mapa = []
        ancho = self.ancho()
        for j in range(ancho):
            new_mapa.append(self.get_columna(ancho - j - 1))
        return Mapa(new_mapa)

    def stringify(self) -> str:
        return "".join([lin for lin in self.mapa])

    def __init__(self, mapa: list) -> None:
        self.mapa = mapa

    def __repr__(self) -> str:
        return "Mapa\n" + "\n".join(self.mapa) + "\n"

    def __iter__(self) -> Iterator[Any]:
        return iter(self.mapa)
