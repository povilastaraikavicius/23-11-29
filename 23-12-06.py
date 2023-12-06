# class Person:
#     def get_age(self) -> int:
#         raise NotImplementedError("")


# class Worker(Person):
#     def get_age(self) -> int:
#         return 53


# class Player(Person):
#     pass


# age_worker = Worker()

# print(age_worker.get_age())


# Create two classes: Shape and Rectangle.
# The Shape class should have the following attributes: name and color.
# It should also have a method called get_area() that returns the abstract area of a shape.

# The Rectangle class should inherit from the Shape class
# and should have the following attributes: width and height.
# It should also override the get_area() method to calculate the area of
#  a rectangle using its width and height.


# class Shape:
#     def __init__(self, name: str, color: str) -> None:
#         self.name = name
#         self.color = color

#     def get_area(self):
#         raise NotImplementedError("")


# class Rectangle(Shape):
#     def __init__(self, name: str, color: str, width: int, height: int)-> None:
#         super().__init__(name, color)
#         self.width = width
#         self.height = height

#     def get_area(self):
#         return self.width * self.height


# rectangle = Rectangle("Rectangle", "Blue", 5, 10)


# print(f"rectangle: {rectangle.get_area()}")


# class Shape:
#     ABSTRACT_AREA = 2

#     def __init__(self, name: str, color: str) -> None:
#         self.name = name
#         self.color = color

#     def get_area(self) -> int:
#         return self.ABSTRACT_AREA


# class Rectangle(Shape):
#     def __init__(self, name: str, color: str, width: int, height: int) -> None:
#         super().__init__(name, color)
#         self.height = height
#         self.width = width

#     def get_area(self) -> int:
#         return self.width * self.height


# rectangle = Rectangle(name="Rectangle", color="Green", width=7, height=8)

# print(f"Area of rectangle: {rectangle.get_area()}")


# Create a class hierarchy for representing different types of geometric figures, such as rectangles, circles, and triangles.
# Each class should have attributes for defining the shape's characteristics, such as dimensions or parameters.
# Use inheritance and method overriding to define methods for calculating the area and perimeter of different shapes
# Possible shapes: Circle, Polygon, RegularPolygon(Polygon), Rectangle(RegularPolygon)


# import math


# class Polygons:
#     def __init__(self, name: str, color: str) -> None:
#         self.name = name
#         self.color = color

#     def get_area(self) -> int:
#         raise NotImplementedError("The are is not defined")

#     def get_perimeter(self) -> int:
#         raise NotImplementedError("The perimeter is not defined")


# class RegularPolygon(Polygons):
#     def __init__(self, name: str, color: str) -> None:
#         super().__init__(name, color)


# class Rectangle(RegularPolygon):
#     def __init__(self, name: str, color: str, width: int, height: int) -> None:
#         super().__init__(name, color)
#         self.width = width
#         self.height = height

#     def get_area(self) -> int:
#         return self.width * self.height

#     def get_perimeter(self) -> int:
#         return (self.width + self.height) * 2


# class Circle(Polygons):
#     def __init__(self, name: str, color: str, radius: int) -> None:
#         super().__init__(name, color)
#         self.radius = radius

#     def get_area(self) -> float:
#         return math.pi * math.sqrt(self.radius)

#     def get_perimeter(self) -> int:
#         return 2 * math.pi * self.radius


# class Triangle(Rectangle):
#     def __init__(
#         self, name: str, color: str, width: int, height: int, a: int, b: int, c: int
#     ) -> None:
#         super().__init__(name, color, width, height)
#         self.a = a
#         self.b = b
#         self.c = c

#     def get_area(self) -> float:
#         return super().get_area() / 2

#     def get_perimeter(self) -> int:
#         return self.a + self.b + self.c


# area_1 = Rectangle(width=102, height=203, name="rect", color="red")
# area_2 = Triangle(
#     width=102, height=203, name="triangle", color="yellow", a=12, b=11, c=9
# )
# area_3 = Circle(name="circle", color="blue", radius=25)

# area_4 = Polygons(name="hdg", color="dfss")

# print(
#     f" Area of rectangle: {area_1.get_area():.2f}, perimeter {area_1.get_perimeter():.2f}"
# )
# print(
#     f" Area of triangle: {area_2.get_area():.2f}, perimeter {area_2.get_perimeter():.2f}"
# )
# print(
#     f" Area of circle: {area_3.get_area():.2f}, perimeter {area_3.get_perimeter():.2f}"
# )



