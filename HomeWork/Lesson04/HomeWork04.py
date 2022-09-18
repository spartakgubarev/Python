# Знакомство с языком Python (семинары)
# Урок 4. Данные, функции и модули в Python. Продолжение
# ******
# 1. Вычислить число c заданной точностью d
# Пример: # при $d = 0.001, π = 3.141
# def rounding(number, coefficient):
#     print(f'{number} - {type(number)}')
#     count = 0
#     while coefficient % 1 != 0:
#         count += 1
#         coefficient *= 10
#     increment = (number * 10 ** count // 1) * 10 ** -count
#     return print(increment)


# num = float(input('Введите дробное число: '))
# d = float(input('С точностью до скольки знаков после запятой в вормате (0.001): '))
# rounding(num, d)

# ******
# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]
# def prime_factors(n):
#     list = []
#     for i in range(2, n+1):
#         while n % i == 0:
#             n = n / i
#             list.append(i)
#     return list


# number = int(input('Введите число, составлю простые множители числа: '))
# list = prime_factors(number)
# print(list)

# ******
# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]
# def search_repetitions(old_list):
#     _list = []
#     for i in range(len(old_list)):
#         if (old_list[i] not in old_list[i+1:]) and (old_list[i] not in old_list[:i]):
#             _list.append(old_list[i])
#     return _list


# new_list = [8, 7, 6, 1, 2, 4, 1, 5, 6, 7, 9, 8, 1, 3, 4]
# list = search_repetitions(new_list)
# print(f'{new_list} -> {list}')


# ******
# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def degree_polynomial(count, rnd_min, rnd_max):
    k = count
    func = 'k = ' + str(count) + ' --> '
    k_str = ''
    while count != 0:
        rnd = (random.randint(rnd_min, rnd_max))
        k_str = str(count)
        func += str(rnd) + '*' + 'x^' + k_str + ' + '
        if count == 1:
            rnd = (random.randint(rnd_min, rnd_max))
            func += str(rnd) + ' = 0'
        count -= 1
    return func


rnd_min1 = 0
rnd_max2 = 100
count1 = int(input('Введите натуральную степень числа к= '))
formula = degree_polynomial(count1, rnd_min1, rnd_max2)
print(f'{formula}')

path = 'G:/Учеба/Разработчик/repo/Python/HomeWork/Lesson04/degree_polynomial.txt'
with open(path, 'a') as data:
    data.write(formula + '\n')
    data.close()


# ******
# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
