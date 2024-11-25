def check(num: str):
    try:
        num = int(num)
    except ValueError:
        return False
    else:
        return True

def progrssia_sum(b, n, q):
    if n==1:
        return 1
    return b + progrssia_sum(b*q, n-1, q)

print(progrssia_sum(2,3,2))