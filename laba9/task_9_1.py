def arif(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum / len(lst)

rating = {
    'Иванов': 20,
    'Сидоров': 68,
    'Петров': 26,
    'Смирнов': 68,
    'Воронина': 85,
    'Ярушкин': 33,
    'Осовский': 15,
    'Лунев': 98,
    'Солольникова': 99
}
lst = list(rating.values())
max_e = lst[0]
min_e = lst[0]
max_f = ''
min_f = ''

for key, value in rating.items():
    if (value > max_e):
        max_f = key
        max_e = value
    if (value < min_e):
        min_f = key
        min_e = value

print(f'Человек с наивысшем баллом: {max_f}')
print(f'Человек с наименьшем баллом: {min_f}')
print(f'Средний балл {arif(lst)}')
