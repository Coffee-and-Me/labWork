def check(n):
    return n.isdigit()


num1 = 'a'
num2 = 'b'
flag = True

while not (check(num1)):
    num1 = input('1 число: ')

num1 = int(num1)

while not (check(num2)):
    num2 = input('2 число: ')

num2 = int(num2)

while (flag):
    variant = input("Введите способ (1,2) перестановки: ")

    if (variant == '1'):
        print(f"a={num1}, b={num2}")
        buf = num1
        num1 = num2
        num2 = buf
        print(f"a={num1}, b={num2}")
        break
    elif (variant == '2'):
        print(f"a={num1}, b={num2}")
        num1 += num2
        num2 -= num1
        num1 += num2
        num2 = -num2
        print(f"a={num1}, b={num2}")
        break
    else:
        continue
