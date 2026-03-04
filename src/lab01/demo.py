from model import Author

def main():
    author1 = Author("Александр", "Пушкин", 1799, 1937, "Россия", "роман", 200)
    author2 = Author("Михаил", "Булгаков", 1891, 1940, "Россия", "роман", 150)
    author3 = Author("Анна", "Ахматова", 1889, 1966, "Россия", "поэзия", 50)
    author4 = Author("Оскар", "Уальд", 1854, 1900, "Ирландия", "драма", 100)

    print("-информация об авторах-\n")
    for author in [author1, author2, author3, author4]:
            print(author.get_info())

    print("\n-магические методы-")
    print(author4)
    print(repr(author4))

    print("\n-проверка валидации-")
    try:
        author_invalid = Author("", "Пушкин", 1799, 1837, "Россия", "поэзия", 100)
    except ValueError as e:
        print(f"есть ошибка: {e}")

    try:
        author_invalid = Author("Александр", "Пушкин", 1799, 1837, "Россия", "фэнтези", 100)
    except ValueError as e:
        print(f"есть ошибка: {e}")

    try:
        author_invalid = Author("Александр", "Пушкин", 1799, 1837, "Россия", "поэзия", -5)
    except ValueError as e:
        print(f"есть ошибка: {e}")

    print("\n-сеттеры-")
    print(f"текущий жанр автора: {author4.genre}")
    author4.genre = "ромком"  
    print(f"новый жанр автора: {author4.genre}")

    print(f"текущее кол-во книг автора: {author4.count_books}")
    author4.count_books = 2234
    print(f"новое кол-во книг author4: {author4.count_books}")

    print("\n-атрибуты класса-")
    print(f"доступные жанры (через класс): {Author.get_available_genres()}")
    print(f"доступные жанры (через экземпляр): {author1.get_available_genres()}")

    Author.add_genre("фантастика")
    print(f"после добавления 'фантастика': {Author.get_available_genres()}")

    print("\n-демонстрация логических состояний-")
    print(f"этот автор активен: {author4.is_active}")

    author4.deactivate()
    print(f"после деактивации: {author4.is_active}")
        
    print(f"полное имя автора1: {author1.get_full_name()}")
    print(f"инициалы автора1: {author1.get_initials()}")
    print(f"жив/мертв ли автор4: {author4.is_alive()}")
    print(f"возраст автора4 в 2017 году: {author4.get_age_in_year(2000)}")
    print(f"текущий возраст атвора3: {author3.get_current_age()}")
    print(f"период жизни автора3: {author3.get_life_period()}")
        


if __name__ == "__main__":
    main()

            