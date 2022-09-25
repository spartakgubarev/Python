#********************* 1. Напишите программу, удаляющую из текста все слова, содержание "абв".
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


#********************* 2. Создайте программу для игры с конфетами человек против человека.
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
        num = input('Сколько конфет заберете? ')
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

print('На столе лежит 2021 конфета. Играют двое. Очередность определяется случайно.')
print('За один ход можно взять от 1-28 конфет. Выиграл тот, кто сделал последний ход.')
rnd = random.randint(1, 2)
count = 2021
player1 = input('Введите имя первого игра: ')
player2 = input('Введите имя второго игра: ')
if rnd == 1:
    player = True 
else:
    player = False

while count > 0:
    number = int(number_check())
    print(number)
    
    count -= number
    print(count)


#********************* 3. Создайте программу для игры в "Крестики-нолики".


#********************* 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
