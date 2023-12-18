# from abc import ABC, abstractmethod


# class Vehicle(ABC):
#     @abstractmethod
#     def get_vehicle_type(self) -> str:
#         pass

#     def return_collor(self) -> str:
#         return "Black"


# class Plane(Vehicle):
#     def get_vehicle_type(self) -> str:
#         return "Plane"


# ticket = Plane()

# print(ticket.return_collor())


# Task Nr.1:

# Create an abstract class Animal with which takes name of animal as an input and initialize it.
#  The create speak abstract method, to be overridden by subclasses. And get_name method which returns name of the animal.

# Now create two subclasses of Animals: Dog and Cat which overrides the speak method,
# and provide the implementation which returns a string "Dog says Woof!" and "Cat says Meow!" respectively.


# from abc import ABC, abstractmethod


# class Animal(ABC):
#     def __init__(self, name: str)->None:
#         self.name = name

#     @abstractmethod
#     def speak(self)->str:
#         pass

#     def get_name(self):
#         return self.name


# class Dog(Animal):
#     def speak(self)->str:
#         return f"Dog {self.name} says Woof!"


# class Cat(Animal):
#     def speak(self)->str:
#         return f"Cat {self.name} says Meow!"


# dog = Dog("Skubi")
# cat = Cat("Mike")


# print(dog.speak())
# print(cat.speak())


# Alberto pvz


# from abc import ABC, abstractmethod


# class Animal(ABC):
#     def __init__(self, name: str) -> None:
#         self.name = name

#     def get_name(self) -> str:
#         return self.name

#     @abstractmethod
#     def speak(self) -> str:
#         pass


# class Dog(Animal):
#     def speak(self) -> str:
#         return "Dog says Woof!"


# class Cat(Animal):
#     def speak(self) -> str:
#         return "Cat says Meow!"


# name = input("Enter animal name: ")

# dog = Dog(name=name)

# print(dog.get_name())
# print(dog.speak())


# Task Nr.3:

# As per previous examples please create an example of your own. The abstract class should contain
#     five (3 abstract and 2 normal ) methods. Create 2 subclasses that would inherit abstract class.
# Kaip nurodyta ankstesniuose pavyzdžiuose, sukurkite savo pavyzdį. Abstrakčioje klasėje turėtų būti
# penki (3 abstraktūs ir 2 normalūs ) metodai. Sukurkite 2 poklasius, kurie paveldėtų abstrakčią klasę.


# from abc import ABC, abstractmethod


# class Tyres(ABC):
#     def __init__(self, model: str) -> None:
#         self.model = model

#     @abstractmethod
#     def price(self) -> str:
#         pass

#     def get_model(self) -> str:
#         return self.model


# class Winter(Tyres):
#     def price(self) -> str:
#         return f"Winter tyres {self.model} price is 150 eu."


# class Summer(Tyres):
#     def price(self) -> str:
#         return f"Summer tyres {self.model} price is 100 eu."


# winter_tyres = Winter("Dunlop")
# summer_tyres = Summer("Goodyear")


# print(winter_tyres.price())
# print(summer_tyres.price())


# Create a Calculator program : it should contain abstract class with
#  methods (abstract and not), base class, geometry, arithmetic calculator classes. Every subclass should have
#  at least 5 methods to make some meaningful calculus operations.


from abc import ABC, abstractmethod


class Calculator(ABC):
    def _init_(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    @abstractmethod
    def sum(self, x, y):
        pass

    @abstractmethod
    def subtract(self, x, y):
        pass

    @abstractmethod
    def multiply(self, x, y):
        pass

    @abstractmethod
    def divide(self, x, y):
        pass

   


class Arithmetic(Calculator):
    def sum(self, x: int, y: int) -> int:
        return x + y

    def subtract(self, x: int, y: int) -> int:
        return x - y

    def multiply(self, x: int, y: int) -> int:
        return x * y

    def divide(self, x: int, y: int) -> float:
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"


class Geometry(Calculator):
    def area_of_rectangle(self, length: int, width: int) -> int:
        return length * width

    def area_of_square(self, side):
        return side**2


arith_calc = Arithmetic()
geom_calc = Geometry()


print("sum:", arith_calc.sum(5, 3))
print("subtract:", arith_calc.subtract(5, 3))
print("multiply:", arith_calc.multiply(5, 3))
print("divide:", arith_calc.divide(5, 3))

print("Area of Rectangle:", geom_calc.area_of_rectangle(5, 8))
