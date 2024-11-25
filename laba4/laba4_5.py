def check(num: str):
    try:
        num = int(num)
    except ValueError:
        return False
    else:
        if num < 0:
            return False
        return True

def nok(a,b):
    pass

a = b = 'e'
while not check(a):
    a = input('Введите число для конвертации: ')

while not check(b):
    b = input('Введите число для конвертации: ')

a = int(a)
b = int(b)

print()