import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab03.models import Translator, Biographer
from lab02.collection import AuthorCollection
from lab02.model import Author  



def main():
    print("\n1. СОЗДАНИЕ ОБЪЕКТОВ")
    print("-" * 40)

    lopukhina = Translator(
        name="Анна", surname="Лопухина",
        birth_year=1985, country="Россия",
        genre="перевод",
        languages_from="английский, французский",
        languages_to="русский",
        translated_books=15
    )
    lopukhina.add_book(3)  
    lopukhina.add_translation(5)

    volkov = Biographer(
        name="Сергей", surname="Волков",
        birth_year=1972, country="Россия",
        genre="биография",
        subjects="Пушкин, Толстой, Достоевский",
        biographies_count=4,
        has_interviews=True
    )
    volkov.add_biography()  
    volkov.add_biography()  

    smirnov = Translator(
        name="Иван", surname="Смирнов",
        birth_year=1990, country="Россия",
        languages_from="немецкий",
        languages_to="русский, английский",
        translated_books=8
    )

    print(f"создан: {lopukhina.get_full_name()}")
    print(f"создан: {volkov.get_full_name()}")
    print(f"создан: {smirnov.get_full_name()}")

    print("\n2. КОЛЛЕКЦИЯ АВТОРОВ")
    print("-" * 40)

    collection = AuthorCollection()
    collection.add(lopukhina)
    collection.add(volkov)
    collection.add(smirnov)

    print(f"авторов в коллекции: {len(collection)}")

    print("\n3. ПОЛИМОРФИЗМ")
    print("-" * 40)

    for author in collection.get_all():
        if hasattr(author, "calculate"):
            result = author.calculate()
            print(f"{author.get_full_name():<5}  продуктивность: {result}")

    print("\n4. ФИЛЬТРАЦИЯ ПО ТИПУ isinstance")
    print("-" * 40)

    translators = [a for a in collection.get_all() if isinstance(a, Translator)]
    biographers = [a for a in collection.get_all() if isinstance(a, Biographer)]

    print(f"переводчиков: {len(translators)}")
    for t in translators:
        print(f"{t.get_full_name()} — {t.get_language_pair()}")

    print(f"\nБиографов: {len(biographers)}")
    for b in biographers:
        print(f"{b.get_full_name()} — пишет о: {b._subjects}")

    print("\n5. УНИКАЛЬНЫЕ МЕТОДЫ ДОЧЕРНИХ КЛАССОВ")
    print("-" * 40)

    print(f"переводчик- {lopukhina.get_full_name()}:")
    print(f"языковая пара: {lopukhina.get_language_pair()}")
    print(f"эффективность перевода: {lopukhina.translation_efficiency():.2f}")

    print(f"\nбиограф- {volkov.get_full_name()}:")
    print(f"главный объект: {volkov.get_main_subject()}")
    print(f"метод работы: {volkov.is_research_based()}")

    print("\n6. ПЕРЕОПРЕДЕЛЁННЫЕ МЕТОДЫ get_info, __str__")
    print("-" * 40)

    print("get_info() для переводчика")
    print(lopukhina.get_info())

    print("\nget_info() для биографа")
    print(volkov.get_info())

    print("\n__str__() для переводчика")
    print(lopukhina)

    print("\n__str__() для биографа")
    print(volkov)

    print("\n7. РАБОТА С СЕТТЕРАМИ")
    print("-" * 40)

    print(f"до: жанр {lopukhina.get_full_name()} - {lopukhina.genre}")
    lopukhina.genre = "художественный перевод"
    print(f"после: жанр - {lopukhina.genre}")

    print(f"\nкниг у {volkov.get_full_name()}: {volkov.count_books}")
    volkov.count_books = 10
    print(f"обновлено: {volkov.count_books} книг")


    print("\n8. АКТИВАЦИЯ/ДЕАКТИВАЦИЯ")
    print("-" * 40)

    print(f"{smirnov.get_full_name()} активен: {smirnov.is_active}")
    smirnov.deactivate()
    print(f"после деактивации: {smirnov.is_active}")

    try:
        smirnov.add_translation(3)
    except RuntimeError as e:
        print(f"ошибка: {e}")

    smirnov.activate()
    print(f"после активации: {smirnov.is_active}")
    smirnov.add_translation(3)
    print(f"переведено книг: {smirnov._translated_books}")


    print("\n9. СРАВНЕНИЕ ЭКЗЕМПЛЯРОВ (__eq__)")
    print("-" * 40)

    translator_copy = Translator(
        name="Анна", surname="Лопухина",
        birth_year=1985, country="Россия"
    )
    print(f"{lopukhina.get_full_name()} - {translator_copy.get_full_name()}: "
          f"{lopukhina == translator_copy}")

    print(f"{lopukhina.get_full_name()} - {volkov.get_full_name()}: "
          f"{lopukhina == volkov}")

    print("\n10. ДОСТУПНЫЕ ЖАНРЫ (классовый метод)")
    print("-" * 40)
    print(f"доступные жанры: {Author.get_available_genres()}")
    Author.add_genre("биография")
    Author.add_genre("перевод")
    print(f"после добавления: {Author.get_available_genres()}")



if __name__ == "__main__":
    main()