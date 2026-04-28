"""
Стратегии, фильтры, фабрики функций и callable-объекты для ЛР-5.
"""

# ==================== СТРАТЕГИИ СОРТИРОВКИ ====================

def by_full_name(author):
    """Сортировка по полному имени (фамилия + имя)."""
    return author.get_full_name().lower()


def by_birth_year(author):
    """Сортировка по году рождения."""
    return author.birth_year if author.birth_year else 0


def by_count_books(author):
    """Сортировка по количеству написанных книг."""
    return author.count_books


def by_country_then_name(author):
    """Сортировка по стране, затем по имени."""
    return (author.country.lower(), author.get_full_name().lower())


def by_translated_books(author):
    """Сортировка по количеству переведённых книг (для переводчиков)."""
    if hasattr(author, '_translated_books'):
        return author._translated_books
    return 0


def by_biographies_count(author):
    """Сортировка по количеству написанных биографий (для биографов)."""
    if hasattr(author, '_biographies_count'):
        return author._biographies_count
    return 0


# ==================== ФУНКЦИИ-ФИЛЬТРЫ ====================

def is_active(author):
    """Фильтр: активные авторы."""
    return author.is_active


def is_alive(author):
    """Фильтр: живые авторы."""
    return author.is_alive()


def is_by_genre(target_genre):
    """Фабрика фильтров: фильтр по жанру."""
    def filter_by_genre(author):
        return author.genre.lower() == target_genre.lower()
    return filter_by_genre


def is_prolific(min_books=10):
    """Фабрика фильтров: авторы с количеством книг >= min_books."""
    def filter_prolific(author):
        return author.count_books >= min_books
    return filter_prolific


def is_translator(author):
    """Фильтр: только переводчики."""
    from lab03.models import Translator
    return isinstance(author, Translator)


def is_biographer(author):
    """Фильтр: только биографы."""
    from lab03.models import Biographer
    return isinstance(author, Biographer)


# ==================== ФАБРИКИ ФУНКЦИЙ ====================

def make_price_filter(max_price):
    """
    Фабрика функций для фильтрации по максимальной цене.
    (Аналог для предметной области авторов не применим, но показываем концепцию)
    """
    def filter_fn(item):
        # Для демонстрации — у авторов нет цены, используем count_books как "ценность"
        return item.count_books <= max_price
    return filter_fn


def make_year_filter(min_year, max_year):
    """Фабрика: фильтр по диапазону годов рождения."""
    def filter_by_year_range(author):
        return (author.birth_year is not None and
                min_year <= author.birth_year <= max_year)
    return filter_by_year_range


# ==================== ФУНКЦИИ ДЛЯ MAP ====================

def to_string_representation(author):
    """Преобразование объекта в строку."""
    return str(author)


def to_short_info(author):
    """Краткая информация об авторе."""
    return f"{author.get_full_name()} ({author.count_books} книг)"


def apply_discount(discount_rate):
    """
    Фабрика: создаёт функцию для применения скидки.
    (Для демонстрации — уменьшает количество книг на discount_rate %)
    """
    def discount_books(author):
        author.count_books = int(author.count_books * (1 - discount_rate))
        return author
    return discount_books


def extract_country(author):
    """Извлечение страны автора."""
    return author.country


# ==================== ПАТТЕРН «СТРАТЕГИЯ» (CALLABLE-ОБЪЕКТЫ) ====================

class DiscountStrategy:
    """
    Стратегия применения скидки к автору (уменьшение количества книг).
    """

    def __init__(self, discount_rate):
        self.discount_rate = discount_rate

    def __call__(self, author):
        author.count_books = int(author.count_books * (1 - self.discount_rate))
        return author


class BonusStrategy:
    """
    Стратегия начисления бонусных книг автору.
    """

    def __init__(self, bonus_count):
        self.bonus_count = bonus_count

    def __call__(self, author):
        author.count_books += self.bonus_count
        return author


class ActivatorStrategy:
    """
    Стратегия активации автора.
    """

    def __call__(self, author):
        author.activate()
        return author


class InfoExtractorStrategy:
    """
    Стратегия извлечения информации об авторе.
    """

    def __init__(self, format_type="full"):
        self.format_type = format_type

    def __call__(self, author):
        if self.format_type == "full":
            return author.get_info()
        elif self.format_type == "short":
            return f"{author.get_full_name()} - {author.count_books} books"
        else:
            return author.get_full_name()