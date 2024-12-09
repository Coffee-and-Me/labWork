def get_val(dictr, n):
    for key, val in dictr.items():
        if val == n:
            return key


while 1:
    st = input('Последовательность через пробел: ')
    try:
        st = list(map(int, st.split()))
    except ValueError:
        print('error')
    else:
        break

st = sorted(st)

dictr = {}

for i in range(len(st)):
    dictr[st[i]] = st.count(st[i])

lst = []
for key, value in dictr.items():
    lst.append(value)

lst = sorted(lst)
if lst[-1] == lst[-2]:
    print('Моды не существует')
else:
    print(f'Мода последовательности {get_val(dictr, lst[-1])}')
