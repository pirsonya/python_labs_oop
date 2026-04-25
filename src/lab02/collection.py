from lab02.model import Author

class AuthorCollection:
    def __init__(self):
        self._items = []  

    def add(self, author):
        if not isinstance(author, Author):
            raise TypeError(f"Можно добавлять только Author или его наследников, получен {type(author).__name__}")

        for existing in self._items:
            if existing == author:
                raise ValueError(f"Автор {author.get_full_name()} ({author.birth_year}) уже существует")

        self._items.append(author)

    def remove(self, author):
        if author not in self._items:
            raise ValueError("Такого автора нет в коллекции")
        self._items.remove(author)

    def remove_at(self, index):
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона")
        return self._items.pop(index)

    def get_all(self):
        return self._items.copy()

    def find_by_full_name(self, name, surname):
        for author in self._items:
            if author.name.lower() == name.lower() and author.surname.lower() == surname.lower():
                return author
        return None

    def find_by_surname(self, surname):
        result = []
        for author in self._items:
            if author.surname.lower() == surname.lower():
                result.append(author)
        return result

    def find_by_genre(self, genre):
        result = []
        for author in self._items:
            if author.genre.lower() == genre.lower():
                result.append(author)
        return result

    def find_by_country(self, country):
        result = []
        for author in self._items:
            if author.country.lower() == country.lower():
                result.append(author)
        return result

    def find_active(self):
        result = []
        for author in self._items:
            if author.is_active:
                result.append(author)
        return result

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        if isinstance(index, slice):
            new_collection = AuthorCollection()
            new_collection._items = self._items[index]
            return new_collection
        if index < 0:
            index = len(self._items) + index
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона")
        return self._items[index]

    def sort(self, key=None, reverse=False):
        new_collection = AuthorCollection()
        if key is None:
            key = lambda a: a.get_full_name().lower()
        new_collection._items = sorted(self._items, key=key, reverse=reverse)
        return new_collection

    def sort_by_full_name(self, reverse=False):
        return self.sort(key=lambda a: a.get_full_name().lower(), reverse=reverse)

    def sort_by_birth_year(self, reverse=False):
        return self.sort(key=lambda a: a.birth_year if a.birth_year else 0, reverse=reverse)

    def sort_by_count_books(self, reverse=False):
        return self.sort(key=lambda a: a.count_books, reverse=reverse)

    def sort_by_country(self, reverse=False):
        return self.sort(key=lambda a: a.country.lower(), reverse=reverse)

    def get_alive(self):
        new_collection = AuthorCollection()
        for author in self._items:
            if author.is_alive():
                new_collection._items.append(author)
        return new_collection

    def get_by_genre(self, genre):
        new_collection = AuthorCollection()
        for author in self._items:
            if author.genre.lower() == genre.lower():
                new_collection._items.append(author)
        return new_collection

    def get_by_country(self, country):
        new_collection = AuthorCollection()
        for author in self._items:
            if author.country.lower() == country.lower():
                new_collection._items.append(author)
        return new_collection

    def get_active(self):
        new_collection = AuthorCollection()
        for author in self._items:
            if author.is_active:
                new_collection._items.append(author)
        return new_collection

    def get_prolific(self, min_books=10):
        new_collection = AuthorCollection()
        for author in self._items:
            if author.count_books >= min_books:
                new_collection._items.append(author)
        return new_collection

    def __repr__(self):
        names = [a.get_full_name() for a in self._items]
        return f"AuthorCollection({len(self._items)} authors: {names})"