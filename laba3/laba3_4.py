from datetime import datetime, timedelta

while 1:
    try:
        birthday = input("Введите дату рождения в формате YYYY.MM.DD: ")
        birthday = datetime.strptime(birthday, '%Y.%m.%d')
        break
    except ValueError:
        print('Введите корректные данные')

print(f'Через 10.000 дней будет {birthday + timedelta(days=10_000)}')
print(f'Через 1.000.000 минут будет {birthday + timedelta(minutes=1_000_000)}')
print(f'Через 1.000.000.000 секунд будет {birthday + timedelta(seconds=1_000_000_000)}')
