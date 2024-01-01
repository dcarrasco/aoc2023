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

    def transpose(self) -> list:
        return Mapa([list(r) for r in zip(*self.mapa)])

    def __init__(self, mapa: list) -> None:
        self.mapa = mapa

    def __repr__(self) -> str:
        return "Mapa\n" + "\n".join(self.mapa) + "\n"
