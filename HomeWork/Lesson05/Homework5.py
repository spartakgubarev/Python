# Урок 5. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension
# -------------------------------------
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# def read_file(path_doc):
#     with open(path_doc, 'r', encoding="utf-8") as d:
#         return d.read()


# def find_text(find, txt):
#     b = filter(lambda a: not find in a, txt.split())
#     return ' '.join(b)


# def save_text(path, txt):
#     with open(path, 'a', encoding="utf-8") as s:
#         s.write(txt)


# path = 'G:/Учеба/Разработчик/repo/Python/HomeWork/Lesson05/abv.txt'
# path_save = 'G:/Учеба/Разработчик/repo/Python/HomeWork/Lesson05/abv_new.txt'
# find_txt = 'абв'
# text = read_file(path)
# new_text = find_text(find_txt, text)
# save_text(path_save, new_text)


# -------------------------------------
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет
# нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
# import random


# def number_check():
#     while True:
#         num = input()
#         if num.isdigit():
#             num = int(num)
#             if num >= 1 and num <= 28:
#                 return num
#             else:
#                 print('Внимательнее, от 1 по 28')
#                 False
#         else:
#             print('Внимательнее, Вы ввели не число.')
#             False


# def mode_player():
#     list = []
#     num = int(input('Введите вариант игры: '))
#     player1 = input('Введите имя игрока: ')
#     if num == 1:
#         player2 = input('Введите имя второго игрока: ')
#     elif num == 2:
#         player2 = 'computer'
#     elif num == 3:
#         player2 = 'computer_expert'
#     rnd = random.randint(1, 2)
#     if rnd == 1:
#         list = [player1, player2, num]
#         return list
#     else:
#         list = [player2, player1, num]
#         return list


# def choice_move(mode):
#     if mode[2] == 1:
#         number = number_check()
#     elif mode[2] == 2:
#         if mode[0] != 'computer':
#             number = number_check()
#         else:
#             if count < 29:
#                 number = count
#             else:
#                 number = random.randint(1, 28)
#             print(number)
#     elif mode[2] == 3:
#         if mode[0] != 'computer_expert':
#             number = number_check()
#         else:
#             number = expert(count)
#             print(number)
#     return number


# def expert(count):
#     if 0 < count % 29 < 29:
#         _temp = count % 29
#         return _temp
#     _temp = random.randint(1, 28)
#     return _temp


# count = 2021

# print(
#     f'На столе лежит {count} конфет(а). Играют двое. Очередность определяется случайно.')
# print('За один ход можно взять от 1-28 конфет. Выиграл тот, кто сделал последний ход.')
# print('Как играем?\n1 - Человек-человек\n2 - Человек-компьютер\n3 - Человек-копьютер(профи)')

# mode = mode_player()

# while count > 0:
#     print(f'Осталось {count} конфет. Ходит {mode[0]}, сколько забираете: ')
#     number = choice_move(mode)
#     temp = mode[0]
#     mode[0] = mode[1]
#     mode[1] = temp
#     count -= number
# print(f'Выиграл {mode[1]}. Поздравляем!!!')

# -------------------------------------
# Создайте программу для игры в ""Крестики-нолики"".
# from tkinter import *


# def clicked(btn1, x, y):
#     global count
#     btn1["state"] = DISABLED
#     if count % 2 == 0:
#         btn1['text'] = 'X'
#     else:
#         btn1['text'] = 'O'
#     btn1["state"] = DISABLED
#     count += 1
#     a = btn1['text']
#     btn[x][y] = a

#     if btn[0][0] == a and btn[0][1] == a and btn[0][2] == a or (
#             btn[1][0] == a and btn[1][1] == a and btn[1][2] == a or
#             btn[2][0] == a and btn[2][1] == a and btn[2][2] == a or
#             btn[0][0] == a and btn[1][0] == a and btn[2][0] == a or
#             btn[0][1] == a and btn[1][1] == a and btn[2][1] == a or
#             btn[0][2] == a and btn[1][2] == a and btn[2][2] == a or
#             btn[0][0] == a and btn[1][1] == a and btn[2][2] == a or
#             btn[0][2] == a and btn[1][1] == a and btn[2][0] == a):
#         l1 = Label(text=f'Победили "{a}", УРААААА!!!!')
#         l1.grid(column=4, row=4)
#         for i in range(3):
#             for j in range(3):
#                 if btn[i][j] != 'X' and btn[i][j] != 'O':
#                     btn[i][j]['state'] = DISABLED


# btn = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# count = 0
# window = Tk()
# window.title('"крестики-нолики"')
# window.geometry('400x250')

# for i in range(3):
#     for j in range(3):
#         btn[i][j] = Button(window, text='', command=lambda x=i,
#                            y=j: clicked(btn[x][y], x, y), width=4)
#         btn[i][j].grid(column=j, row=i)
# window.mainloop()

# -------------------------------------
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
def compression(textzip, key):
    i = 0
    str_text = ''
    if key == 1:
        while i < len(textzip)-1:
            count = 1
            while i + 1 < len(textzip) and textzip[i] == textzip[i+1]:
                count += 1
                i += 1
            str_text += textzip[i] + str(count)
            i += 1
        return str_text + '\n'
    elif key == 2:
        while i + 1 < len(textzip)-1:
            str_text += textzip[i] * int(textzip[i+1])
            i += 2
        return str_text + '\n'


def open_files(path_files, key):
    text = ''
    with open(path_files, 'r', encoding='utf-8') as data:
        for line in data:
            text += compression(line, key)
    return text


# ********************* Сжатие
path = 'G:/Учеба/Разработчик/repo/Python/HomeWork/Lesson05/Text_homework_04.txt'
KEY = 1
text = open_files(path, KEY)
f = open('G:/Учеба/Разработчик/repo/Python/HomeWork/Lesson05/zip_new.txt', 'w', encoding='utf-8')
f.write(text)
f.close()

# ********************* Распаковка
path = 'G:/Учеба/Разработчик/repo/Python/HomeWork/Lesson05/zip_new.txt'
KEY = 2
text = open_files(path, KEY)
f = open('G:/Учеба/Разработчик/repo/Python/HomeWork/Lesson05/unpacking_new.txt', 'w', encoding='utf-8')
f.write(text)
f.close()