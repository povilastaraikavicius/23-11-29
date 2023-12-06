# from datetime import datetime, date

# x = date.today()
# print(x)
# print(type(x))

# import datetime

# now = datetime.datetime.now()
# print(now)
# print(now - datetime.timedelta(days=5))
# print(now + datetime.timedelta(hours=5))
# print(now + datetime.timedelta(days=20, hours=8))


# Parašyti programą, kuri:

# Atspausdintų dabartinę datą ir laiką
# Atimtų iš dabartinės datos ir laiko 5 dienas ir juos atspausdintų
# Pridėti prie dabartinės datos ir laiko 8 valandas ir juos atspausdintų
# Atspausdintų dabartinę datą ir laiką tokiu formatu: 2019 03 08, 09:57:17
# Patarimas: naudoti datetime, timedelta (from datetime import timedelta)

# from datetime import datetime, timedelta

# now = datetime.now()
# print(now)
# print(now - timedelta(days=5))
# print(now + timedelta(hours=8))
# print(now.strftime("%Y %m %d  %I:%M:%S"))


# arašyti programą, kuri:

# Leistų vartotojui įvesti norimą datą ir laiką (pvz. gimtadienį)
# Paskaičiuotų ir atspausdintų, kiek nuo įvestos datos ir laiko praėjo:
# Metų
# Mėnesių
# Dienų
# Valandų
# Minučių
# Sekundžių
# Kadangi tiksliai galima paskaičiuoti tik dienas ir sekundes, metus, mėnesius ir t.t. paskaičiuokite apytiksliai.
# Patarimas: naudoti datetime, .days, .total_seconds()

# Skaičių suapvalinimo pavyzdys (kurio gali prireikti šioje užduotyje):

# skaicius = 4.66

# print(round(skaicius))


import datetime

ivesta_data = input("Įveskite datą: ")

data = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d")

skirtumas = datetime.datetime.now() - data

print(skirtumas.days)
