import numpy as np

m = n = k = 0
matrix_1 = matrix_2 = []

while 1:
    try:
        m = int(input('Число m: '))
    except ValueError:
        print('error')
    else:
        if m <= 0: continue
        break

while 1:
    try:
        k = int(input('Число k: '))
    except ValueError:
        print('error')
    else:
        if k <= 0: continue
        break

while 1:
    try:
        n = int(input('Число n: '))
    except ValueError:
        print('error')
    else:
        if k <= 0: continue
        break

print(f'Введите первую матрицу размера {m}x{k}')
for i in range(m):
    try:
        matrix_1.append(list(map(int, input().split()))[:k])
    except ValueError:
        print('Неверные данные. Программа обиделась(')
        exit()

print(f'Введите первую матрицу размера {k}x{n}')
for i in range(k):
    try:
        matrix_2.append(list(map(int, input().split()))[:n])
    except ValueError:
        print('Неверные данные. Программа обиделась(')
        exit()

matrix_1 = np.array(matrix_1[:m])
matrix_2 = np.array(matrix_2[:k])

matrix_res = np.dot(matrix_1, matrix_2)
print(matrix_res)
