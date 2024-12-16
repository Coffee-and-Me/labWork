import os
import random

res = []


def read_phr(file: str = 'Phrases.txt'):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

        for line in lines:
            res.append(line.strip().split('; '))


def generate_phr(phrs: list, count: int):
    sentences = []
    for i in range(count):
        sentences.append(
            random.choice(phrs[0]) + ' ' +
            random.choice(phrs[1]) + ' ' +
            random.choice(phrs[2]) + ' ' +
            random.choice(phrs[3]) + '. '
        )

    return sentences


while True:
    try:
        num = int(input("Сколько предложений вы хотите сгенерировать? "))
    except ValueError:
        print("Введите число.")

    else:
        if os.path.exists('Phrases.txt'):
            read_phr()
            buf = '\n'.join(generate_phr(res, num))

            with open('Result.txt', 'w', encoding='utf-8') as f:
                f.write(buf)

            print('Всё выполнялось корректно')
            break
        else:
            print('Phrases.txt не существует')
            exit()

while True:
    buff = input('Хотите продолжить? [y|n] ').lower()
    if buff == 'y':
        while True:
            try:
                num = int(input("Сколько предложений вы хотите сгенерировать? "))
            except ValueError:
                print("Введите число.")
            else:
                break

        buf = '\n'.join(generate_phr(res, num))

        with open('Result.txt', 'a', encoding='utf-8') as f:
            f.write('\n\n')
            f.write(buf)

            print('Всё выполнялось корректно')
    elif buff == 'n':
        break
