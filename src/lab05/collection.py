"""
Расширенная коллекция AuthorCollection с методами функциональной обработки.
"""

from lab02.collection import AuthorCollection
from lab01.model import Author


class FunctionalAuthorCollection(AuthorCollection):
    """
    Расширение AuthorCollection с функциональными методами:
    - sort_by(key_func)
    - filter_by(predicate)
    - apply(func)
    """

    def sort_by(self, key_func, reverse=False):
        """
        Сортировка коллекции по переданной функции-ключу.
        
        Args:
            key_func: функция, возвращающая ключ для сортировки
            reverse: обратный порядок сортировки
        """
        self._items.sort(key=key_func, reverse=reverse)
        return self

    def filter_by(self, predicate):
        """
        Фильтрация коллекции по предикату.
        
        Args:
            predicate: функция, возвращающая True/False для элемента
        
        Returns:
            FunctionalAuthorCollection: новая коллекция с отфильтрованными элементами
        """
        new_collection = FunctionalAuthorCollection()
        new_collection._items = [item for item in self._items if predicate(item)]
        return new_collection

    def apply(self, func):
        """
        Применить функцию ко всем элементам коллекции (модифицирует элементы).
        
        Args:
            func: функция для применения к каждому элементу
        """
        for i in range(len(self._items)):
            self._items[i] = func(self._items[i])
        return self

    def map(self, func):
        """
        Преобразовать коллекцию, применив функцию к каждому элементу.
        
        Args:
            func: функция преобразования элемента
        
        Returns:
            list: список результатов преобразования
        """
        return list(map(func, self._items))

    def filter(self, predicate):
        """
        Алиас для filter_by (возвращает новую коллекцию).
        
        Args:
            predicate: функция-фильтр
        """
        return self.filter_by(predicate)

    def get_items(self):
        """Вернуть внутренний список элементов."""
        return self._items