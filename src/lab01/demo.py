from model import Author

def main():

    print("\nСОЗДАНИЕ ЭКЗЕМПЛЯРОВ")
    print("-" * 50)
    
    author1 = Author("Александр", "Пушкин", 1799, 1837, "Россия", "роман", 200)
    author2 = Author("Михаил", "Булгаков", 1891, 1940, "Россия", "роман", 150)
    author3 = Author("Анна", "Ахматова", 1889, 1966, "Россия", "поэзия", 50)
    author4 = Author("Оскар", "Уайльд", 1854, 1900, "Ирландия", "драма", 100)
    
    authors = [author1, author2, author3, author4]
    
    print("Созданы 4 экземпляра Author:")
    for author in authors:
        print(f"   - {author.get_full_name()} ({author.birth_year}-{author.death_year if author.death_year else 'наст. время'})")
    
    print("\nвывод через print (__str__)")
    print("-" * 50)
    for author in authors:
        print(author)
    
    print("\nвывод через repr (__repr__)")
    print("-" * 50)
    for author in authors:
        print(repr(author))
    
    print("\nсравнение объектов (__eq__)")
    print("-" * 50)
    
    author1_copy = Author("Александр", "Пушкин", 1799, 1837, "Франция", "поэзия", 500)
    
    print(f"Пушкин (оригинал) == Пушкин (копия): {author1 == author1_copy}")
    print(f"Совпадают имя, фамилия, год рождения = True")
    print(f"\nПушкин == Булгаков: {author1 == author2}")
    print(f"Разные фамилии = False")
    print(f"\nПушкин == Ахматова: {author1 == author3}")
    print(f"Разные имена и фамилии = False")
    

    print("\nпопытка создать экземпляр с некорректным именем")
    print("-" * 50)
    try:
        author_invalid = Author(123, "Пушкин", 1799, 1837, "Россия", "роман", 100)
        print("ошибка: объект не должен был создаться")
    except TypeError as e:
        print(f"Корректная ошибка: {e}")
    
   
    print("\nпопытка установить пустую строку через сеттер")
    print("-" * 50)
    try:
        author1.country = ""
        print(f"cтрана рождения успешно установлена: '{author1.country}'")
    except ValueError as e:
        print(f"ошибка: {e}")

    print("\nпопытка установить отрицательное количество книг")
    print("-" * 50)
    try:
        author1.count_books = -50
        print("ошибка: отрицательное кол-во книг не должно устанавливаться")
    except ValueError as e:
        print(f"Корректная ошибка: {e}")
    
 
    print("\nпопытка создать автора некорректным годом смерти")
    print("-" * 50)
    try:
        author_invalid = Author("Иван", "Грозный", 1584, 1530, "Россия", "драма", 1)
        print("ошибка: объект не должен был создаться")
    except ValueError as e:
        print(f"Корректная ошибка: {e}")
    
  
    print("\nпопытка создать автора с пустым именем")
    print("-" * 50)
    try:
        author_invalid = Author("", "Пушкин", 1799, 1837, "Россия", "роман", 100)
        print("ошибка: объект не должен был создаться")
    except ValueError as e:
        print(f"Корректная ошибка: {e}")
    

    

    print("\nпроверка начального состояния")
    print("-" * 50)
    print(f"Автор {author4.get_full_name()}:")
    print(f"-Активен: {author4.is_active}")
    print(f"-Количество книг: {author4.count_books}")
    

    print("\nдобавление книг автору в список")
    print("-" * 50)
    author4.add_book(5)
    print(f"Количество книг после добавления: {author4.count_books}")
  
    
  
    print("\nдеактивация автора")
    print("-" * 50)
    author4.deactivate()
    print(f"Активен: {author4.is_active}")
    
 
    print("\nпопытка обновить кол-во книг неактивному автору")
    print("-" * 50)
    try:
        author4.update_count_books(500)
        print("ошибка: не должно быть возможности обновлять книги неактивного автора")
    except RuntimeError as e:
        print(f"Корректная ошибка: {e}")


    print("\nполучение списка жанров/категорий")
    print("-" * 50)
    print(f"жанры: {Author.get_available_genres()}")
    

    print("\nдобавление нового жанра")
    print("-" * 50)
    Author.add_genre("фантастика")
    print(f"обновлённый список жанров: {Author.get_available_genres()}")
    
 
    print("\nдобавление нескольких жанров")
    print("-" * 50)
    Author.add_genre("триллер")
    Author.add_genre("фэнтези")
    print(f"После добавления 'триллер' и 'фэнтези': {Author.get_available_genres()}")
    
   
    print("\nдоступ к списку жанров через экземпляр")
    print("-" * 50)
    print(f"author1.get_available_genres(): {author1.get_available_genres()}")
   
    

    
   
    print("\nсоздание автора (жив, активен)")
    print("-" * 50)
    living_author = Author("Виктор", "Пелевин", 1962, None, "Россия", "роман", 20)
    print(f"Автор: {living_author.get_full_name()}")
    print(f"Год рождения: {living_author.birth_year}")
    print(f"Жив: {living_author.is_alive()}")
    

    print("\nполучение возраста автора в разные годы")
    print("-" * 50)
    print(f"возраст {living_author.get_full_name()} в 2000 году: {living_author.get_age_in_year(2000)} лет")
    print(f"возраст в 2010 году: {living_author.get_age_in_year(2010)} лет")
    print(f"возраст в 2026 году: {living_author.get_current_age()} лет")
    print(f"возраст в 2050 году: {living_author.get_age_in_year(2050)} лет")
    
 
    print("\nполучение периода жизни автора")
    print("-" * 50)
    print(f"{author1.get_full_name()}: {author1.get_life_period()}")
    print(f"{living_author.get_full_name()}: {living_author.get_life_period()}")
    

    print("\nполучение инициалов")
    print("-" * 50)
    for author in authors:
        print(f"  {author.get_full_name()} → {author.get_initials()}")
    

    print("\nполная информация (get info) обо всех авторах")
    print("-" * 50)
    for author in authors:
        print(author.get_info())
    

    print("\nизменение жанра через сеттер")
    print("-" * 50)
    print(f"текущий жанр {author4.get_full_name()}: {author4.genre}")
    author4.genre = "комедия"
    print(f"новый жанр: {author4.genre}")



if __name__ == "__main__":
    main()