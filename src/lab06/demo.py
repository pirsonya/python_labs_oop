import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from typing import List
from lab01.model import Author
from lab03.models import Translator, Biographer
from lab06.container import (
    TypedCollection, 
    DisplayableCollection, 
    ScorableCollection,
    Displayable,
    Scorable
)

from lab06.validate import (
    validate_name, 
    validate_year, 
    validate_country, 
    validate_genre, 
    validate_count_books
)


def create_demo_collection() -> TypedCollection[Author]:
    collection = TypedCollection[Author]()
    
    author1 = Author("Лев", "Толстой", 1828, 1910, "Россия", "роман", 20)
    author2 = Author("Фёдор", "Достоевский", 1821, 1881, "Россия", "роман", 15)
    author3 = Author("Джордж", "Оруэлл", 1903, 1950, "Великобритания", "антиутопия", 8)
    author4 = Author("Эрих", "Ремарк", 1898, 1970, "Германия", "роман", 12)
    author5 = Author("Харуки", "Мураками", 1949, None, "Япония", "магический реализм", 14)
    
    translator = Translator(
        "Нора", "Галь", 1912, 1991, "Россия", "художественный перевод", 50,
        languages_from="английский, французский", languages_to="русский",
        translated_books=70
    )
    
    biographer = Biographer(
        "Илья", "Толстой", 1950, None, "Россия", "биография", 5,
        subjects="Лев Толстой, русская литература",
        biographies_count=4,
        has_interviews=True
    )
    
    collection.add(author1)
    collection.add(author2)
    collection.add(author3)
    collection.add(author4)
    collection.add(author5)
    collection.add(translator)
    collection.add(biographer)
    
    return collection


# сценарий 1

def sc1():
    print("СЦЕНАРИЙ 1")
    print("-" * 60)

    collection: TypedCollection[Author] = TypedCollection()
    print("cоздана коллекция TypedCollection[Author]")
    
    author = Author("Лев", "Толстой", 1828, 1910, "Россия", "роман", 20)
    collection.add(author)
    print(f"добавлен: {author.get_full_name()}")
    
    translator = Translator(
        "Нора", "Галь", 1912, 1991, "Россия", "художественный перевод", 50,
        languages_from="английский", languages_to="русский", translated_books=70
    )
    collection.add(translator)
    print(f"lобавлен: {translator.get_full_name()}")
    
    print(f"\nВсего элементов: {len(collection)}")
    print("Элементы коллекции:")
    for item in collection.get_all():
        print(f"-{item.get_full_name()} ({item.__class__.__name__})")
    
    print("\nСценарий 1 завершён\n")

def sc2():
    print("СЦЕНАРИЙ 2")
    print("-" * 60)
    
    collection = create_demo_collection()
    print(f"Коллекция содержит {len(collection)} авторов")
    
    print("\n--- find() ---")
    
    found = collection.find(lambda a: a.get_full_name() == "Лев Толстой")
    if found:
        print(f"найден: {found.get_full_name()}, книг: {found.count_books}")
    
    not_found = collection.find(lambda a: a.get_full_name() == "Иван Петров")
    print(f"поиск несуществующего: {not_found} (None)")
    
    print("\n--- filter() ---")
    
    prolific_authors = collection.filter(lambda a: a.count_books >= 15)
    print(f"Авторы с >= 15 книгами ({len(prolific_authors)}):")
    for author in prolific_authors:
        print(f"-{author.get_full_name()}: {author.count_books} книг")
    
    russian_authors = collection.filter(lambda a: a.country == "Россия")
    print(f"\nАвторы из России ({len(russian_authors)}):")
    for author in russian_authors:
        print(f"-{author.get_full_name()} ({author.country})")
    
    print("\n--- map() ---")
    
    names: List[str] = collection.map(lambda a: a.get_full_name())
    print(f"map() -> list[str] (имена): {names[:5]}...")

    years: List[int] = collection.map(lambda a: a.birth_year)
    print(f"map() -> list[int] (годы рождения): {years}")

    ratings: List[float] = collection.map(lambda a: min(a.count_books / 10, 10.0))
    print(f"map() -> list[float] (рейтинг): {[round(r, 1) for r in ratings]}")

    descriptions: List[str] = collection.map(
        lambda a: f"{a.get_full_name()} ({a.count_books} книг)"
    )
    print(f"\nmap() -> list[str] (описание):")
    for desc in descriptions:
        print(f" - {desc}")
    
    print("\nСценарий 2 завершён\n")


def sc3():
    print("СЦЕНАРИЙ 3")
    print("=" * 60)
      
    displayable_collection: DisplayableCollection = DisplayableCollection()
    
    author = Author("Лев", "Толстой", 1828, 1910, "Россия", "роман", 20)
    translator = Translator(
        "Нора", "Галь", 1912, 1991, "Россия", "художественный перевод", 50,
        languages_from="английский", languages_to="русский", translated_books=70
    )
    biographer = Biographer(
        "Илья", "Толстой", 1950, None, "Россия", "биография", 5,
        subjects="Лев Толстой, русская литература",
        biographies_count=4, has_interviews=True
    )
    
    displayable_collection.add(author)
    displayable_collection.add(translator)
    displayable_collection.add(biographer)
    
    print(f"В коллекции DisplayableCollection: {len(displayable_collection)} объектов")
    
    for item in displayable_collection.get_all():
        if hasattr(item, 'display'):
            print(f"-{item.display()}")
        else:
            print(f"-{item.get_full_name()} нет метода display")
            
    
    print("\n--- Protocol Scorable ---")
    
    scorable_collection: ScorableCollection = ScorableCollection()
    
    scorable_collection.add(author)
    scorable_collection.add(translator)
    scorable_collection.add(biographer)
    
    print(f"В коллекции ScorableCollection: {len(scorable_collection)} объектов")
    
    for item in scorable_collection.get_all():
        if hasattr(item, 'score'):
            print(f"-{item.get_full_name()}: {item.score()}")
        else:
            print(f"-{item.get_full_name()} нет метода score")
    
    print("\nСценарий 3 завершён\n")

def sc4():
    from lab01.model import Author
    
    def get_author_info(author: Author) -> str:
        return f"{author.get_full_name()} ({author.birth_year})"
    
    def filter_by_genre(collection: TypedCollection[Author], genre: str) -> List[Author]:
        return collection.filter(lambda a: a.genre.lower() == genre.lower())
    
    collection = create_demo_collection()
    
    info = get_author_info(collection.get_all()[0])
    print(f"get_author_info(): {info}")
    
    romance_authors = filter_by_genre(collection, "роман")
    print(f"filter_by_genre('роман'): {len(romance_authors)} авторов")
    for a in romance_authors:
        print(f"  - {a.get_full_name()}")
    


def main():
    print("\n" + "=" * 60)
    sc1()
    sc2()
    sc3()
    sc4()
    



if __name__ == "__main__":
    main()