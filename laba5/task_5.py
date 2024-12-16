import random


def computer_move(stones_left):
    return random.randint(1, min(3, stones_left))


print("Добро пожаловать в игру 'Камни'!")
stones = random.randint(4, 30)
print(f"На столе {stones} камней.")

# Случайно выбираем, кто ходит первым
user_turn = random.choice([True, False])
print("Первым ходит", "пользователь" if user_turn else "компьютер")
while stones > 0:
    if user_turn:
        # Ход пользователя
        while True:
            try:
                user_choice = int(input(f"Ваш ход. Возьмите от 1 до 3 камней (осталось {stones}): "))
                if 1 <= user_choice <= 3 and user_choice <= stones:
                    break
                else:
                    print("Некорректный ввод. Попробуйте снова.")
            except ValueError:
                print("Пожалуйста, введите число от 1 до 3.")

        stones -= user_choice
        print(f"Вы взяли {user_choice} камней. Осталось {stones}.")

        if stones == 0:
            print("Поздравляем! Вы выиграли! Компьютер остался с последним камнем.")
            break

    else:
        # Ход компьютера
        computer_choice = computer_move(stones)
        stones -= computer_choice
        print(f"Компьютер взял {computer_choice} камней. Осталось {stones}.")

        if stones == 0:
            print("Компьютер выиграл! Вы остались с последним камнем.")
            break

    # Смена хода
    user_turn = not user_turn
