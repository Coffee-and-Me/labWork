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

#os.chdir('labWork/laba10')
#print(os.listdir(path='.'))

try:
    num = int(input('Напишите число: '))
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