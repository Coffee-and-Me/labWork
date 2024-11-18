from math import gcd


def nod(num_one, num_two):
    max = 0

    if num_one == num_two: return num_one
    if num_one == 0 or num_two == 0: return 1
    if num_one % num_two == 0 or num_two % num_one == 0:
        return min(num_one, num_two)

    for i in range(1, num_one // 2 + 1):
        if num_one % i == 0 and num_two % i == 0:
            max = i

    return max


n_one, n_two = 'a', 'b'

while not n_one.isdigit():
    n_one = input("Введите первое число: ")

while not n_two.isdigit():
    n_two = input("Введите второе число: ")


print(nod(int(n_one), int(n_two)))
print(gcd(int(n_one), int(n_two)))
