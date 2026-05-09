# ЛР-6 — Generics и typing

---

## Цель работы

* Освоить систему аннотаций типов в Python (`typing`).
* Научиться создавать **обобщённые (generic) классы** с помощью `TypeVar` и `Generic`.
* Понять концепцию **структурной типизации** через `typing.Protocol`.


## 2. Описание реализованных типов и контейнеров

### Generic-класс `TypedCollection[T]`

Обобщённая версия коллекции из ЛР-2. Позволяет хранить элементы одного типа `T`

```python
class TypedCollection(Generic[T]):
    def __init__(self) -> None: ...
    def add(self, item: T) -> None: ...
    def remove(self, item: T) -> None: ...
    def get_all(self) -> List[T]: ...
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]: ...
    def filter(self, predicate: Callable[[T], bool]) -> List[T]: ...
    def map(self, transform: Callable[[T], R]) -> List[R]: ...

Базовый TypeVar — подходит для любого типа
T = TypeVar('T')

TypeVar для map() — тип результата может быть другим
R = TypeVar('R')

TypeVar с ограничением — только объекты у которых есть метод display()
D = TypeVar('D', bound=Displayable)

TypeVar с ограничением — только объекты у которых есть метод score()
S = TypeVar('S', bound=Scorable) 
```

### Описание протоколов 

```python
class Displayable(Protocol):
    """
    Протокол для объектов, которые можно отобразить.
    Любой класс у которого есть метод display() подходит.
    """
    def display(self) -> str:
        """Вернуть строковое представление объекта"""
        ...

class Scorable(Protocol):
    """
    Протокол для объектов, которые можно оценить.
    Любой класс у которого есть метод score() подходит.
    """
    def score(self) -> float:
        """Вернуть числовую оценку объекта"""
        ...
```

### Какие классы подходят протоколам

```python
#  Author имеет метод display() и score()
class Author:
    def display(self) -> str:
        return f"Author: {self.get_full_name()}, books: {self.count_books}"
    
    def score(self) -> float:
        return min(self.count_books / 10, 10.0)

# Translator имеет метод display()
class Translator(Author):
    def display(self) -> str:
        return f"Translator: {self.get_full_name()}, translated: {self._translated_books}"

# Biographer имеет метод display()
class Biographer(Author):
    def display(self) -> str:
        return f"Biographer: {self.get_full_name()}, subjects: {self._subjects}"
''' 
Все три класса подходят под Displayable (есть метод display())
Author подходит под Scorable (есть метод score())
Translator и Biographer НЕ подходят под Scorable (нет метода score())
'''
```

## 3. Демонстрация работы

### Сценарий 1 - Базовые операции TypedCollection
**Что происходит:**
- Создаётся коллекция `TypedCollection[Author]` — коллекция может хранить только объекты типа Author или его наследников
- В коллекцию добавляются объекты: обычный автор (Author) и переводчик (Translator)
- Выводится количество элементов в коллекции
- Все элементы коллекции выводятся по очереди
- Демонстрируется доступ к элементу по индексу
![alt text](<../../img/lab06/1 сценарий.png>)

### Сценарий 2 — find(), filter(), map()
**Метод find():**
- Ищет первый элемент, подходящий под условие
- В первом случае условие находит автора "Лев Толстой" — возвращается объект автора
- Во втором случае условие ищет несуществующего автора "Иван Петров" — возвращается None

**Метод filter():**
- Фильтрует авторов по стране "Россия" — возвращается список из 5 российских авторов
- Фильтрует авторов по количеству книг (>= 15) — возвращаются авторы с 20 и 50 книгами

**Метод map():**
- Преобразует коллекцию авторов в список имён (Author → str)
- Преобразует коллекцию авторов в список годов рождения (Author → int)
- Преобразует коллекцию авторов в список рейтингов (Author → float)

![alt text](<../../img/lab06/2 сценарий.png>)

### Сценарий 3 — Protocol и структурная типизация
**Protocol Displayable:**
- Создаётся коллекция `DisplayableCollection` — может хранить только объекты, у которых есть метод `display()`
- В эту коллекцию добавляются объекты разных типов: Author, Translator, Biographer
- У всех этих классов есть метод `display()`
- Для каждого объекта вызывается метод `display()` 

**Protocol Scorable:**
- Создаётся коллекция `ScorableCollection` — может хранить только объекты, у которых есть метод `score()`
- В эту коллекцию добавляются объекты, у которых есть метод `score()` 
- Объекты без метода `score()` (Translator, Biographer) нельзя добавить 
![alt text](<../../img/lab06/3 сценарий.png>)

