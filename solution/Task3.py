import math

planet1 = input("Планета №1: ")
r1 = float(input("Радиус ее орбиты (млн. км): "))
v1 = float(input("Ее орбитальная скорость (км/с): "))

r1 = r1 * 1000000  # переводим миллионы км в просто км

year1 = 2 * math.pi * r1 / v1
year1 = year1 / (60 * 60 * 24)  # переводим секунды в дни

planet2 = input("Планета №2: ")
r2 = float(input("Радиус ее орбиты (млн. км): "))
v2 = float(input("Ее орбитальная скорость (км/с): "))

r2 = r2 * 1000000

year2 = 2 * math.pi * r2 / v2
year2 = year2 / (60 * 60 * 24)

print("Длина года в днях на планете %s: %2.f" % (planet1, year1))
print("Длина года в днях на планете %s: %2.f" % (planet2, year2))

print("Длина года на %s больше, чем на %s? %s" % (planet1, planet2, year1 > year2))