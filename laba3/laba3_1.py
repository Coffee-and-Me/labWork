from math import sin, cos, tan, radians

x = 'x'
x = input("Введите размер угла в градусах: ")

while not x.isdigit():
    print("Введите правильные данные в градусах")
    x = input()

x = radians(int(x))

print(f"cos(x) = {cos(x)}")
print(f"sin(x) = {sin(x)}")
print(f"tan(x) = {tan(x)}")