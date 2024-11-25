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
<<<<<<< HEAD
print(f"Путь займёт {time_in - time_out}")
=======
print(f"Путь займёт {time_in - time_out}")
>>>>>>> 2b3cd06c7e3a1a1741c55793d2933f7128f48958
