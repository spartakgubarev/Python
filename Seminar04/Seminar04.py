# ************
# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.
# def int_number_str(number):
#     list = []
#     for i in number:
#         list.append(int(i))
#     return list


# number_str = input('Введите числа разделяя пробелом: ').split()
# list = int_number_str(number_str)
# print(f'список {list} min = {min(list)}, max = {max(list)}')

# ************
# # 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
import math


def int_number_str(number):
    list = []
    for i in number:
        list.append(int(i))
    a = list[0]
    b = list[1]
    c = list[2]
    d = b ** 2 - 4 * a * c
    if d > 0:
        x_1 = (-b + d ** 0.5) / (2 * a)
        x_2 = (-b - d ** 0.5) / (2 * a)
        return print(x_1, x_2)
    else:
        return print('Решений нет.')


abc = input(
    'Введите значения квадратного уравнения через пробел, ax^2 + bx + c = 0: ').split()
int_number_str(abc)

# 2) с помощью дополнительных библиотек Python


def int_number_str(number):
    list = []
    for i in number:
        list.append(int(i))
    a = list[0]
    b = list[1]
    c = list[2]
    d = math.pow(b, 2) - 4 * a * c
    if d > 0:
        x_1 = (-b + math.sqrt(d)) / (2 * a)
        x_2 = (-b - math.sqrt(d)) / (2 * a)
        return print(x_1, x_2)
    else:
        return print('Решений нет.')


abc = input(
    'Введите значения квадратного уравнения через пробел, ax^2 + bx + c = 0: ').split()
int_number_str(abc)


# ************
# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# Ответ записать в файл.
