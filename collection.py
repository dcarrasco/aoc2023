from functools import reduce
from typing import List, Any, Callable, Iterator


class Collection:

    list: List[Any]

    def __init__(self, list: List[Any]):
        self.list = list

    def map(self, func: Callable[[Any], Any]) -> 'Collection':
        return Collection(list(map(func, self.list)))

    def filter(self, func: Callable[[Any], Any]) -> 'Collection':
        return Collection(list(filter(func, self.list)))

    def reduce(self, func) -> Any:
        return reduce(func, self.list)

    def sum(self) -> int:
        return int(self.reduce(lambda x, y: y + x))

    def mult(self) -> int:
        return int(self.reduce(lambda x, y: y * x))

    def max(self) -> Any:
        return max(self.list)

    def min(self) -> Any:
        return min(self.list)

    def count(self) -> int:
        return len(self.list)

    def is_empty(self) -> bool:
        return len(self.list) == 0

    def first(self) -> Any:
        return self.list[0]

    def sort(self) -> 'Collection':
        return Collection(sorted(self.list))

    def flatten(self) -> 'Collection':
        new_list = []
        for x in self.list:
            for y in x:
                new_list.append(y)
        return Collection(new_list)

    def unique(self) -> 'Collection':
        new_list = []
        for x in self.list:
            if x not in new_list:
                new_list.append(x)
        return Collection(new_list)

    def contains(self, item: Any) -> bool:
        return item in self.list

    def get_list(self) -> List[Any]:
        return self.list

    def append(self, item) -> 'Collection':
        return Collection(self.list.append(item))

    def filter_blanks(self) -> 'Collection':
        return self.filter(lambda x: x != "")

    def all(self) -> List[Any]:
        return self.list

    def enumerate(self):
        return enumerate(self.list)

    def process(self, function: Callable):
        return function(self)

    def dump(self):
        print([str(elem) for elem in self.list])
        return self

    def __str__(self) -> str:
        return f"Collection{str(self.list)}"

    def __iter__(self) -> Iterator[Any]:
        return iter(self.list)

    def __getitem__(self, item: int) -> Any:
        return self.list[item]
