import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab03.base import Author
class Translator(Author):
    def __init__(self, name, surname, birth_year=None, death_year=None,
                 country="", genre="", count_books=0,
                 languages_from="", languages_to="", translated_books=0):

        super().__init__(name, surname, birth_year, death_year,
                         country, genre, count_books)
        self._languages_from = languages_from
        self._languages_to = languages_to
        self._translated_books = translated_books      

    def add_translation(self, count=1):
        if not self._is_active:
            raise RuntimeError("переводчик неактивен")
        if count <= 0:
            raise ValueError("количество должно быть > 0")
        self._translated_books += count
        return self._translated_books

    def get_language_pair(self):
        return f"{self._languages_from} -> {self._languages_to}"

    def translation_efficiency(self):
        if self._count_books == 0:
            return self._translated_books
        return self._translated_books / self._count_books

    def get_info(self):
        parent_info = super().get_info() 
        return (f"{parent_info}\n"
                f"[Переводчик] Переводит с: {self._languages_from}, "
                f"на: {self._languages_to}, переведено книг: {self._translated_books}")

    def __str__(self):
        base_str = super().__str__()
        return (f"{base_str}\n"
                f"переводчик: {self.get_language_pair()}, "
                f"переведено книг: {self._translated_books}")

    def calculate(self):
        return self._translated_books


class Biographer(Author):
    def __init__(self, name, surname, birth_year=None, death_year=None,
                 country="", genre="биография", count_books=0,
                 subjects="", biographies_count=0, has_interviews=False):

        super().__init__(name, surname, birth_year, death_year,
                         country, genre, count_books)
        self._subjects = subjects                      
        self._biographies_count = biographies_count    
        self._has_interviews = has_interviews          

    def add_biography(self):
        return self.add_book()

    def get_main_subject(self):
        if self._subjects:
            return self._subjects.split(",")[0].strip()
        return "неизвестно"

    def is_research_based(self):
        return "использует интервью" if self._has_interviews else "только открытые источники"

    def get_info(self):
        parent_info = super().get_info()
        return (f"{parent_info}\n"
                f"[Биограф] Пишет о: {self._subjects}, "
                f"биографий: {self._biographies_count}, "
                f"интервью: {'да' if self._has_interviews else 'нет'}")

    def __str__(self):
        base_str = super().__str__()
        return (f"{base_str}\n"
                f"биограф: объект исследования — {self.get_main_subject()}, "
                f"{self.is_research_based()}")

    def calculate(self):
        multiplier = 1.5 if self._has_interviews else 1.0
        return self._biographies_count * multiplier