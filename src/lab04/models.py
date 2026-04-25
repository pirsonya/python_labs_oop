from lab03.base import Author
from lab03.models import Translator, Biographer
from lab04.interfaces import Printable, Comparable

class PrintableAuthor(Author, Printable):
    def to_string(self) -> str:
        return f"Author: {self.get_full_name()}, books: {self.count_books}"

class PrintableTranslator(Translator, Printable):
    def to_string(self) -> str:
        return (f"Translator: {self.get_full_name()}, "
                f"translations: {self._translated_books}, "
                f"lang pair: {self.get_language_pair()}")

class PrintableBiographer(Biographer, Printable):
    def to_string(self) -> str:
        return (f"Biographer: {self.get_full_name()}, "
                f"subjects: {self._subjects}, "
                f"interviews: {self._has_interviews}")

class ComparableAuthor(PrintableAuthor, Comparable):
    def compare_to(self, other) -> int:
        if not isinstance(other, Author):
            raise TypeError("Can only compare with Author")
        if self.birth_year < other.birth_year:
            return -1
        elif self.birth_year > other.birth_year:
            return 1
        return 0

class ComparableTranslator(PrintableTranslator, Comparable):
    def compare_to(self, other) -> int:
        if not isinstance(other, Author):
            raise TypeError("Can only compare with Author")
        if isinstance(other, Translator):
            if self._translated_books < other._translated_books:
                return -1
            elif self._translated_books > other._translated_books:
                return 1
        if self.birth_year < other.birth_year:
            return -1
        elif self.birth_year > other.birth_year:
            return 1
        return 0

class ComparableBiographer(PrintableBiographer, Comparable):
    def compare_to(self, other) -> int:
        if not isinstance(other, Author):
            raise TypeError("Can only compare with Author")
        if isinstance(other, Biographer):
            if self._biographies_count < other._biographies_count:
                return -1
            elif self._biographies_count > other._biographies_count:
                return 1
        if self.birth_year < other.birth_year:
            return -1
        elif self.birth_year > other.birth_year:
            return 1
        return 0