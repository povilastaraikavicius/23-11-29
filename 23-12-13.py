# class MyString:
#     def __init__(self, value: str):
#         self.value = value

#     def add_exclamation(self) -> 'MyString':
#         self.value += "!"
#         return self

#     def make_upper(self) -> 'MyString':
#         self.value = self.value.upper()
#         return self

# my_string = MyString("hello")
# my_string.add_exclamation().make_upper()

# print(my_string.value) # output: "HELLO!"

# class Person:
#     def __init__(self, name: str):
#         self.name = name
#         self.name_length = None
#         self.email = None

#     def set_name_length(self) -> "Person":
#         self.name_length = len(self.name)
#         return self

#     def create_email(self, surname: str) -> "Person":
#         DEFAULT_EMAIL_PROVIDER = "@gmail.com"
#         self.email = self.name + "." + surname + DEFAULT_EMAIL_PROVIDER
#         return self

#     def get_name(self) -> str:
#         return self.name


# person = Person("Jonas")
# person.set_name_length().create_email(surname="Jonaitis")
# print(f"Email: {person.email}\nName length: {person.name_length}")


# Task Nr.1:

# Create a class Person that has two methods: set_name and set_age, which set the name and age attributes of the class, respectively.
# Modify these methods to return self, so that the calls can be chained together.


# class Person:
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age

#     def set_name(self, name: str):
#         self.name = name
#         return self

#     def set_age(self, age: int):
#         self.age = age
#         return self


# person = Person()
# person.set_name("Alice").set_age(30)

# print(f"Name: {person.name}, Age: {person.age}")


# Create a class Currency that has the following properties:

# code: A 3-letter currency code (e.g. "USD", "EUR", "GBP")
# amount
# exchange_rate
# Create the following methods:

# set_code: A method that accepts a 3-letter currency code and sets the code attribute of the object
# set_amount: A method that accepts a float number and sets the amount attribute of the object
# set_exchange_rate: A method that accepts a float number and sets the exchange_rate attribute of the object
# convert: A method that accepts a 3-letter currency code and a float number representing the new exchange rate, and
# calculates the new amount of currency based on the exchange rate.
# str: A method that returns a string representation of the Currency object in the following format "code: amount"
# Each method should return the instance of the class to allow method chaining.

# Klasės valiutos, turinčios šias ypatybes, kūrimas:

# kodas: 3 raidžių valiutos kodas (pvz., "USD", "EUR", "GBP")
# suma
# exchange_rate
# Sukurkite šiuos metodus:

# set_code: metodas, kuris priima 3 raidžių valiutos kodą ir nustato objekto kodo atributą
# set_amount: metodas, kuris priima plūdės numerį ir nustato objekto kiekio atributą
# set_exchange_rate: metodas, kuris priima plūdės numerį ir nustato exchange_rate objekto atributą
# konvertuoti: metodas, kuris priima 3 raidžių valiutos kodas ir kintamasis skaičius, nurodantis naująjį valiutos kursą, ir
# apskaičiuoja naują valiutos sumą pagal valiutos kursą.
# str: metodas, grąžinantis valiutos objekto eilutės atvaizdavimą tokiu formatu "kodas: suma"
# Kiekvienas metodas turėtų grąžinti klasės egzempliorių, kad būtų galima sujungti metodą.


from typing import Union


class Currency:
    def __init__(self) -> None:
        self.code = None
        self.amount = None
        self.exchange_rate = None
        self.prev_code = None

    def set_code(self, code: str) -> "Currency":
        self.code = code
        return self

    def set_amount(self, amount: float) -> "Currency":
        self.amount = amount
        return self

    def set_exchange_rate(self, exchange_rate: float) -> "Currency":
        self.exchange_rate = exchange_rate
        return self

    def convert(self, new_code: str, new_exchange_rate: float) -> Union[str, float]:
        self.amount = self.amount * new_exchange_rate
        self.prev_code = self.code
        self.code = new_code
        self.exchange_rate = new_exchange_rate
        return self.amount, self.code, self.exchange_rate

    def __str__(self) -> str:
        return f"Converted from {self.prev_code} to {self.code}: {self.amount}"


currency = Currency()

currency.set_code("EUR").set_amount(1000.0)
currency.convert(new_code="USD", new_exchange_rate=1.2)
print(currency)
