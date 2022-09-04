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
my_list = [8, 'r', 7, True]     # можно объявить и пустой []
print(my_list[2])
print(my_list[-1])              # знак минус говорит об обратном отсчете
my_list.append('END!')          # .append добавляет элемент в конец списка
print(my_list)
my_list[1] = 'Hello, World!'
print(my_list)
my_list.pop(1)                  # удаляет первый элемент
print(my_list)
