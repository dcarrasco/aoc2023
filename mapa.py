from typing import Any, Iterator


class Mapa:
    mapa: list
    rows: int
    cols: int

    def ancho(self) -> int:
        return len(self.mapa[0])

    def alto(self) -> int:
        return len(self.mapa)

    def get_linea(self, nlin: int) -> str:
        return self.mapa[nlin]

    def set_value(self, pos: "Pos", value: Any) -> None:
        self.mapa[pos.y][pos.x] = value

    def get_value(self, pos: "Pos") -> str:
        if self.en_mapa(pos):
            return self.mapa[pos.y][pos.x]

        return ""

    def en_mapa(self, pos: "Pos") -> bool:
        return 0 <= pos.x < self.cols and 0 <= pos.y < self.rows

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

    def new(value: Any, cols: int, rows: int) -> "Mapa":
        return Mapa([[value for _ in range(cols)] for _ in range(rows)])

    def __init__(self, mapa: list) -> None:
        self.mapa = mapa
        self.cols = self.ancho()
        self.rows = self.alto()

    def __repr__(self) -> str:
        repr = "Mapa\n"
        for linea in self.mapa:
            if type(linea) is str:
                repr += f"{linea}\n"
            elif type(linea) is list:
                repr += "".join([str(elem) + " " for elem in linea]) + "\n"
        return repr

    def __iter__(self) -> Iterator[Any]:
        return iter(self.mapa)


class Pos:
    x: int
    y: int

    def __add__(self, position: "Pos") -> "Pos":
        return Pos(self.x + position.x, self.y + position.y)

    def __gt__(self, position: "Pos") -> bool:
        return self.modulo() > position.modulo()

    def __lt__(self, position: "Pos") -> bool:
        return self.modulo() < position.modulo()

    def __eq__(self, position: "Pos") -> bool:
        return self.x == position.x and self.y == position.y

    def __hash__(self) -> str:
        return (self.x, self.y).__hash__()

    def rotate_left(self) -> "Pos":
        return Pos(-self.y, self.x)

    def rotate_right(self) -> "Pos":
        return Pos(self.y, -self.x)

    def modulo(self) -> float:
        return (self.x**2 + self.y**2)

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x},{self.y})"
