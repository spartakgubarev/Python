# Знакомство с языком Python (семинары)
# Урок 3. Данные, функции и модули в Python
# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример: # - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# def sum_odd_numbers(arr):
#     summ = 0
#     for i in range(1, len(arr), 2):
#         summ += arr[i]
#     return summ
# list1 = [2, 3, 5, 9, 3, 12, 17, 3, 2]
# print(sum_odd_numbers(list1))

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый
# и последний элемент, второй и предпоследний и т.д.
# Пример: # - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
# def multiplication(arr):
#     list_result = []
#     parity_check = len(arr)
#     if parity_check % 2 == 1:
#         parity_check = parity_check // 2 + 1
#     else:
#         parity_check //= 2
#     for i in range(parity_check):
#         list_result.append(arr[i] * arr[-i-1])
#     return list_result
# list = [1, 2, 3, 4, 5, 6, 7]
# print(list)
# print(multiplication(list))

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# Пример: # - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# def difference_real_numbers(list):
#     list1 = []
#     for i in range(len(list)):
#         list1.append(round(list[i] % 1, len(str(list[i]))-2))
#     min_list1 = list1[0]
#     max_list1 = list1[0]
#     for e in range(1, len(list1)):
#         if list1[e] < min_list1:
#             min_list1 = list1[e]
#         if list1[e] > max_list1:
#             max_list1 = list1[e]
#     if len(str(max_list1)) > len(str(min_list1)):
#         number_characters = len(str(max_list1))
#     else:
#         number_characters = len(str(min_list1))
#     return (f'{list} => {max_list1 - min_list1}')

# arr = [1.1, 1.211, 3.1, 10.01, 0.0001]
# print(difference_real_numbers(arr))

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: # - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
def binary_system(binary, result):
    if binary > 0:
        result = result + str(binary % 2)
        return binary_system(binary // 2, result)
    else:
        return result


number = int(input('Введите десятичное число, переведу в двоичное: '))
result = ''
a = (binary_system(number, result))
print(a)
print(a[::-1])


# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: # - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи]
