from datetime import datetime

while 1:
    try:
        str = input("Введите год, месяц, день, час, минуту отбытия через точку: ")
        time_out = datetime.strptime(str, '%Y.%m.%d.%H.%M')
    except ValueError:
        print('Введены некорректные данные')
    else:
        break

while 1:
    try:
        str = input("Введите год, месяц, день, час, минуту прибытия через точку: ")
        time_in = datetime.strptime(str, '%Y.%m.%d.%H.%M')

    except ValueError:
        print('Введены некорректные данные')
    else:
        break

print(time_out)
print(time_in)
print(f"Путь займёт {time_in - time_out}")
