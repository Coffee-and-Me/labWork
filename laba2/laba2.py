num_one, num_two = 'a', 'b'

while 1:
    num_one = input("Введите 1-е число: ")
    if num_one.isdigit():
        break
    elif num_one[1::].isdigit():
        break

while 1:
    num_two = input("Введите 2-е число: ")
    if num_two.isdigit():
        break
    elif num_two[1::].isdigit():
        break

len_one = len(str(abs(int(num_one))))
len_two = len(str(abs(int(num_two))))

if len_one > len_two:
    print("Первое число длинее")
elif len_one < len_two:
    print("Второе число длинее первого")
elif len_one == len_two:
    print("Числа одинаковой длины")
