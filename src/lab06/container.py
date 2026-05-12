from typing import TypeVar, Generic, Optional, Callable, List, Protocol, Union

class Displayable(Protocol):
    def display(self) -> str: ...


class Scorable(Protocol):
    def score(self) -> float: ...

T = TypeVar('T')           
R = TypeVar('R')           
D = TypeVar('D', bound=Displayable)   
S = TypeVar('S', bound=Scorable)      


class TypedCollection(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []

    def add(self, item: T) -> None:
        """добавить элемент в коллекцию"""
        self._items.append(item)

    def remove(self, item: T) -> None:
        """удалить элемент из коллекции"""
        self._items.remove(item)

    def remove_at(self, index: int) -> T:
        """удалить элемент по индексу"""
        if index < 0 or index >= len(self._items):
            raise IndexError("индекс вне диапазона")
        return self._items.pop(index)

    def get_all(self) -> List[T]:
        """получить копию списка элементов"""
        return self._items.copy()

    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        """найти первый элемент, удовлетворяющий условию"""
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        """найти все элементы, удовлетворяющие условию"""
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[T], R]) -> List[R]:
        """преобразовать элементы с помощью функции transform"""
        return [transform(item) for item in self._items]

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index: Union[int, slice]) -> Union[T, 'TypedCollection[T]']:
        if isinstance(index, slice):
            new_collection = TypedCollection[T]()
            new_collection._items = self._items[index]
            return new_collection
        return self._items[index]

    def __repr__(self) -> str:
        return f"TypedCollection({len(self._items)} items)"



class DisplayableCollection(TypedCollection[D]):
    """коллекция для объектов с методом display()"""
    pass


class ScorableCollection(TypedCollection[S]):
    """коллекция для объектов с методом score()"""
    pass
