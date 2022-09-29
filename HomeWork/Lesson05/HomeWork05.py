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
from tkinter import *


def examination():
    if btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X' or (
        btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O' or
        btn4['text'] == 'X' and btn5['text'] == 'X' and btn6['text'] == 'X' or
        btn4['text'] == 'O' and btn5['text'] == 'O' and btn6['text'] == 'O' or
        btn7['text'] == 'X' and btn8['text'] == 'X' and btn9['text'] == 'X' or
        btn7['text'] == 'O' and btn8['text'] == 'O' and btn9['text'] == 'O' or
        btn1['text'] == 'X' and btn4['text'] == 'X' and btn7['text'] == 'X' or
        btn1['text'] == 'O' and btn4['text'] == 'O' and btn7['text'] == 'O' or
        btn2['text'] == 'X' and btn5['text'] == 'X' and btn8['text'] == 'X' or
        btn2['text'] == 'O' and btn5['text'] == 'O' and btn8['text'] == 'O' or
        btn3['text'] == 'X' and btn6['text'] == 'X' and btn9['text'] == 'X' or
        btn3['text'] == 'O' and btn6['text'] == 'O' and btn9['text'] == 'O' or
        btn1['text'] == 'X' and btn5['text'] == 'X' and btn9['text'] == 'X' or
        btn1['text'] == 'O' and btn5['text'] == 'O' and btn9['text'] == 'O' or
        btn3['text'] == 'X' and btn5['text'] == 'X' and btn7['text'] == 'X' or
        btn3['text'] == 'O' and btn5['text'] == 'O' and btn7['text'] == 'O'
        ):
        print('Победа')



def clicked(btn):  
    global count

    if count % 2 ==0:
        btn['text'] = 'X'
    else:
        btn['text'] = 'O'
    btn["state"] = DISABLED
    examination()
    count += 1
    

count = 0

window = Tk()
window.title('"крестики-нолики"')
window.geometry('400x250')

btn1 = Button(window, text='',command=lambda: clicked(btn1), width=4)
btn1.grid(column=0, row=0)

btn2 = Button(window, text='',command=lambda: clicked(btn2), width=4)
btn2.grid(column=0, row=1)

btn3 = Button(window, text='',command=lambda: clicked(btn3), width=4)
btn3.grid(column=0, row=2)

btn4 = Button(window, text='',command=lambda: clicked(btn4), width=4)
btn4.grid(column=1, row=0)

btn5 = Button(window, text='',command=lambda: clicked(btn5), width=4)
btn5.grid(column=1, row=1)

btn6 = Button(window, text='',command=lambda: clicked(btn6), width=4)
btn6.grid(column=1, row=2)

btn7 = Button(window, text='',command=lambda: clicked(btn7), width=4)
btn7.grid(column=2, row=0)

btn8 = Button(window, text='',command=lambda: clicked(btn8), width=4)
btn8.grid(column=2, row=1)

btn9 = Button(window, text='',command=lambda: clicked(btn9), width=4)
btn9.grid(column=2, row=2)

window.mainloop()

# from tkinter import *

# tkWindow = Tk()  
# tkWindow.geometry('400x150')  
# tkWindow.title('PythonExamples.org - Tkinter Example')

# def toggleText(button1):  
# 	if(button1['text']=='Submit'):
# 		button1['text']='Submitted'
# 	else:
# 		button1['text']='Submit'

# button = Button(tkWindow,
# 	text = 'Submit',
# 	command = lambda: toggleText(button))  
# button.pack()  
# button1 = Button(tkWindow,
# 	text = 'Submit',
# 	command = lambda: toggleText(button1))  
# button1.pack()  
# tkWindow.mainloop()


# from tkinter import *

# tkWindow = Tk()  
# tkWindow.geometry('400x150')  
# tkWindow.title('PythonExamples.org - Tkinter Example')

# def changeText():  
#     button['text'] = 'Submitted'

# button = Button(tkWindow,
# 	text = 'Submit',
# 	command = changeText)  
# button.pack()  
  
# tkWindow.mainloop()


# from tkinter import *
# import tkinter
# import tkinter.messagebox

# root = Tk()


# def fun(arg):
#     if arg == 1:
#         tkinter.messagebox.showinfo("button 1", "button 1 used")
#     elif arg == 2:
#         tkinter.messagebox.showinfo("button 2", "button 2 used")
#     elif arg == 3:
#         tkinter.messagebox.showinfo("button 3", "button 3 used")
#     elif arg == 4:
#         tkinter.messagebox.showinfo("button 4", "button 4 used")


# b1 = Button(root, text="Quit1", command=lambda: fun(1))
# b1.pack()
# b2 = Button(root, text="Quit2", command=lambda: fun(2))
# b2.pack()
# b3 = Button(root, text="Quit3", command=lambda: fun(3))
# b3.pack()
# b4 = Button(root, text="Quit4", command=lambda: fun(4))
# b4.pack()

# root.mainloop()


# ********************* 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
