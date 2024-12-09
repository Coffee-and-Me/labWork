try:
    st1 = list(map(int, input('Первый набор чисел: ').split()))
    st2 = list(map(int, input('Второй набор чисел: ').split()))
except ValueError:
    print('error')
else:
    st1 = set(st1)
    st2 = set(st2)

    print(st1 & st2)
