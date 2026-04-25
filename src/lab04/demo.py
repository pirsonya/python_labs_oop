#!/usr/bin/env python3
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab04.models import (
    ComparableAuthor, ComparableTranslator, ComparableBiographer
)
from lab02.collection import AuthorCollection
from lab04.interfaces import Printable, Comparable

print("=" * 60)
print("1. создание объектов и вызов интерфейсных методов")
print("=" * 60)

author = ComparableAuthor("Фёдор", "Достоевский", 1821, 1881, "Россия", "роман", 15)
translator = ComparableTranslator("Иван", "Кашкин", 1899, 1963, "Россия", "перевод", 20,
                                   "английский", "русский", 45)
biographer = ComparableBiographer("Павел", "Басинский", 1961, None, "Россия",
                                   "биография", 8, "писатели", 5, True)

print("\nобъекты созданы")
print(f"автор: {author.get_full_name()}")
print(f"переводчик: {translator.get_full_name()}")
print(f"биограф: {biographer.get_full_name()}")

print("\nВызов метода to_string() (Printable)")
print(f"автор: {author.to_string()}")
print(f"переводчик: {translator.to_string()}")
print(f"биограф: {biographer.to_string()}")

print("\nВызов метода compare_to() (Comparable)")
print(f"автор (сравнение по году рождения):")
print(f"Достоевский ^ Кашкин: {author.compare_to(translator)} (отрицательное число -> первый старше)")
print(f"\nпереводчик (сравнение по кол-ву переводов):")
print(f"Кашкин ^ Басинский: {translator.compare_to(biographer)}")
print(f"\nБиограф (сравнение по кол-ву биографий):")
print(f"Басинский ^ Достоевский: {biographer.compare_to(author)}")


print("\n" + "=" * 60)
print("2. функция через интерфейс и проверка isinstance")
print("=" * 60)

def display_printable_items(items: list[Printable]) -> None:
    print("\nВывод через интерфейс Printable")
    for item in items:
        print(f"-{item.to_string()}")


mixed_objects = [author, translator, biographer]

display_printable_items(mixed_objects)

print("\nпроверка isinstance")
for obj in mixed_objects:
    print(f"{obj.get_full_name()}:")
    print(f"    Printable? {isinstance(obj, Printable)}")
    print(f"    Comparable? {isinstance(obj, Comparable)}")

print("\nобъекты реализуют несколько интерфейсов")
for obj in mixed_objects:
    interfaces = []
    if isinstance(obj, Printable):
        interfaces.append("Printable")
    if isinstance(obj, Comparable):
        interfaces.append("Comparable")
    print(f"{obj.get_full_name()} -> реализует: {', '.join(interfaces)}")


print("\n" + "=" * 60)
print("3. фильтрация коллекции по интерфейсу")
print("=" * 60)

collection = AuthorCollection()
collection.add(author)
collection.add(translator)
collection.add(biographer)

collection.add(ComparableAuthor("Анна", "Ахматова", 1889, 1966, "Россия", "поэзия", 12))
collection.add(ComparableTranslator("Самуил", "Маршак", 1887, 1964, "Россия", "перевод", 30,
                                     "английский", "русский", 120))

print(f"всего объектов в коллекции: {len(collection)}")
print("список всех объектов:")
for obj in collection.get_all():
    print(f"  - {obj.get_full_name()} ({type(obj).__name__})")

print("\nфильтрация: только Printable объекты")
print(f"количество Printable объектов: {len([obj for obj in collection.get_all() if isinstance(obj, Printable)])}")

print("\nфильтрация: только Comparable объекты")
comparable_objects = [obj for obj in collection.get_all() if isinstance(obj, Comparable)]
for obj in comparable_objects:
    print(f"  - {obj.get_full_name()} (можно сравнивать через compare_to)")

def filter_by_interface(col: AuthorCollection, interface_type) -> AuthorCollection:
    new_collection = AuthorCollection()
    for obj in col.get_all():
        if isinstance(obj, interface_type):
            new_collection.add(obj)
    return new_collection

print("\nфильтрация через отдельную функцию с возвратом коллекции")
printable_collection = filter_by_interface(collection, Printable)
print(f"отфильтровано Printable объектов: {len(printable_collection)}")
print("имена отфильтрованных объектов:")
for obj in printable_collection.get_all():
    print(f"  - {obj.get_full_name()}")


