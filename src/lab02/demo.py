from model import Author
from collection import AuthorCollection

def main():
    print("\nСОЗДАНИЕ ЭКЗЕМПЛЯРОВ КЛАССА AUTHOR")
    print("-" * 50)

    author1 = Author("Александр", "Пушкин", 1799, 1837, "Россия", "поэзия", 15)
    author2 = Author("Лев", "Толстой", 1828, 1910, "Россия", "роман", 20)
    author3 = Author("Фёдор", "Достоевский", 1821, 1881, "Россия", "роман", 12)
    author4 = Author("Агата", "Кристи", 1890, 1976, "Великобритания", "детектив", 66)
    author5 = Author("Джордж", "Оруэлл", 1903, 1950, "Великобритания", "роман", 9)
    author6 = Author("Виктор", "Пелевин", 1962, None, "Россия", "роман", 18)

    authors = [author1, author2, author3, author4, author5, author6]

    print("созданы экземпляры класса Author:")
    for author in authors:
        print(f"  - {author.get_full_name()} ({author.birth_year}-{author.death_year if author.death_year else 'наст. время'})")

 
    print("\nСОЗДАНИЕ КОЛЛЕКЦИИ AuthorCollection")
    print("-" * 50)

    collection = AuthorCollection()

    print("\nдобавление объектов в коллекцию")
    print("-" * 50)

    for author in authors:
        collection.add(author)
        print(f"добавлен: {author.get_full_name()}")

    

    print("\nпроверка на дубликаты")
    print("-" * 50)

    try:
        duplicate = Author("Александр", "Пушкин", 1799, 1837, "Россия", "поэзия", 15)
        collection.add(duplicate)
        print("ошибка: дубликат не должен был добавиться")
    except ValueError as e:
        print(f"корректная ошибка: {e}")

    print("\nпроверка типа объекта")
    print("-" * 50)

    try:
        collection.add("это строка, а не автор")
        print("ошибка: строка не должна была добавиться")
    except TypeError as e:
        print(f"корректная ошибка: {e}")

    print("\nВЫВОД ВСЕХ ЭЛЕМЕНТОВ")
    print("-" * 50)

    all_authors = collection.get_all()
    for author in all_authors:
        print(f"- {author.get_full_name()}")

    print("\nИТЕРАЦИЯ ПО КОЛЛЕКЦИИ")
    print("-" * 50)

    for idx, author in enumerate(collection):
        print(f"[{idx}] {author.get_full_name()}")

    print("\nПОИСК ПО АТРИБУТАМ")
    print("-" * 50)

    print("поиск по фамилии 'Толстой':")
    found = collection.find_by_surname("Толстой")
    for author in found:
        print(f"{author.get_full_name()}")

    print("\nпоиск по жанру 'роман':")
    found = collection.find_by_genre("роман")
    for author in found:
        print(f"{author.get_full_name()}")

    print("\nпоиск по стране 'Великобритания':")
    found = collection.find_by_country("Великобритания")
    for author in found:
        print(f"{author.get_full_name()}")

    print("\nпоиск активных авторов:")
    found = collection.find_active()
    for author in found:
        print(f"{author.get_full_name()} (активен)")

    print("\nпоиск по полному имени 'Лев Толстой':")
    found = collection.find_by_full_name("Лев", "Толстой")
    print(f"{found.get_full_name() if found else 'Не найден'}")

    print("\nДОСТУП ПО ИНДЕКСУ")
    print("-" * 50)

    print(f"collection[0] = {collection[0].get_full_name()}")
    print(f"collection[2] = {collection[2].get_full_name()}")
    print(f"collection[-1] = {collection[-1].get_full_name()}")


    print("\nУДАЛЕНИЕ ПО ИНДЕКСУ")
    print("-" * 50)

    print(f"удаление collection[5] ({collection[5].get_full_name()}):")
    removed = collection.remove_at(5)
    print(f"удалён: {removed.get_full_name()}")
    print(f"сейчас в коллекции {len(collection)} авторов:")

    for idx, author in enumerate(collection):
        print(f"    [{idx}] {author.get_full_name()}")

    print("\nУДАЛЕНИЕ ОБЪЕКТА")
    print("-" * 50)

    print(f"удаляем {author3.get_full_name()}:")
    collection.remove(author3)
    print(f"после удаления в коллекции {len(collection)} авторов:")

    for idx, author in enumerate(collection):
        print(f"    [{idx}] {author.get_full_name()}")

    print("\nПОПЫТКА УДАЛИТЬ НЕСУЩЕСТВУЮЩЕГО АВТОРА")
    print("-" * 50)

    try:
        fake_author = Author("Несуществующий", "Автор", 2000, None, "Страна", "жанр", 0)
        collection.remove(fake_author)
        print("ошибка: несуществующий автор не должен был удалиться")
    except ValueError as e:
        print(f"корректная ошибка: {e}")

    print("\nСОРТИРОВКА")
    print("-" * 50)

    print("сортировка по году рождения:")
    sorted_by_birth = collection.sort_by_birth_year()
    for author in sorted_by_birth:
        print(f"    {author.birth_year} — {author.get_full_name()}")

    print("\nсортировка по количеству книг:")
    sorted_by_books = collection.sort_by_count_books(reverse=True)
    for author in sorted_by_books:
        print(f"    {author.count_books} книг — {author.get_full_name()}")

    print("\nсортировка по полному имени:")
    sorted_by_name = collection.sort_by_full_name()
    for author in sorted_by_name:
        print(f"    {author.get_full_name()}")

    print("\nФИЛЬТРАЦИЯ")
    print("-" * 50)

    print("живые авторы:")
    alive = collection.get_alive()
    for author in alive:
        print(f"    🟢 {author.get_full_name()} (род. {author.birth_year})")

    print("\nавторы жанра 'роман':")
    novel_authors = collection.get_by_genre("роман")
    for author in novel_authors:
        print(f"{author.get_full_name()}")

    print("\nавторы из России:")
    russian = collection.get_by_country("Россия")
    for author in russian:
        print(f"{author.get_full_name()}")

    print("\nактивные авторы:")
    active = collection.get_active()
    for author in active:
        print(f"{author.get_full_name()}")

    print("\nпо кол-ву книг (> 15 книг):")
    prolific = collection.get_prolific(15)
    for author in prolific:
        print(f"{author.get_full_name()} — {author.count_books} книг")

    print("\nпроверка __len__")
    print("-" * 50)

    print(f"  len(collection) = {len(collection)}")

    print("\nпроверка __repr__")
    print("-" * 50)

    print(f"  {repr(collection)}")

    print("\nитоговое стостояние коллекции")
    print("-" * 50)

    print(f"В коллекции осталось {len(collection)} авторов:")
    for author in collection:
        status = "активен" if author.is_active else "неактивен"
        alive_status = "жив" if author.is_alive() else f"умер в {author.death_year}"
        print(f"{author.get_full_name()} — {alive_status}, {status}, {author.count_books} книг")


if __name__ == "__main__":
    main()