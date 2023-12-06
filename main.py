# pratymas vaikscioimas pirmin<, adgal> per itemus

# import subprocess

# lis = [5, 6, 7]

# i = 0


# while True:
#     print("Index of list item: ", i)
#     user_input = input()
#     if user_input == ">":
#         i += 1
#         try:
#             print(lis[i])

#         except IndexError as err:
#             print("End of the list")
#             i -= 1
#             # i = len(lis) - 1
#             # print(lis[i])
#     elif user_input == "<":
#         if i == 0:
#             i += 1
#         i -= 1
#         try:
#             print(lis[i])

#         except IndexError as err:
#             print("End of the list")
#             i += 1


# Problem:
#  Write a function that takes a list of integers and returns their average. Raise a TypeError if the input
# is not a list or if any element in the list is not an integer. Provide a solution that addresses this error.


# from typing import List

# list1 = [1, 2, 3, 4, 5]

# def get_average(a: List[int]) -> float:

#     if all(isinstance(n, (int, float)) for n in a):
#         if a:
#             return sum(a) / len(a)
#         else:
#             raise ValueError("Empty list, cannot calculate average")
#     else:
#         raise TypeError("Type error problem in the given argument")

# try:
#     average = get_average(list1)
#     print("Average:", average)
# except (TypeError, ValueError) as err:
#     print("Error:", err)


# def get_average(num_list: list) -> float:
#     if not isinstance(num_list, list):
#         raise TypeError("Input should be a list")

#     if not all(isinstance(num, (int, float)) for num in num_list):
#         raise TypeError("Input should be a list of int or float")

#     if len(num_list) == 0:
#         raise ValueError("Empty list")

#     return sum(num_list) / len(num_list)

# try:
#     result = get_average([1, 2, 3, 4, 5])
#     print(f"The average is: {result}")

# except (TypeError, ValueError) as e:
#     print(f"Error: {e}")
# Write a function that takes a list of integers and returns their average.
# Raise a TypeError if the input is not a list or if any element in the list is not an integer.
# Provide a solution that addresses this error.


# numbers = [5, 47, 6, 485, 1, 521, 8, 184, 1, 7, 5, 52, 562]
# numbers_not = [5, 47, 6, 485, 1, "a", 8, 184, 1, 7, 5, 52, 562]
# numbers_not_again = "5, 47, 6, 485, 1, 521, 8, 184, 1, 7, 5, 52, 562"


# def calculate_average(numb: list) -> float:
#     if type(numb) is not list or not numb:
#         raise TypeError("Not a list or is empty list")
#     numb_check = [x for x in numb if type(x) == int]
#     # print(numb_check)
#     if numb_check != numb:
#         raise TypeError("Not all items of the list are integers")
#     return round((sum(numb) / len(numb)), 2)


# def try_calculate_averages(*args: list) -> list:
#     averages = []
#     for arg in args:
#         try:
#             averages.append(calculate_average(arg))
#         except TypeError as e:
#             if str(e) == "Not a list or is empty list":
#                 print("Not a list or is empty list")
#             elif str(e) == "Not all items of the list are integers":
#                 print("Not all items of the list are integers")
#                 try:
#                     fixed_list = [int(x) for x in arg]
#                     averages.append(calculate_average(fixed_list))
#                 except ValueError:
#                     print("Unable to quickfix your problem!")
#         except Exception as e:
#             print(f"Unexpected problem {e}")
#     return averages


# print(try_calculate_averages(numbers, numbers_not, numbers_not_again))


# Problem:
#  Create a function that reads a file and returns its contents. Raise a
# FileNotFoundError if
# the file does not exist. Provide a solution that handles this error.


def read_file(file):
    try:
        with open(file, "r") as f:
            contents = f.readlines()
        return contents
    except FileNotFoundError:
        print("Filenot found")
        return None


file_contents = read_file("file.txt")
if file_contents is not None:
    print(file_contents)


# def is_leap_year(year):
#     if 1600 <= year <= 4000:
#         if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#           return True
#         else:
#             return False


