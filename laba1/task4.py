from math import sqrt


def check(s):
    if s[0] == '-':
        if s[1::].isdigit():
            return s[1::].isdigit()
    else:
        if s.isdigit():
            return s.isdigit()


x, y, z = 'a', 'a', 'a'

while not (check(x)):
    print('Введите вектор OX')
    x = input()

while not (check(y)):
    print('Введите вектор OY')
    y = input()

while not (check(z)):
    print('Введите вектор OZ')
    z = input()

x, y, z = abs(int(x)), abs(int(y)), abs(int(z))

print(sqrt(x * x + y * y + z * z))
