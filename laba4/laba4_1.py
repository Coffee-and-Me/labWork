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

def progrssia(b, n):

    if n == 1:
        return 1
    return progrssia(b, n-1) * b

element = q = n = 'e'
while not check(element):
    element = input('Введите первый член прогрессии: ')

while not check(q):
    q = input('Введите множитель: ')

while not check(n):
    n = input('Введите искомый член прогрессии: ')

element = int(element)
q = int(q)
n = int(n)

print(element*progrssia(q, n))
