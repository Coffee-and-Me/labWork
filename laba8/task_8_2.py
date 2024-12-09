st1 = set(input('Первая строка: '))
st2 = set(input('Вторая сторка: '))

if len(st1) <= len(st2):
    print('Не существует таких символов')
    exit()

print(st1 - st2)
