# переменные
# встроенные функции: print(), int(), str()
# условия
# списки
# for, range(), Len()
# while


# встроенные функции
# my_age = int(input('Введите возраст: '))
# print(f"Вам {my_age} лет")

# if условия
# Задача: 1. Напишите программу, которая принимает на вход два числа и проверяет,
# является ли одно число квадратом другого.
# Пример
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 - > нет
# - 8, 9 -> нет
# one_number = int(input('Введите первое число: '))
# two_number = int(input('Введите второе число: '))
# if one_number * one_number == two_number:
#     print(f"{one_number} является квадратом {two_number}")
# elif two_number ** 2 == one_number:
#     print(f"{two_number} является квадратом {one_number}")
# else:
#     print(f"{one_number} не является квадратом {two_number}")

# Списки
# my_list = [8, 'r', 7, True]     # можно объявить и пустой []
# print(my_list[2])
# print(my_list[-1])              # знак минус говорит об обратном отсчете
# my_list.append('END!')          # .append добавляет элемент в конец списка
# print(my_list)
# my_list[1] = 'Hello, World!'
# print(my_list)
# my_list.pop(1)                  # удаляет первый элемент
# print(my_list)


# for, range(), Len()
# print(len(my_list))             # len возвращает длину
# range (5)                     # [0, 1, 2, 3, 4]
# range (1, 11)                 # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# range (1, 10, 2)              # [1, 3, 5, 7, 9]
# for i in 1, 2, 3, 4:
#     print(i, end=' ')

# print()
# for i in range(1, 10, 2):
#     print(i, end=' ')

# my_list = [8, 'r', 7, True]
# for i in range(len(my_list)):
#     print(my_list[i])

# Задачи:
# 1. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Пример:
# 1, 2, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90

# number = 5
# list = []
# for i in range(number):
#     list.append(int(input(f"Введите число {i+1}: ")))
# max = list[0]
# for i in range(1, number):
#     if max < list[i]:
#         max = list[i]
# print(f"{list} -> максимальное число: {max}")

# 2. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# Пример:
# 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# number = int(input('Введите положительное число: '))
# for i in range(-number, number+1):
#     print(i, end=' ')

# 3. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# Пример:
# 6,78 -> 7
# 5 -> нет
# 0,34 -> 3

# number = float(input('Введите дробное число через точку: '))
# number = number / 0.1
# number_end = int(number % 10)
# print(number_end)

# 4. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно (5 и 10) или (15, но не 30)
# number = int(
#     input('Введите число, проверю на кратность (5 и 10) или (15, но не 30) - '))
# if ((number % 5 == 0) and (number % 10 == 0)) or ((number % 15 == 0) and (number % 30 != 0)):
#     print(f"кратно")
# else:
#     print('не кратно')
