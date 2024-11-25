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


def arif_progr(a1, d, n):
    if n == 1:
        return a1
    return arif_progr(a1, d, n - 1) + d


element = q = n = 'e'
while not check(element):
    element = input('Введите первый член прогрессии: ')

while not check(q):
    q = input('Введите слагаемое: ')

while not check(n):
    n = input('Введите искомый член прогрессии: ')

element = int(element)
q = int(q)
n = int(n)

print(arif_progr(element, q, n))
