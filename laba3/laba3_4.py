from datetime import datetime, timedelta

while 1:
    try:
        birthday = input("Введите дату рождения в формате YYYY.MM.DD: ").split('.')
        dateday = datetime(int(birthday[0]), int(birthday[1]), int(birthday[2]))
        break
    except ValueError:
        print('Введите корректные данные')

print(f'Через 10000 дней будет {dateday + timedelta(days=10_000)}')
print(f'Через 1000000 минут будет {dateday + timedelta(minutes=100_000)}')
print(f'Через 1000000000 секунд будет {dateday + timedelta(seconds=1_000_000_000)}')
