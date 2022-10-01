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
#     if 0 < (count % 29) < 29:
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


# ********************* 3. Создайте программу для игры в "Крестики-нолики".
# from tkinter import *


# def examination():
#     if btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X' or (
#         btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O' or
#         btn4['text'] == 'X' and btn5['text'] == 'X' and btn6['text'] == 'X' or
#         btn4['text'] == 'O' and btn5['text'] == 'O' and btn6['text'] == 'O' or
#         btn7['text'] == 'X' and btn8['text'] == 'X' and btn9['text'] == 'X' or
#         btn7['text'] == 'O' and btn8['text'] == 'O' and btn9['text'] == 'O' or
#         btn1['text'] == 'X' and btn4['text'] == 'X' and btn7['text'] == 'X' or
#         btn1['text'] == 'O' and btn4['text'] == 'O' and btn7['text'] == 'O' or
#         btn2['text'] == 'X' and btn5['text'] == 'X' and btn8['text'] == 'X' or
#         btn2['text'] == 'O' and btn5['text'] == 'O' and btn8['text'] == 'O' or
#         btn3['text'] == 'X' and btn6['text'] == 'X' and btn9['text'] == 'X' or
#         btn3['text'] == 'O' and btn6['text'] == 'O' and btn9['text'] == 'O' or
#         btn1['text'] == 'X' and btn5['text'] == 'X' and btn9['text'] == 'X' or
#         btn1['text'] == 'O' and btn5['text'] == 'O' and btn9['text'] == 'O' or
#         btn3['text'] == 'X' and btn5['text'] == 'X' and btn7['text'] == 'X' or
#         btn3['text'] == 'O' and btn5['text'] == 'O' and btn7['text'] == 'O'
#         ):
#         print('Победа')



# def clicked(btn):  
#     global count

#     if count % 2 ==0:
#         btn['text'] = 'X'
#     else:
#         btn['text'] = 'O'
#     btn["state"] = DISABLED
#     examination()
#     count += 1
    

# count = 0

# window = Tk()
# window.title('"крестики-нолики"')
# window.geometry('400x250')

# btn1 = Button(window, text='',command=lambda: clicked(btn1), width=4)
# btn1.grid(column=0, row=0)

# btn2 = Button(window, text='',command=lambda: clicked(btn2), width=4)
# btn2.grid(column=0, row=1)

# btn3 = Button(window, text='',command=lambda: clicked(btn3), width=4)
# btn3.grid(column=0, row=2)

# btn4 = Button(window, text='',command=lambda: clicked(btn4), width=4)
# btn4.grid(column=1, row=0)

# btn5 = Button(window, text='',command=lambda: clicked(btn5), width=4)
# btn5.grid(column=1, row=1)

# btn6 = Button(window, text='',command=lambda: clicked(btn6), width=4)
# btn6.grid(column=1, row=2)

# btn7 = Button(window, text='',command=lambda: clicked(btn7), width=4)
# btn7.grid(column=2, row=0)

# btn8 = Button(window, text='',command=lambda: clicked(btn8), width=4)
# btn8.grid(column=2, row=1)

# btn9 = Button(window, text='',command=lambda: clicked(btn9), width=4)
# btn9.grid(column=2, row=2)

# window.mainloop()





from tkinter import *


# def examination():
#     if btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X' or (
#         btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O' or
#         btn4['text'] == 'X' and btn5['text'] == 'X' and btn6['text'] == 'X' or
#         btn4['text'] == 'O' and btn5['text'] == 'O' and btn6['text'] == 'O' or
#         btn7['text'] == 'X' and btn8['text'] == 'X' and btn9['text'] == 'X' or
#         btn7['text'] == 'O' and btn8['text'] == 'O' and btn9['text'] == 'O' or
#         btn1['text'] == 'X' and btn4['text'] == 'X' and btn7['text'] == 'X' or
#         btn1['text'] == 'O' and btn4['text'] == 'O' and btn7['text'] == 'O' or
#         btn2['text'] == 'X' and btn5['text'] == 'X' and btn8['text'] == 'X' or
#         btn2['text'] == 'O' and btn5['text'] == 'O' and btn8['text'] == 'O' or
#         btn3['text'] == 'X' and btn6['text'] == 'X' and btn9['text'] == 'X' or
#         btn3['text'] == 'O' and btn6['text'] == 'O' and btn9['text'] == 'O' or
#         btn1['text'] == 'X' and btn5['text'] == 'X' and btn9['text'] == 'X' or
#         btn1['text'] == 'O' and btn5['text'] == 'O' and btn9['text'] == 'O' or
#         btn3['text'] == 'X' and btn5['text'] == 'X' and btn7['text'] == 'X' or
#         btn3['text'] == 'O' and btn5['text'] == 'O' and btn7['text'] == 'O'
#         ):
#         print('Побед/а')



def clicked(btn1, x, y):  
    global count
    print(btn1, x, y)
    
    if count % 2 ==0:
        btn1['text'] = 'X'
    else:
        btn1['text'] = 'O'
    btn1["state"] = DISABLED
    # examination()
    btn1.grid(column=x, row=y)
    count += 1

count = 0
btn = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
# x = [0, 1, 2]
# y = [0, 1, 2]

window = Tk()
window.title('"крестики-нолики"')
window.geometry('400x250')


for i in range(3):
    for j in range(3):
        btn[i][j] = Button(window, text='', command=lambda x=i, y=j: clicked(btn[x][y], x, y), width=4)
        btn[i][j].grid(column=i, row=j)
        print(btn[i][j])
# btn = Button(window, text='', command=lambda x=i, y=j: clicked(btn, x, y), width=4)
# btn.grid(column=x, row=y)

        # btn = Button(window, text='', command=lambda x=i, y=j: clicked(btn, x, y), width=4)

# Button(window, text='', command=lambda: clicked(), width=4)

# btn = Button(window, text='', command=lambda: clicked(btn), width=4)
# print(btn)
# btn1.grid(column=0, row=0)


# btn1.grid(column=0, row=1)
# btn1.grid(column=0, row=2)
# btn1.grid(column=1, row=0)

# btn = Button(window, text='',command=lambda: clicked(btn), width=4)
# btn1 = Button(window, text='',command=lambda: clicked(btn1), width=4)
# btn1.grid(column=0, row=0)

# btn2 = Button(window, text='',command=lambda: clicked(btn2), width=4)
# btn2.grid(column=0, row=1)

# btn3 = Button(window, text='',command=lambda: clicked(btn3), width=4)
# btn3.grid(column=0, row=2)

# btn4 = Button(window, text='',command=lambda: clicked(btn4), width=4)
# btn4.grid(column=1, row=0)

# btn5 = Button(window, text='',command=lambda: clicked(btn5), width=4)
# btn5.grid(column=1, row=1)

# btn6 = Button(window, text='',command=lambda: clicked(btn6), width=4)
# btn6.grid(column=1, row=2)

# btn7 = Button(window, text='',command=lambda: clicked(btn7), width=4)
# btn7.grid(column=2, row=0)

# btn8 = Button(window, text='',command=lambda: clicked(btn8), width=4)
# btn8.grid(column=2, row=1)

# btn9 = Button(window, text='',command=lambda: clicked(btn9), width=4)
# btn9.grid(column=2, row=2)

window.mainloop()



# ********************* 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
