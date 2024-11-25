def nod(a, b):
    if a == b:
        return a
    if a > b:
        return nod(a - b, b)
    return nod(a, b - a)

def nok(a, b):
    return (a / nod(a, b)) * b


a = b = 'e'
while not check(a):
    a = input('Введите число: ')

while not check(b):
    b = input('Введите число: ')

a = int(a)
b = int(b)

print(nok(a, b))
