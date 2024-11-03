oklad = input()
while not (oklad.isdigit()):
    oklad = input('Введите оклад: ')

premia = int(oklad) * (2 / 3)
stonks = int(oklad) * 0.87

print(f"Премия составила: {premia}")
print(f"Доход с учётом налогового вычета: {stonks}")
