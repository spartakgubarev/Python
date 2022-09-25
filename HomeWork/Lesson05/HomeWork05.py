# ********************* 1. Напишите программу, удаляющую из текста все слова, содержание "абв".
# def open_files(path_file):
#     with open(path_file, 'r') as data:
#         data = data.read()
#     return data

# def find_numbers(str_txt, find_txt):
#     list = filter(lambda x: not find_txt in x, str_txt.split())
#     return ' '.join(list)

# path = 'G:/Учеба/Разработчик/repo/Python/HomeWork/Lesson05/Text_HomeWork01.txt'
# data = open_files(path)
# find_text = 'абв'

# list = find_numbers(data, find_text)
# print(f'{data} => {list}')


# ********************* 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#     а) Добавьте игру против бота
#     б) подумайте как наделить бота "интеллектом"
import random


def number_check():
    while True:
        num = input()
        if num.isdigit():
            num = int(num)
            if num >= 1 and num <= 28:
                return num
            else:
                print('Внимательнее, от 1 по 28')
                False
        else:
            print('Внимательнее, Вы ввели не число.')
            False


def mode_player():
    list = []
    num = int(input('Введите вариант игры: '))
    player1 = input('Введите имя игрока: ')
    if num == 1:
        player2 = input('Введите имя второго игрока: ')
    elif num == 2:
        player2 = 'computer'
    elif num == 3:
        player2 = 'computer_expert'
    rnd = random.randint(1, 2)
    if rnd == 1:
        list = [player1, player2, num]
        return list
    else:
        list = [player2, player1, num]
        return list


def choice_move(mode):
    if mode[2] == 1:
        number = number_check()
    elif mode[2] == 2:
        if mode[0] != 'computer':
            number = number_check()
        else:
            if count < 29:
                number = count
            else:
                number = random.randint(1, 28)
            print(number)
    elif mode[2] == 3:
        if mode[0] != 'computer_expert':
            number = number_check()
        else:
            number = expert(count)
            print(number)
    return number


def expert(count):
    if 0 < (count % 29) < 29:
        _temp = count % 29
        return _temp
    _temp = random.randint(1, 28)
    return _temp


count = 2021

print(
    f'На столе лежит {count} конфет(а). Играют двое. Очередность определяется случайно.')
print('За один ход можно взять от 1-28 конфет. Выиграл тот, кто сделал последний ход.')
print('Как играем?\n1 - Человек-человек\n2 - Человек-компьютер\n3 - Человек-копьютер(профи)')

mode = mode_player()

while count > 0:
    print(f'Осталось {count} конфет. Ходит {mode[0]}, сколько забираете: ')
    number = choice_move(mode)
    temp = mode[0]
    mode[0] = mode[1]
    mode[1] = temp
    count -= number
print(f'Выиграл {mode[1]}. Поздравляем!!!')


# ********************* 3. Создайте программу для игры в "Крестики-нолики".


# ********************* 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
