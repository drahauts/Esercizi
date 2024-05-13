class Animal:
    def __init__(self, specie: str, age: int) -> None:
        self.specie = specie
        self.age = age

    def __str__(self) -> str:
        return f"Species = {self.specie}, age = {self.age}"
class Person(Animal):
    def __init__(self, name: str, surname: str, cf: str, specie :str, age: int) -> None:
        super().__init__(self.specie, self.age)
        self.name = name
        self.surname = surname
        self.cf = cf

    def __str__(self) -> str:
        return f"({self.name.capitalize()}{self.surname.capitalize()}(cf = {self.cf}), age = {self.age}, specie = {self.specie}"


class Cat(Animal):
    def __init__(self, name: str, age: int) -> None:
        super().__init__("felidai", age)
        self.name = name

""" def __str__(self) -> str:
        return super().__str__()"""

class Rabbit(Animal):
    pass

class Student(Person):
    pass

p = Person(name="Lorenzo", surname= "Maggi", cf= "bella", specie= "Homo Sapiens", age= 22)
a = Animal(specie="Balana", age=25)
c = Cat(name= "Garfield", age= 15)
print(p)
print(a)
print(c)