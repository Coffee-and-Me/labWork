import datetime
from datetime import datetime

time_out = time_in = ''
ls = []

"""
for t in ['год', 'месяц', 'день', 'час', 'минуты']:
    buf = 'a'
    while not buf.isdigit():
        buf = input(f"Введите {t} отбытия: ")

    time_out += f'{buf}:'

for t in ['год', 'месяц', 'день', 'час', 'минуты']:
    buf = 'a'
    while not buf.isdigit():
        buf = input(f"Введите {t} прибытия: ")

    time_in += f'{buf}:'
"""
while (1):
    try:
        str = input("Введите год, месяц, день, час, минуту отбытия через пробел: ")
        str = str.split()

        for i in range(0, len(str)):
            ls.append(int(str[i]))

        time_out = datetime(ls[0], ls[1], ls[2], ls[3], ls[4])

    except ValueError:
        print('Введены некорректные данные')
    else:
        break
ls = []
while (1):
    try:
        str = input("Введите год, месяц, день, час, минуту прибытия через пробел: ")
        str = str.split()

        for i in range(0, len(str)):
            ls.append(int(str[i]))

        time_in = datetime(ls[0], ls[1], ls[2], ls[3], ls[4])

    except ValueError:
        print('Введены некорректные данные')
    else:
        break

print(time_out)
print(time_in)
print(f"Путь займёт {time_in - time_out}")
