# Знакомство с языком Python (семинары)
# Урок 2. Знакомство с Python. Продолжение
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 0,56 -> 11
# Вариант 1: для строки
# summ = 0
# number = input('Введите вещественное число через точку (пример: 6.543): ')
# print(number)
# for i in number:
#     if i.isdigit():
#         summ += int(i)
# print(summ)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# summ = 1
# n = int(input('Введите N, посчитаю факториал N!: '))
# print(f'N= {n}')
# if n > 1:
#     for i in range(1, n+1):
#         summ *= i
#         print(summ, end=' ')
# else:
#     print('1')

# Задайте список из k чисел последовательности (1 + 1/k)^k и выведите на экран их сумму.
# summ = 0
# k = int(input('Введите число к: '))
# for i in range(1, k+1):
#     summ += (1 + 1/i) ** i
#     print(f'{i} --> {summ}')

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.
# from random import randint
# summ = 1
# n = int(input('Введите количество элеменов N: '))
# arr = [randint(-n, n) for i in range(-n, n+1)]
# print(arr)
# search = input(
#     f'Введите через пробел позицию в диапозоне [{0}, {n+n}], например [2 {n-4}] ')
# str_list = search.split(sep=' ')
# for i in range(int(str_list[0]), int(str_list[1])+1):
#     summ *= arr[i]
# print(f'Произведение элементов в диапозоне [{str_list}] равно {summ}')

# Реализуйте алгоритм перемешивания списка.
from random import randint

number_digits = 50
n = int(input('Введите количество массива N:'))
arr = [randint(0, 50) for i in range(n)]
arr_new = list()
print(arr)
_arr = arr
for i in range(n):
    rnd = randint(0, n-1-i)
    arr_new.append(_arr[rnd])
    _arr.pop(rnd)
arr = arr_new
print(arr)
