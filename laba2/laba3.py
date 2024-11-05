sum_u = 'a'
while 1:
    sum_u = input("Введите сумму: ")
    if sum_u.isdigit():
        sum_u = int(sum_u)
        if sum_u > 27:
            print("Сумма цифр трёхзначного числа не может быть больше 27")
            continue
        else:
            break
    else:
        continue

for num in range(100, 1000):
    if int(str(num)[0]) + int(str(num)[1]) + int(str(num)[2]) == sum_u:
        print(num)
