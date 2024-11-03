a, b, c = 'a', 'a', 'a'


def check(max, x1, x2):
    if (x1 ** 2 + x2 ** 2 == max ** 2):
        print("Прямоугольный")
    elif (x1 ** 2 + x2 ** 2 > max ** 2):
        print("Остроугольный")
    elif (x1 ** 2 + x2 ** 2 < max ** 2):
        print("Тупоугольный")


while not (a.isdigit()):
    a = input('Введите сторону: a=')

while not (b.isdigit()):
    b = input('Введите сторону: b=')

while not (c.isdigit()):
    c = input('Введите сторону: c=')

a = int(a)
b = int(b)
c = int(c)

if (a + b > c and a + c > b and b + c > a):
    if (a >= b and a >= c):
        check(a, b, c)
    elif (b >= a and b >= c):
        check(b, a, c)
    elif (c >= a and c >= b):
        check(c, a, b)

else:
    print("Такого треугольника не существует")
