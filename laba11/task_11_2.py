import os
import re
def func(count: int, file: str = 'text.txt'):
    buf = 0
    with open(file, 'r', encoding='utf-8') as f:
        new_str = f.readline()
        for i in range(len(new_str)):
            if new_str[i] == '.' or new_str[i] == '!' or new_str[i] == '?':
                global new_lst
                new_lst.append(new_str[buf:i+1])
                buf = i+1
    for i in range(len(new_lst)):
        new_lst[i] = new_lst[i].strip()

    global matrix
    matrix = []
    for i in range(len(new_lst)):
        matrix.append(new_lst[i].split())

    for i in range(len(matrix)):
        if len(matrix[i]) > count:
            res = ' '.join(matrix[i])
        #print(' '.join(matrix[i]))

new_lst = []
res = ''
try:
    num = int(input('Напишите число: '))
except:
    print('Error')
    exit()
else:
    if os.path.exists('text.txt'):
        with open('textout.txt', 'w', encoding='utf-8') as f:
            f.write(res)
        #print(func(num))
        print('Всё выполнялось корректно')
    else:
        print('Такого файла не существует')
        exit()