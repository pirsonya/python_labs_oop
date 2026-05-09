from datetime import datetime
from validate import (
    validate_name, 
    validate_year, 
    validate_country, 
    validate_genre, 
    validate_count_books
)
class Author:
    _genre_categories = ["роман", "поэзия", "ужасы", "комедия", "детектив", "драма"]
    def __init__(self, name: str, surname: str, birth_year: int, death_year: int, country: str, genre: str, count_books=0) -> None:
        self._name=""
        self._surname=""
        self._birth_year=None
        self._death_year=None
        self._country=""
        self._genre=""
        self._count_books=0
        self._is_active=True

        validate_name(name, "name")
        validate_name(surname, "surname")
        validate_year(birth_year, "birth_year", min_year=1000, max_year=2026)
        validate_year(death_year, "death_year", min_year=birth_year, allow_none=True)
        validate_country(country)
        validate_genre(genre)
        validate_count_books(count_books)

        self._name: str = name
        self._surname: str = surname
        self._birth_year: int = birth_year
        self._death_year: int = death_year
        self._country: str = country
        self._genre: str = genre
        self._count_books: int = count_books

    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def surname(self) -> str:
        return self._surname
    
    @property
    def birth_year(self) -> int:
        return self._birth_year
    
    @property
    def death_year(self) -> int:
        return self._death_year
    
    @property
    def country(self) -> str:
        return self._country
    
    @property
    def genre(self) -> str:
        return self._genre
    
    @property
    def count_books(self) -> int:
        return self._count_books
    
    @property
    def is_active(self) -> bool:
        return self._is_active
    
    @count_books.setter
    def count_books(self, new_count) -> int:
        validate_count_books(new_count)
        self._count_books = new_count
    
    @country.setter
    def country(self, new_country) -> str:
        validate_country(new_country)
        self._country = new_country
    
    @genre.setter
    def genre(self, new_genre) -> str:
        validate_genre(new_genre)
        old_genre = self._genre
        self._genre = new_genre
        print(f"жанр  изменён с '{old_genre}' на '{self._genre}'")

    def activate(self):
        self._is_active = True
        return self._is_active
    
    def deactivate(self):
        self._is_active = False
        return self._is_active

    def get_full_name(self) -> str:
        return f'{self._name} {self._surname}'
    def get_initials(self) -> str:
        return f'{self._surname} {self._name[0]}'
    def is_alive(self):
        return self._death_year is None
    def get_age_in_year(self, year) -> int:
        if year<self._birth_year:
            return 0
        elif self._death_year and year>self._birth_year:
            return self._death_year-self._birth_year
        else:
            return year-self._birth_year
    def get_current_age(self, current=2026) -> int:
        if self.is_alive:
            return current-self._birth_year
        else:
            return 0
    def get_life_period(self) -> int:
        if self._death_year:
            return f'{self._birth_year}-{self._death_year}'
        else:
            return f'{self._birth_year}-настоящее время'
    def add_book(self, count=1):
        if not self._is_active:
            raise RuntimeError("автор неактивен")
        if count <= 0:
            raise ValueError("кол-во должно быть > 0")
        self._count_books += count
        return self._count_books
    def update_count_books(self, new_count):
        if not self._is_active:
            raise RuntimeError("автор неактивен")
        validate_count_books(new_count)
        self._count_books = new_count
        return True
    def get_info(self):
        life_status = "жив" if self.is_alive() else f"умер в {self._death_year}"
        activity_status = "активен" if self._is_active else "неактивен"
        return (f"{self.get_full_name()} ({self._birth_year}-{self._death_year if self._death_year else 'настоящее время'}), "
                f"{self._country}. жанр книг автора: {self._genre}. "
                f"написал книг: {self._count_books}. статус: {life_status}. "
                f"активность: {activity_status}")
    
    @classmethod
    def get_available_genres(cls):
        return cls._genre_categories
    
    @classmethod
    def add_genre(cls, new_genre):
        if new_genre.lower() not in cls._genre_categories:
            cls._genre_categories.append(new_genre.lower())
        return cls._genre_categories
    
    def display(self) -> str:
        return f"Author: {self.get_full_name()}, books: {self.count_books}"
    
    def score(self) -> float:
        return min(self.count_books / 10, 10.0)

    def __str__(self):
        life_status = f"({self._birth_year}"
        life_status += f"-{self._death_year}" if self._death_year else "-настоящее ыремя"
        life_status += ")"
        return (f"{self.get_full_name()} {life_status}, {self.country}\n"
                f"жанр: {self._genre}\n"
                f"кол-во написанных книг: {self._count_books}")
    
    def __repr__(self):
        return (f"Author(name='{self._name}', surname='{self._surname}', "
                f"birth_year={self._birth_year}, death_year={self._death_year}, "
                f"country='{self._country}', genre='{self._genre}', "
                f"count_books={self._count_books})")
    
    def __eq__(self, other):
        if not isinstance(other, Author): 
            return False
        return (self.surname == other.surname and 
                self.name == other.name and 
                self.birth_year == other.birth_year)


