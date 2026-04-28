import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lab02.model import Author
from lab03.models import Translator, Biographer
from lab05.collection import FunctionalAuthorCollection
from lab05.strategies import (
    by_full_name, by_birth_year, by_count_books, by_country_then_name,
    is_active, is_alive, is_translator, is_biographer,
    is_by_genre, is_prolific, make_year_filter,
    to_string_representation, to_short_info, extract_country,
    DiscountStrategy, BonusStrategy, ActivatorStrategy, InfoExtractorStrategy
)
from lab05.validate import (
    validate_name, 
    validate_year, 
    validate_country, 
    validate_genre, 
    validate_count_books
)


def create_demo_collection():
    collection = FunctionalAuthorCollection()

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

def sc1():
    print("-" * 60)
    print("СЦЕНАРИЙ 1")
    print("-" * 60)

    collection = create_demo_collection()
    print("\n[Исходная коллекция]")
    for item in collection.get_items():
        print(f"-{item.get_full_name()} ({item.country}) — книг: {item.count_books}")

    print("\nФильтрация жанр 'роман'")
    filtered = collection.filter_by(is_by_genre("роман"))
    print(f"найдено авторов: {len(filtered)}")
    for author in filtered.get_items():
        print(f"-{author.get_full_name()} жанр: {author.genre}")

    print("\nСортировка по полному имени")
    sorted_col = filtered.sort_by(by_full_name)
    for author in sorted_col.get_items():
        print(f"-{author.get_full_name()} — книг: {author.count_books}")

    print("\nПрименение скидки = уменьшение количества книг на 20%")
    sorted_col.apply(DiscountStrategy(0.2))
    for author in sorted_col.get_items():
        print(f"-{author.get_full_name()} — книг после скидки: {author.count_books}")

    

def sc2():
    print("-" * 60)
    print("СЦЕНАРИЙ 2")
    print("-" * 60)

    collection = create_demo_collection()

    print("\n[Исходная коллекция]")
    for author in collection.get_items():
        print(f"-{author.get_full_name()} , год: {author.birth_year} , книг: {author.count_books}")

    print("\nСортировка по году рождения")
    sorted1 = collection.sort_by(by_birth_year)
    for author in sorted1.get_items():
        print(f"-{author.get_full_name()}: {author.birth_year}")


    print("\nСортировка по количеству книг")
    sorted2 = collection.sort_by(by_count_books, reverse=True)
    for author in sorted2.get_items():
        print(f"-{author.get_full_name()}: {author.count_books} книг")

    print("\nСортировка по стране -> имени")
    sorted3 = collection.sort_by(by_country_then_name)
    for author in sorted3.get_items():
        print(f"-{author.get_full_name()} , страна: {author.country}")


def sc3():
    print("-" * 60)
    print("СЦЕНАРИЙ 3")
    print("-" * 60)

    collection = create_demo_collection()

    small_collection = FunctionalAuthorCollection()
    for i in range(3):
        small_collection.add(collection.get_items()[i])

    print("\n[Исходные авторы]")
    for author in small_collection.get_items():
        print(f"-{author.get_full_name()}: книг = {author.count_books}")

    print("\nDiscountStrategy (скидка 30%)")
    discount_strategy = DiscountStrategy(0.3)
    small_collection.apply(discount_strategy)
    for author in small_collection.get_items():
        print(f"-{author.get_full_name()}: книг после скидки = {author.count_books}")

    print("\nBonusStrategy (+10 бонусных книг)")
    bonus_strategy = BonusStrategy(10)
    small_collection.apply(bonus_strategy)
    for author in small_collection.get_items():
        print(f"-{author.get_full_name()}: книг после бонуса = {author.count_books}")

    print("\nInfoExtractorStrategy")
    full_info_strategy = InfoExtractorStrategy("full")
    short_info_strategy = InfoExtractorStrategy("short")

    print("полная информация:")
    for author in small_collection.get_items():
        print(f"  {full_info_strategy(author)}")

    print("\nкраткая информация:")
    for author in small_collection.get_items():
        print(f"  {short_info_strategy(author)}")


def sc4():
    print("-" * 60)
    print("СЦЕНАРИЙ 4")
    print("-" * 60)

    collection = create_demo_collection()

    print("\nmap()- преобразование объектов в строки")
    strings = collection.map(to_string_representation)
    for s in strings[:5]:
        print(f"  {s[:80]}...")

    print("\nmap()- краткая информация")
    short_infos = collection.map(to_short_info)
    for info in short_infos:
        print(f"  {info}")

    print("\nmap()- извлечение стран авторов")
    countries = collection.map(extract_country)
    print(f"  Страны: {set(countries)}")

    print("\nfilter()- живые авторы")
    alive = collection.filter(is_alive)
    for author in alive.get_items():
        status = "жив" if author.is_alive() else "умер"
        print(f"  - {author.get_full_name()}: {status}")

    print("\nfilter()- активные авторы")
    active_authors = collection.filter(is_active)
    for author in active_authors.get_items():
        print(f"  - {author.get_full_name()}: активен = {author.is_active}")

    print("\nФабрика фильтров: авторы, родившиеся между 1900 и 1950")
    year_filter = make_year_filter(1900, 1950)
    filtered_by_year = collection.filter(year_filter)
    for author in filtered_by_year.get_items():
        print(f"  - {author.get_full_name()}: {author.birth_year}")
    
    print("\nФабрика фильтров: prolific (>= 20 книг)")
    prolific_filter = is_prolific(20)
    prolific_authors = collection.filter(prolific_filter)
    for author in prolific_authors.get_items():
        print(f"  - {author.get_full_name()}: {author.count_books} книг")


def sc5():
    print("-" * 60)
    print("СЦЕНАРИЙ 5")
    print("-" * 60)

    collection = create_demo_collection()

    print("\nСортировка через lambda по году рождения")
    lambda_sorted = collection.sort_by(lambda a: a.birth_year or 0)
    for author in lambda_sorted.get_items()[:3]:
        print(f"  {author.get_full_name()}: {author.birth_year}")

    print("\nСортировка через функцию by_birth_year")
    named_sorted = collection.sort_by(by_birth_year)
    for author in named_sorted.get_items()[:3]:
        print(f"  {author.get_full_name()}: {author.birth_year}")


def main():
    print("\n" + "-" * 60)

    sc1()
    sc2()
    sc3()
    sc4()
    sc5()

if __name__ == "__main__":
    main()