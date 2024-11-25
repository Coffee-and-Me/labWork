num = 'a'
res = 1
while 1:
    num = input("Введите число: ")
    if num.isdigit():
        break

for fact in range(1, int(num) + 1):
    res*=fact

print(res)