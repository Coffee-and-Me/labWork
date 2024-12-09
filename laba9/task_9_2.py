library = {
    'Достоеский': ['Преступление и наказание'],
    'Страуд': ['Агенство Локвуд и Компания']
}

print('-'*5 + 'Авторы' + '-'*5)
for i in library.keys():
    print(i)
print()

st = input('Введите фамилию: ').lower().capitalize()
if st in library.keys():
    for i in library[i]:
        print(i)

    buf = input('Хотите добавить список? [1/0] ')
    if buf == '0':
        pass
    else:
        buf = input('Книга: ')
        library[st].append(buf)
else:
    print('Кажется такого автора нет, давайте добавим его произведение')
    buf = input()
    library[st] = []
    library[st].append(buf)
print()
print('-'*5 + 'Итог' + '-'*5)
for key, value in library.items():
    print(f'{key}: {value}')
