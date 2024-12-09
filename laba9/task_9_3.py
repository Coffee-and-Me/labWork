dictr = {
    'я': 'I',
    'могу': 'can',
    'играть': 'play',
    'футбол': 'football'
}

lst = input('Строка: ').lower().split()

for i in range(len(lst)):
    if lst[i] in dictr.keys():
        lst[i] = dictr[lst[i]]

res = ' '.join(lst)

print(res)