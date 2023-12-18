# Nasa needs to calculate expenses for the new mission: using OOP principles implement Base and
# Space Shuttle classes. Create a simple calculator with:

# Base class should give a functionality to know info about spacecraft (age, cost, year built, weight etc.. ).
# Through the main class you should be able to calculate the mission cost which includes: fuel cost (FUEL_COST x BURN_RATE
#  (kg/mile) * BURN_RATE_VARIABLE (2500 / orbit_height(in miles))) , average personals expenditures ( ppl x base_salary ).
# Prepare the final report in the file document and on screen with a method get_full_report with all gathered and calculated data.


# NASA turi apskaičiuoti išlaidas naujai misijai: naudodama OOP principus įgyvendinti "Base" ir "Space Shuttle" klases.
# Sukurkite paprastą skaičiuoklę su:
# Bazinė klasė turėtų suteikti funkcionalumą, leidžiantį žinoti informaciją
# apie erdvėlaivius (amžius, kaina, pastatymo metai, svoris ir kt.).
# Per pagrindinę klasę turėtumėte sugebėti apskaičiuoti misijos išlaidas,
# į kurias įeina: kuro sąnaudos (FUEL_COST x BURN_RATE (kg / mylia) * BURN_RATE_VARIABLE (2500 / orbit_height (myliomis))) ,
# vidutinės asmeninės išlaidos ( ppl x base_salary ).
# Paruoškite galutinę ataskaitą bylos dokumente ir ekrane, naudodami metodą, get_full_report su visais
# surinktais ir apskaičiuotais duomenimis.


# class Base:
#     def __init__(self, age: int, cost: float, year_built: int, weight: float) -> None:
#         self.age = age
#         self.cost = cost
#         self.year_built = year_built
#         self.weight = weight

#     def get_info(self):
#         return f"age: {self.age}, Cost: {self.cost}, built year: {self.year_built}, Weight: {self.weight}"


# class SpaceShuttle(Base):
#     def __init__(
#         self,
#         age: int,
#         cost: float,
#         year_built: int,
#         weight: float,
#         orbit_height: float,
#         fuel_cost: float,
#         base_salary: int,
#         burn_rate: int,
#         ppl: int,
#     ):
#         super().__init__(age, cost, year_built, weight)
#         self.orbit_height = orbit_height
#         self.fuel_cost = fuel_cost
#         self.base_salary = base_salary
#         self.burn_rate = burn_rate
#         self.ppl = ppl

#     def BURN_RATE_VARIABLE(self) -> float:
#         return 2500 / self.orbit_height

#     def get_fuel_cost(self):
#         return self.fuel_cost * self.burn_rate * self.BURN_RATE_VARIABLE()

#     def personals_expenditures(self):
#         return self.ppl * self.base_salary
#     # def get_full_report(self):
#     #     return

# shuttle = SpaceShuttle(
#     age=1,
#     cost=50000,
#     year_built=2022,
#     weight=15000,
#     orbit_height=10000,
#     fuel_cost=100,
#     base_salary=50000,
#     burn_rate=1000,
#     ppl=100,
# )

# print(f"average personals expenditures: {shuttle.personals_expenditures()}$")
# # print(shuttle.BURN_RATE_VARIABLE())
# print(f"fuel cost:{shuttle.get_fuel_cost()} $")


# Saruno PVZ

from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def get_fuel_cost(self) -> float:
        pass

    @abstractmethod
    def personal_expenditures(self) -> float:
        pass

    def spacecraft_info(self) -> str:
        pass


class Space(Base):
    BURN_RATE_VARIABLE = 2500

    def __init__(
        self,
        age: int,
        cost: float,
        year_built: int,
        weight: float,
        fuel_cost: float,
        burn_rate: float,
        orbit_height: float,
        personal: int,
        base_salary: float,
    ) -> None:
        self._age = age
        self._cost = cost
        self._year_built = year_built
        self._weight = weight
        self.fuel_cost = fuel_cost
        self.burn_rate = burn_rate
        self.orbit_height = orbit_height
        self.personal = personal
        self.base_salary = base_salary

    def spacecraft_info(self) -> str:
        return f"Spacecraft age - {self._age}, cost - {self._cost} EUR, year built - {self._year_built}, weight -{self._weight} kg."

    def get_fuel_cost(self) -> float:
        return round(
            self.fuel_cost
            * self.burn_rate
            * (self.BURN_RATE_VARIABLE / self.orbit_height),
            2,
        )

    def personal_expenditures(self) -> float:
        return self.personal * self.base_salary

    def get_full_report(self) -> str:
        report = f"Spacecraft info: {self.spacecraft_info()} Mission info: fuel cost - {self.get_fuel_cost()} Eur., personal cost - {self.personal_expenditures()} Eur."

        with open("report.txt", "a") as file:
            file.write(report + "\n")

            return report


spacecraft = Space(
    age=4,
    cost=500000000,
    year_built=2022,
    weight=100000,
    fuel_cost=10.3,
    burn_rate=2,
    orbit_height=1000,
    personal=4,
    base_salary=100000,
)
print(spacecraft.get_full_report())
