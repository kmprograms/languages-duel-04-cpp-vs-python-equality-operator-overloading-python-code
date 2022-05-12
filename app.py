# Przygotuj klasę Person z polami skladowymi name oraz age.
# Przygotuj klasę do pracy z operatorem ==

import json
from dataclasses import dataclass


# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#     def __eq__(self, other):
#         return isinstance(other, Person) \
#                and json.dumps(self.__dict__) == json.dumps(other.__dict__)
#
#     # def __ne__(self, other):

@dataclass
class Person:
    name: str
    age: int

def main() -> None:
    p1 = Person('JAN', 10)
    p2 = Person('JAN', 10)
    p3 = Person('JAN', 11)
    print(p1 == p2)
    print(p1 != p3)


if __name__ == '__main__':
    main()

