class A:
    def foo(self) -> None:
        print("A.foo")


class B(A):
    def foo(self) -> None:
        print("B.foo")


class C(A):
    def foo(self) -> None:
        print("C.foo")


class D(B, C):
    pass


d = D()
d.foo()  # prints "B.foo"


# Task Nr.1:

# Define a Shape class with the following attributes and methods:

# A name attribute, which is a string that represents the name of the shape.
# A sides attribute, which is an integer that represents the number of sides of the shape.
# An area method, which returns the area of the shape.
# Then, define a Rectangle class that inherits from the Shape class and has the following attributes and methods:

# A width attribute, which is a float that represents the width of the rectangle.
# A height attribute, which is a float that represents the height of the rectangle.
# An init method that initializes the name, sides, width, and height attributes.
# An area method that overrides the area method of the Shape class and returns the area of the rectangle.
# Finally, define a Square class that inherits from the Rectangle class and has the following attributes and methods:

# A side_length attribute, which is a float that represents the length of the sides of the square.
# An init method that initializes the side_length attribute and calls the init method of the Rectangle class to initialize
#     the name, sides, width, and height attributes.


# class Shape:
#     def __init__(self, name: str, sides: int) -> None:
#         self.name = name
#         self.sides = sides

#     def area(self) -> float:
#         raise NotImplementedError

# class Rectangle(Shape):
#     def __init__(self, width: float, height: float) -> None:
#         super().__init__("Rectangle", 4)
#         self.width = width
#         self.height = height

#     def area(self) -> float:
#         return self.width * self.height

# class Square(Rectangle):
#     def __init__(self, side_length: float) -> None:
#         super().__init__(side_length, side_length)
#         self.side_length = side_length

# square = Square(5)
# print(square.name)
# print(square.sides)
# print(square.area())


# Task Nr.2:

# Create a Bus, Taxi, Train child classes that inherits from the Vehicle class.
# Implement at least five methods in a superclass what would describe those vehicles.
# The default fare charge of any vehicle is seating capacity * 100 . If Vehicle is Bus
# instance, we need to add an extra 10% on full fare as a maintenance charge.

# Sukurkite autobusų, taksi, traukinių vaikų klases, kurios paveldi iš transporto priemonės klasės.
# Superklasėje įgyvendinkite bent penkis metodus, kurie apibūdintų tas transporto priemones.
# Numatytasis bet kurios transporto priemonės bilieto mokestis yra sėdimų vietų skaičius * 100 . Jei transporto priemonė yra autobusas
# egzempliorių, turime pridėti papildomą 10% nuo visos bilieto kainos kaip priežiūros mokestį.


class Vehicle:
    def __init__(self, colour: str, seats: int, wheels: int, weight: float) -> None:
        self.seats = seats
        self.colour = colour
        self.wheels = wheels
        self.weight = weight

    def ticket_price(self) -> float:
        return self.seats * 100


class Bus(Vehicle):
    def __init__(self, colour: str, seats: int, wheels: int, weight: float) -> None:
        super().__init__(colour, seats, wheels, weight)

    def get_bus_ticket_price(self) -> float:
        return super().ticket_price() * 1.1


class Taxi(Vehicle):
    pass


class Train(Vehicle):
    def __init__(self, colour: str, seats: int, wheels: int, weight: float) -> None:
        super().__init__(colour, seats, wheels, weight)

    def train_ticket_price(self) -> float:
        return super().ticket_price()


bus = Bus(colour="red", seats=50, weight=4000, wheels=6)
print(f"bus ticket price: {bus.get_bus_ticket_price()}")

taxi = Taxi(colour="red", seats=4, weight=1000, wheels=4)
print(f"taxi ticket price: {taxi.ticket_price()}")

train = Train(colour="red", seats=1000, weight=10000, wheels=10)
print(f"train ticket price: {train.ticket_price()}")
