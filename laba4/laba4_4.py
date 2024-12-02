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
    if n == 0:
        return 0
    else:
        return conv(n // 2) * 10 + n % 2


n = 'e'
while not check(n):
    n = input('Введите число для конвертации: ')

n = int(n)

print(f'Число {n} в двоичном представлении: {conv(n)}')
