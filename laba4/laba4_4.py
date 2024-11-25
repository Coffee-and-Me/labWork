from sys import setrecursionlimit
setrecursionlimit(1_000_000)

def check(num: str):
    try:
        num = int(num)
    except ValueError:
        return False
    else:
        if num < 0:
            return False
        return True
def conv(n, base):
    rel = ''
    symb = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while (n > 0):
        k = n % base
        rel = symb[k] + rel
        n = n // base

    return rel

n = 'e'
while not check(n):
    n = input('Введите число для конвертации: ')

n = int(n)

print(f'Число {n} в двоичном представлении: {conv(n, 2)}')