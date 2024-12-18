import os

lst = []


def func(remv: int, file: str = "input.txt"):
    with open(file, 'r') as f:
        try:
            lst = list(map(float, f.readline().split()))
        except ValueError:
            print('error')
            exit()

    lst = list(map(str, lst[:-remv]))
    lst = ' '.join(lst)

    with open('output.txt', 'w') as f:
        f.write(lst)


try:
    num = int(input('Напишите число: '))
    if num < 0:
        raise ValueError

except:
    print('Error')
    exit()
else:
    if os.path.exists('input.txt'):
        func(num)
        print('Всё выполнялось корректно')
    else:
        print('Такого файла не существует')
        exit()
