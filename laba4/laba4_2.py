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

def progrssia_sum(b, n, q):
    if n==1:
        return b
    return b + progrssia_sum(b*q, n-1, q)

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

print(progrssia_sum(element ,n, q))