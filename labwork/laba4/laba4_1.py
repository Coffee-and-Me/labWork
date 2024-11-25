def check(num: str):
    try:
        num = int(num)
    except ValueError:
        return False
    else:
        return True

def progrssia(b, n):

    if n == 1:
        return 1
    return progrssia(b, n-1) * b

print(-3*progrssia(4, 5))
