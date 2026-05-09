from typing import TypeVar

T=TypeVar('T')

s=[1,2,3]
p=(1,2,3)
f=['kisa', 'o']
def cl(items: list[T]) -> T:
    return items[1]

x=cl([1,2,3])
print(x)