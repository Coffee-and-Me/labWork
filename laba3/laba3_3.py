from datetime import datetime, strptime

time_out = time_in = ''
ls = []

while 1:
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
while 1:
    try:
        strg = input("Введите год, месяц, день, час, минуту прибытия через пробел: ")
        strg = strg.split()

        for i in range(0, len(strg)):
            ls.append(int(strg[i]))

        time_in = datetime(ls[0], ls[1], ls[2], ls[3], ls[4])

    except ValueError:
        print('Введены некорректные данные')
    else:
        break

print(time_out)
print(time_in)
print(f"Путь займёт {time_in - time_out}")