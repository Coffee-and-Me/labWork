ticket_min, ticket_max = 'a', 'b'
sum_tic = 0
while 1:
    ticket_min = input("Введите минимальный билет: ")
    if ticket_min.isdigit():
        if int(ticket_min) > 999_999:
            print("Билет не может быть больше 999999")
            continue
        if int(ticket_min) < 100_000:
            print("Билет не может быть меньше 100000")
            continue
        else:
            break
    else:
        continue

while 1:
    ticket_max = input("Введите максимальный билет: ")
    if ticket_max.isdigit():
        if int(ticket_max) < int(ticket_min):
            print("Максимальный билет не может быть меньше минимального")
            continue
        if int(ticket_max) > 999_999:
            print("Билет не может быть больше 999999")
            continue
        else:
            break
    else:
        continue

ticket_max = int(ticket_max)
ticket_min = int(ticket_min)


for n in range(ticket_min, ticket_max):
    st = str(n)
    if int(st[0]) + int(st[1]) + int(st[2]) == int(st[3]) + int(st[4]) + int(st[5]):
        sum_tic += 1

print(f'Счастливых билетов: {sum_tic}')
