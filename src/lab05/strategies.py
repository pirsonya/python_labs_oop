# стратегии сортировки

def by_full_name(author):
    """стратегия сортировки по полному иемни автора
    Args:
    объект Author (или его наследник) с методом get_full_name()
    Returns:
    полное имя автора (str) в нижнем регистре для сортировки
    """
    return author.get_full_name().lower()

def by_birth_year(author):
    """стратегия сортировки по году рождения автора
    Args:
    объект Author (или его наследник) с методом birth_year
    Returns:
    год рождения автора(int) -> 0, если None
    """
    return author.birth_year if author.birth_year else 0

def by_count_books(author):
    """стратегия сортировки по кол-ву написанных книг
    Args:
    объект Author (или его наследник) с методом count_books
    Returns:
    количество написанных книг(int)
    """
    return author.count_books

def by_country_then_name(author):
    """стратегия сортировки сначала по стране рождение и затем по полному имени
    Args:
    объект Author (или наследник) с атрибутами country и методом get_full_name()
    Returns:
    страна в нижнем регистре, полное имя в нижнем регистре. (tuple)"""
    return (author.country.lower(), author.get_full_name().lower())

def by_translated_books(author):
    """стратегия сортировки по кол-ву переведенных книг(для переводчиков)
    Args:
    объект Author (или наследник), может иметь атрибут _translated_books
    Returns:
    количество переведённых книг (int) -> 0, если атрибут отсутствует
    """
    if hasattr(author, '_translated_books'):
        return author._translated_books
    return 0

def by_biographies_count(author):
    """"стратегия сортировки по кол-ву написанных биографий(для биографов). 
    Для обычных авторов возвращает 0, чтобы они оказались в начале списка
    Args:
    объект Author (или наследник), может иметь атрибут _biographies_count
    Returns:
    количество написанных биографий (int) -> 0, если атрибут отсутствует
    """
    if hasattr(author, '_biographies_count'):
        return author._biographies_count
    return 0



# функции-фильтры

def is_active(author):
    """фильтр: оставляет только активных авторов
    Args:
    объект Author (или наследник) с атрибутом is_active
    Returns:
    True, если автор активен, иначе False (bool)
    """
    return author.is_active

def is_alive(author):
    """фильтр: оставляет только живых авторов (тех, у кого death_year is None).
    Args:
    объект Author (или наследник) с методом is_alive()
    Returns:
    True, если автор жив, иначе False (bool)
    """
    return author.is_alive()

def is_translator(author):
    """фильтр: оставляет только объекты класса Translator
    Args:
    объект Author (или наследник)    
    Returns:
    True, если автор является экземпляром Translator, иначе False (bool)
    """
    from lab03.models import Translator
    return isinstance(author, Translator)

def is_biographer(author):
    """фильтр: оставляет только объекты класса Biographer
    Args:
    объект Author (или наследник)
    Returns:
    True, если автор является экземпляром Biographer, иначе False (bool)"""
    from lab03.models import Biographer
    return isinstance(author, Biographer)

# фабрики функций

def is_by_genre(target_genre):
    """фабрика фильтров: создаёт функцию для фильтрации авторов по жанру.
    Args:
    целевой жанр для фильтрации (target_genre)
    Returns:
    функция, принимающая автора и возвращающая bool (Callable)"""
    def filter_by_genre(author):
        return author.genre.lower() == target_genre.lower()
    return filter_by_genre

def is_prolific(min_books=10):
    """фабрика фильтров: создаёт функцию для фильтрации продуктивных авторов.
    Args:
    минимальное количество книг для отбора (min_books)
    Returns:
    функция, принимающая автора и возвращающая bool (Callable)"""
    def filter_prolific(author):
        return author.count_books >= min_books
    return filter_prolific



def make_price_filter(max_price):
    """фабрика фильтров: создаёт функцию для фильтрации по максимальной цене.
    Args:
    максимальное значение для отбора (max_price)
    Returns:
    функция, принимающая автора и возвращающая bool (Callable)"""
    def filter_fn(item):
        return item.count_books <= max_price
    return filter_fn

def make_year_filter(min_year, max_year):
    """фабрика фильтров: создаёт функцию для фильтрации по диапазону годов рождения
    Args:
    минимальный год рождения (min_year)
    максимальный год рождения (max_year)  
    Returns:
    функция, принимающая автора и возвращающая bool (Сallable)"""
    def filter_by_year_range(author):
        return (author.birth_year is not None and
                min_year <= author.birth_year <= max_year)
    return filter_by_year_range


# функции для map

def to_string_representation(author):
    """преобразует объект автора в строковое представление
    Args:
    объект Author (или наследник)
    Returns:
    строковое представление автора через __str__"""
    return str(author)

def to_short_info(author):
    """преобразует объект автора в краткую строку с именем и количеством книг.
    Args:
    объект Author (или наследник)
    Returns:
    строка формата "Имя Фамилия (N книг)"""
    return f"{author.get_full_name()} ({author.count_books} книг)"

def apply_discount(discount_rate):
    """фабрика: создаёт функцию для применения скидки к количеству книг автора
    Args:
    размер скидки (от 0 до 1), например 0.2 = скидка 20% (discount_rate)
    Returns:
    функция, принимающая автора и возвращающая его же после изменений"""
    def discount_books(author):
        author.count_books = int(author.count_books * (1 - discount_rate))
        return author
    return discount_books

def extract_country(author):
    """извлекает страну автора
    Args:
    объект Author (или наследник) с атрибутом country
    Returns:
    название страны (str)
    """
    return author.country


# паттерн-стратегия. Callable-объекты

class DiscountStrategy:
    """cтратегия применения скидки к автору (уменьшение количества книг)"""
    def __init__(self, discount_rate):
        self.discount_rate = discount_rate

    def __call__(self, author):
        """применяет скидку к автору"""
        author.count_books = int(author.count_books * (1 - self.discount_rate))
        return author

class BonusStrategy:
    """стратегия начисления бонусных книг автору"""
    def __init__(self, bonus_count):
        self.bonus_count = bonus_count

    def __call__(self, author):
        """добавляет бонусные книги к атору"""
        author.count_books += self.bonus_count
        return author

class ActivatorStrategy:
    """cтратегия активации автора"""
    def __call__(self, author):
        author.activate()
        return author

class InfoExtractorStrategy:
    """cтратегия извлечения информации об авторе в разных форматах"""
    def __init__(self, format_type="full"):
        self.format_type = format_type

    def __call__(self, author):
        if self.format_type == "full":
            return author.get_info()
        elif self.format_type == "short":
            return f"{author.get_full_name()} - {author.count_books} books"
        else:
            return author.get_full_name()