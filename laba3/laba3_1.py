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
