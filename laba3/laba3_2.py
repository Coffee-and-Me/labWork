<<<<<<< HEAD
from math import gcd
=======
rom math import gcd
>>>>>>> 2b3cd06c7e3a1a1741c55793d2933f7128f48958


def nod(num_one, num_two):
    maxm = 0

    if num_one == num_two: return num_one
    if num_one == 0 or num_two == 0: return 1
    if num_one % num_two == 0 or num_two % num_one == 0:
        return min(num_one, num_two)

    for i in range(1, num_one // 2 + 1):
        if num_one % i == 0 and num_two % i == 0:
            maxm = i

    return maxm


num_1 = num_2 = '0'
n_one, n_two = 'a', 'b'

while 1:
    try:
        n_one = input("Введите первое число: ")
        num_1 = int(n_one)
    except ValueError:
        continue
    else:
        break

while 1:
    try:
        n_two = input("Введите второе число: ")
        num_2 = int(n_two)
    except ValueError:
        continue
    else:
        break

print(nod(num_1, num_2))
print(gcd(num_1, num_2))
