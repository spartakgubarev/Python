# Знакомство с языком Python (семинары)
# Урок 4. Данные, функции и модули в Python. Продолжение
# ******
# 1. Вычислить число c заданной точностью d
# Пример: # при $d = 0.001, π = 3.141
def rounding(number, coefficient):
    print(f'{number} - {type(number)}')
    count = 0
    while coefficient % 1 != 0:
        count += 1
        coefficient *= 10
    increment = (number * 10 ** count // 1) * 10 ** -count
    return print(increment)


num = float(input('Введите дробное число: '))
d = float(input('С точностью до скольки знаков после запятой в вормате (0.001): '))
rounding(num, d)

# ******
# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

# ******
# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

# ******
# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# ******
# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
