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
    if n==1:
        return a1
    return arif_progr(a1, d, n-1) + d

print(arif_progr(1, 1, 3))