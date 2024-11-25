def check(num: str):
    try:
        num = int(num)
    except ValueError:
        return False
    else:
        return True

def progrssia_sum(b, n):
    if n==1:
        return b
    return progrssia_sum(b, n-1)

print()