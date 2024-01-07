from functools import reduce
from typing import List, Any, Callable, Iterator


class Collection:

    lista: List[Any]

    def __init__(self, lista: List[Any]):
        self.lista = lista

    def map(self, func: Callable[[Any], Any]) -> 'Collection':
        return Collection(list(map(func, self.lista)))

    def filter(self, func: Callable[[Any], Any]) -> 'Collection':
        return Collection(list(filter(func, self.lista)))

    def reduce(self, func: Callable[[Any, Any], Any]) -> Any:
        return reduce(func, self.lista)

    def sum(self) -> int:
        return int(self.reduce(lambda x, y: y + x))

    def mult(self) -> int:
        return int(self.reduce(lambda x, y: y * x))

    def max(self) -> Any:
        return max(self.lista)

    def min(self) -> Any:
        return min(self.lista)

    def count(self) -> int:
        return len(self.lista)

    def is_empty(self) -> bool:
        return len(self.lista) == 0

    def first(self) -> Any:
        return self.lista[0]

    def sort(self) -> 'Collection':
        return Collection(sorted(self.lista))

    def flatten(self) -> 'Collection':
        new_list = []
        for x in self.lista:
            for y in x:
                new_list.append(y)
        return Collection(new_list)

    def unique(self) -> 'Collection':
        new_list = []
        for x in self.lista:
            if x not in new_list:
                new_list.append(x)
        return Collection(new_list)

    def contains(self, item: Any) -> bool:
        return item in self.lista

    def get_list(self) -> List[Any]:
        return self.lista

    def append(self, item: Any) -> 'Collection':
        self.lista.append(item)
        return Collection(self.lista)

    def filter_blanks(self) -> 'Collection':
        return self.filter(lambda x: x != "")

    def all(self) -> List[Any]:
        return self.lista

    def enumerate(self) -> 'enumerate[Any]':
        return enumerate(self.lista)

    def process(self, function: Callable[[Any], Any]) -> Any:
        return function(self)

    def dump(self) -> 'Collection':
        print([str(elem) for elem in self.lista])
        return self

    def __str__(self) -> str:
        return f"Collection{str(self.lista)}"

    def __iter__(self) -> Iterator[Any]:
        return iter(self.lista)

    def __getitem__(self, item: int) -> Any:
        return self.lista[item]
