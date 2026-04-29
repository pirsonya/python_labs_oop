from lab02.collection import AuthorCollection
from lab01.model import Author

class FunctionalAuthorCollection(AuthorCollection):
    def sort_by(self, key_func, reverse=False):
        self._items.sort(key=key_func, reverse=reverse)
        return self

    def filter_by(self, predicate):
        new_collection = FunctionalAuthorCollection()
        new_collection._items = [item for item in self._items if predicate(item)]
        return new_collection

    def apply(self, func):
        for i in range(len(self._items)):
            self._items[i] = func(self._items[i])
        return self

    def map(self, func):
        return list(map(func, self._items))

    def filter(self, predicate):
        return self.filter_by(predicate)

    def get_items(self):
        return self._items