# class Circle:
#     PI = 3.14159

#     def __init__(self, radius: float) -> None:
#         self.radius = radius

#     def area(self) -> float:
#         return Circle.calculate_area(self.radius)

#     @staticmethod
#     def calculate_area(radius: float) -> float:
#         return Circle.PI * radius ** 2


# Task Nr.1:

# Create a class which takes temperature measurements in Kelvins and
#  add static methods to transform those to Celsius and Fahrenheit units.


# class TemperatureConverter:
#     def __init__(self, kelvins: float) -> None:
#         self.kelvins = kelvins

#     @staticmethod
#     def kelvin_to_celsius(kelvin: float) -> float:
#         return kelvin - 273.15

#     @staticmethod
#     def kelvin_to_fahrenheit(kelvin: float) -> float:
#         return (kelvin - 273.15) * 9 / 5 + 32


# kelvins = 300

# celsius_temperature = TemperatureConverter.kelvin_to_celsius(kelvins)
# print(f"{celsius_temperature}°C")

# fahrenheit_temperature = TemperatureConverter.kelvin_to_fahrenheit(kelvins)
# print(f"{fahrenheit_temperature}°F")


# Task Nr.2:

# Create a class that would take at least five imperial system measurements and would transform
# with the help of static methods to metric system units.


# class Imperial:
#     @staticmethod
#     def inches_to_centimeters(inches:float)->float:
#         return inches * 2.54

#     @staticmethod
#     def feet_to_meters(feet:float)->float:
#         return feet * 0.3048

#     @staticmethod
#     def yards_to_meters(yards:float)->float:
#         return yards * 0.9144

#     @staticmethod
#     def miles_to_kilometers(miles:float)->float:
#         return miles * 1.60934

#     @staticmethod
#     def pounds_to_kilograms(pounds:float)->float:
#         return pounds * 0.453592


# inches_value = 10
# feet_value = 5
# yards_value = 2
# miles_value = 3
# pounds_value = 150

# print(f"{Imperial.inches_to_centimeters(inches_value)} cm")
# print(f"{Imperial.feet_to_meters(feet_value)} m")
# print(f"{Imperial.yards_to_meters(yards_value)} m")
# print(f"{Imperial.miles_to_kilometers(miles_value)} km")
# print(f"{Imperial.pounds_to_kilograms(pounds_value)} kg")


# Sauliaus PVZ

# class ConvertToMetric:
#     FOOT_RATIO_TO_METER: float = 0.3048
#     YARD_RATIO_TO_METER: float = 0.9144
#     POUND_RATIO_TO_KG: float = 0.45359237
#     TON_RATIO_TO_KG: float = 1016.0469088
#     GALLON_RATIO_TO_LITERS: float = 4.54609

#     @staticmethod
#     def calculate_foot_to_meters(foot: float) -> float:
#         return ConvertToMetric.FOOT_RATIO_TO_METER * foot

#     @staticmethod
#     def calculate_yard_to_meters(yard: float) -> float:
#         return ConvertToMetric.YARD_RATIO_TO_METER * yard

#     @staticmethod
#     def calculate_pound_to_kg(pound: float) -> float:
#         return ConvertToMetric.POUND_RATIO_TO_KG * pound

#     @staticmethod
#     def calculate_ton_to_kg(ton: float) -> float:
#         return ConvertToMetric.TON_RATIO_TO_KG * ton

#     @staticmethod
#     def calculate_gallon_to_liters(gallon: float) -> float:
#         return ConvertToMetric.GALLON_RATIO_TO_LITERS * gallon


# print(ConvertToMetric.calculate_foot_to_meters(foot=100.0))
# print(ConvertToMetric.calculate_yard_to_meters(yard=100.0))
# print(ConvertToMetric.calculate_pound_to_kg(pound=100.0))
# print(ConvertToMetric.calculate_ton_to_kg(ton=0.001))
# print(ConvertToMetric.calculate_gallon_to_liters(gallon=100.0))


# Task Nr.3:

# Create a class called TimeUtils that has a static method called time_to_seconds that takes a time string in the format hh:mm:ss and
# returns the total number of seconds represented by that time. Use functional programing paradigm.


# class TimeUtils:
#     @staticmethod
#     def time_to_seconds(time_str: str) -> int:
#         hours, minutes, seconds = map(int, time_str.split(":"))
#         return (hours * 3600) + (minutes * 60) + seconds


# print(TimeUtils.time_to_seconds("01:30:00"))
# print(TimeUtils.time_to_seconds("12:30:00"))


# class TimeUtils:
#     @staticmethod
#     def time_to_seconds(time_str):
#         hours, minutes, seconds = map(int, time_str.split(":"))

#         total_seconds = hours * 3600 + minutes * 60 + seconds
#         return total_seconds

# time_string = "01:30:00"
# total_seconds = TimeUtils.time_to_seconds(time_string)
# print(f'Total seconds in "{time_string}" are: {total_seconds}')

# from datetime import datetime


# class TimeUtils:
#     @staticmethod
#     def time_to_seconds(time_str):
#         time_obj = datetime.strptime(time_str, "%H:%M:%S")

#         total_seconds = time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second
#         return total_seconds


# time_string = "02:30:45"
# total_seconds = TimeUtils.time_to_seconds(time_string)
# print(f'Total seconds in "{time_string}" are: {total_seconds}')


# Task Nr.4:

# Create a class called Employee with a static method called calculate_payroll that takes a list
# of Employee instances and returns the total amount to be paid to all
#  employees. Each Employee instance has two attributes: name and salary.


# from typing import List
# class Employee:

#     def __init__(self, name: str, salary: float) -> None:
#         self.name = name
#         self.salary = salary

#     @staticmethod
#     def calculate_payroll(employ_list: List["Employee"]) -> float:
#         return sum(employ.salary for employ in employ_list)


# employ_list = [
#     Employee("Tomas", 1000.0),
#     Employee("Andrius", 2000.0),
#     Employee("Jonas", 1500.0),
# ]
# print(Employee.calculate_payroll(employ_list))


# alberto PVZ


# from typing import List


# class Employee:
#     def __init__(self, name: str, salary: float) -> None:
#         self.name = name
#         self.salary = salary

#     @staticmethod
#     def calculate_payroll(employee_list: List["Employee"]) -> float:
#         salary_list = [employee.salary for employee in employee_list]
#         return sum(salary_list)


# employee1 = Employee(name="Jonas", salary=1500)
# employee2 = Employee(name="Diana", salary=600)
# employee3 = Employee(name="Agne", salary=700)
# employee4 = Employee(name="Darius", salary=2000)
# employee5 = Employee(name="Paulius", salary=1600)
# employee_list = [employee1, employee2, employee3, employee4, employee5]

# print(Employee.calculate_payroll(employee_list))
