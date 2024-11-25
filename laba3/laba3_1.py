<<<<<<< HEAD
from math import sin, cos, tan, radians

x = input("Введите размер угла в градусах: ")

while 1:
    try:
        x = input("Введите правильные данные в градусах: ")
        x = radians(float(x))
    except ValueError:
        continue
    else:
        break

print(f"cos(x) = {cos(x)}")
print(f"sin(x) = {sin(x)}")
print(f"tan(x) = {tan(x)}")
=======
from math import sin, cos, tan, radians

while 1:
    try:
        x = input("Введите правильные данные в градусах: ")
        x = radians(float(x))
    except ValueError:
        continue
    else:
        break

print(f"cos(x) = {cos(x)}")
print(f"sin(x) = {sin(x)}")
print(f"tan(x) = {tan(x)}")
>>>>>>> 2b3cd06c7e3a1a1741c55793d2933f7128f48958
