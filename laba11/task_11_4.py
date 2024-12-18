import os

lst = []
res = []


def func(file: str = 'book.txt'):
    global res
    global lst
    with open(file, 'r', encoding='utf-8') as f:
        for i in f.readlines():
            if i != '\n':
                lst.append(i.strip())

    for i in range(len(lst)):
        if lst[i].startswith('Глава') or lst[i].startswith('Charter'):
            res.append(f'{lst[i]}. {lst[i + 1]}')

    return res


if os.path.exists('book.txt'):
    with open('Content.txt', 'w', encoding='utf-8') as f:
        f.write('Оглавление\n\n')
        for i in func():
            f.write(i + '\n')
    print('Всё выполнялось корректно')
else:
    print('Такого файла не существует')
    exit()
