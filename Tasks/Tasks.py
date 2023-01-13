# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# import random
#
# num = random.uniform(10**(-1), 10**(-10))
# print(f'Дано число {num}, с какой точностью вывести число после запятой (0.0001): ')
# d = input()
# val = len(d)
# val1 = float((str(num))[:val])
# print(val1)


# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# ls = []
# n = int(input('Задайте натуральное число N, программа разложит его на простые множители: '))
# val = 2
# while n >= val:
#     if n % val == 0:
#         ls.append(val)
#         n /= val
#     else:
#         val += 1
# print(ls)


# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# import random
#
# amount = 20
# ls = list(map(lambda x: random.randint(0, amount), range(amount)))
# print('ls', ls)
# ls1 = list(filter(lambda x: ls.count(x) == 1, ls))
# print('ls1', ls1)


# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# import random
#
#
# def save_txt(text_val):
#     PATH = 'C:/Users/Юра/PycharmProjects/pythonProject/degree_polynomial_1.txt'
#     with open(PATH, 'a') as fil:
#         fil.writelines(text_val + '\n')
#
#
# k = int(input('Задайте натуральную степень к: '))
# val = f' - k={k} => '
# while k >= 0:
#     rnd = random.randint(0, 100)
#     if rnd == 0:
#         val += ''
#     elif k == 1:
#         val += f'{rnd}*x + '
#     elif k == 0:
#         val += f'{rnd}'
#     else:
#         val += f'{rnd}*x^{k} + '
#     k -= 1
# val += ' = 0'
# print(val)
# save_txt(val)


# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# def file_read(path_path):
#     with open(path_path, 'r') as file:
#         return file.readlines()
#
# def file_save(path):
#     pass
#
# def sum_polynomial(ls1, ls2):
#     pass
#
#
#
# PATH = 'C:/Users/Юра/PycharmProjects/pythonProject/degree_polynomial.txt' # чтение
# PATH1 = 'C:/Users/Юра/PycharmProjects/pythonProject/degree_polynomial_1.txt' # чтение
# PATH2 = 'C:/Users/Юра/PycharmProjects/pythonProject/degree_polynomial_2.txt' # сохранение
# txt_ls = file_read(PATH)
# txt_ls1 = file_read(PATH1)
#
# # срезы лишнего
# txt_ls = list(map(lambda x: x[x.find('=> ') + 3:x.find(' = 0')], txt_ls))
# txt_ls1 = list(map(lambda x: x[x.find('=> ') + 3:x.find(' = 0')], txt_ls1))
#
# print(txt_ls)
# print(txt_ls1)
#
# lsls =txt_ls[0].split(' + ')
# lsls1 =txt_ls1[0].split(' + ')
# if len(lsls) > len(lsls1):
#     pass
# else:
#     pass
#
# print(lsls)
# print(lsls1)
#
# ls = list(map(lambda x: x[:x.find('*')], lsls))
# ls1 = list(map(lambda x: x[:x.find('*')], lsls1))
# print(ls)
# print(ls1)


# --------------------------------- задачки
# Простейшие арифметические операции (1)
# Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть произведена
# над ними. Если третий аргумент +, сложить их; если —, то вычесть;
# * — умножить; / — разделить (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".
# def arithmetic(num1, num2, val):
#     if val == '*':
#         sum = num1 * num2
#     elif val == '/':
#         sum = num1 / num2
#     elif val == '+':
#         sum = num1 + num2
#     elif val == '-':
#         sum = num1 - num2
#     else:
#         sum = 'Неизвестная операция.'
#     return sum
#
#
# print('Простой калькулятор, умеет *, /, +, -.')
# a = int(input('Введите а: '))
# b = int(input('Введите b: '))
# c = input('Ввевдите действие *, /, +, -: ')
#
# print(arithmetic(a, b, c))


# Високосный год (2)
# Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный,
# и False иначе.
# def is_year_leap(year):
#     return (year % 4 == 0) and not (year % 100 == 0) or (year % 400 == 0)
#
#
# a = int(input('Введите год: '))
# print(f'{a} - {is_year_leap(a)}')


# Квадрат (3)
# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
# (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
# def square(a):
#     return (4 * a, a * a, (a ** 2 + a ** 2) ** 0.5)
#
#
# xxx = int(input('Введите сторону квадрата: '))
# val = square(xxx)
# print(f'сторона квадрата - {xxx}\nпериметр - {val[0]}\nПлощадь - {val[1]}\nдиагональ - {val[2]}')
# print('сторона квадрата - {0}\nпериметр - {1}\nПлощадь - {2}\nдиагональ - {3}'.format(xxx, val[0], val[1], val[2]))


# Времена года (4)
# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года,
# которому этот месяц принадлежит (зима, весна, лето или осень).
# def season(num_month):
#     if num_month <= 2 or num_month == 12:
#         return 'зима'
#     elif 2 < num_month <= 5:
#         return 'весна'
#     elif 5 < num_month <= 8:
#         return 'лето'
#     elif 8 < num_month <= 11:
#         return 'осень'
#
#
# val = int(input('Введите номер месяца: '))
# a = season(val)
# print(f'{val} месяц это - {a}')


# Банковский вклад (5)
# Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых (каждый год размер его вклада
# увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
# Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.
# def bank(a, year):
#     for i in range(year):
#         a += a * INTEREST_RATE
#         print(f'{i + 1} год сумму равна - {a}')
#     return a
#
#
# contribution = int(input('Введите размер вклада в рублях: '))
# YEAR = int(input('Введите срок вклада в годах: '))
# INTEREST_RATE = 0.1
# print(f'Ваш вклад по истечению {YEAR} лет будет равен - {bank(contribution, YEAR)}')


# Простые числа (6)
# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True,
# если оно простое, и False - иначе.
# def is_prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
#
#
# print(is_prime(int(input('Введите число от 0 до 1000, узнаю является ли простым: '))))


# Правильная дата (7)
# Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True,
# если такая дата есть в нашем календаре, и False иначе.
# def date(day, month, year):
#     if day < 1 or day > 31 or month < 1 or month > 12:
#         return False
#     else:
#         if month == 2 and day == 29:
#             return (year % 4 == 0) and not (year % 100 == 0) or (year % 400 == 0)
#         if (month == 2 and day > 29) or day == 31 and (month == 4 or month == 6 or month == 9 or month == 11):
#             return False
#         return True
#
#
# a = int(input('Введите день: '))
# b = int(input('Введите месяц: '))
# c = int(input('Введите год: '))
# print(date(a, b, c))
# # aaa = ('январь(31)', 'февраль(28,29)', 'март(31)', 'апрель(30)',
# #        'май(31)', 'июнь(30)', 'июль(31)', 'август(31)', 'сентябрь(30)', 'октябрь(31)', 'ноябрь(30)', 'декабрь(31)')
# # q = 0
# #
# # a = 31
# # c = 2023
# # for i in range(1, 13):
# #     print(i, aaa[q], date(a, i, c))
# #     q += 1
# # print("29/02/2024", date(29, 2, 2024))


# Оценщик малярных работ. Малярная компания установила, что на каждые 10 квадратных метров поверхности стены требуется
# 5 литров карски и 8 часов работы. Компания взимает за работу 2000 руб. в час. Напишите програму, которая просит пользователя
# ввести площадь поверхности окрашиваемой стены и цену 5-литровой емкости краски. Программа должна показать следующие данные:
# - количыество требуемых емкостей краски;
# - количество затраченных рабочих часов;
# - стоимость краски;
# - стоимость работы;
# - общая стоимость малярных работ.
# def main():
#     def sum_result(a, b):
#         num_dye = a / 10
#         hour = num_dye * 8
#         price_dye = num_dye * b
#         cost_work = hour / 8 * 2000
#         sum = cost_work + num_dye * b
#
#         print(f'количество требуемых емкостей краски - {num_dye}\nколичество затраченных рабочих часов - {hour}\
#         \nстоимость краски - {price_dye}\nстоимость работы - {cost_work}\nобщая стоимость малярных работ - {sum}')
#
#     area = int(input('Ввыедите площадь окрашиваемой стены: '))
#     price = int(input('Введите цену 5-литровой емкости краски:'))
#     sum_result(area, price)
#
#
# main()


# Месячяный налог с продаж. Розничная компания должна зарегистрировать отчет о месячном налоге с продаж с указанием
# общего налога с продаж за месяц и взимаемывх сукмм муниципального и федерального налогов с продаж.
# Федеральный налог с продаж составляет 5%, муниципальный налог с продаж - 2,5%. Напишите программу, которая просит
# пользователя ввести общий объем продаж за месяц.
# Из этого значения приложение должно рассчитать и показать:
# - сумму муниципального налога с продаж;
# - сумму федерального налога с продаж;
# - общий налог с продаж (муниципальный плюс федеральный)
# def main():
#     def tax(sum):
#         sum_municipal = sum * MUNICIPAL_TAX
#         sum_federal = sum * FEDERAL_TAX
#         print(
#             f'Сумма муниципального налога с продаж - {sum_municipal}\nСумма федерального налога с продаж - {sum_federal}\
#         \nОбщий налог с продаж (муниципальный и федеральный) - {sum_federal + sum_municipal}')
#
#     MUNICIPAL_TAX = 0.025
#     FEDERAL_TAX = 0.05
#     num = int(input('Введите общий объем продаж за месяц: '))
#     tax(num)
#
#
# main()


# Футы и дюймы. Один фут равняется 12 дюймам. Напишите функцию feet_to_inches, которая в качестве аргумента принимает
# количество футов и возвращает количество дюймов в этом количестве футов.
# Примените эту функцию в программе, которая предлагает пользователю ввести количество футов и затем показывает
# количество дюймов в этом количестве футов.
# def main():
#     def feet_to_inches(feet):
#         CONST_INCHES = 12
#         inches = feet * CONST_INCHES
#         print(f'{feet} футов - это {inches} дюймов')
#
#     value = int(input('Введите количество футов: '))
#     feet_to_inches(value)
#
#
# main()


# Математический тест. Напишите программу, которая позволяет проводить простые математические тесты. Она должна
# показать два случайных числа, которые должны быть проссумированы вот так:
#  245
# +129
# Эта программа должна давать обучаемому возможность вводить ответ. Если ответ правильный, то должно быть показано
# подздравительное сообщение. Если ответ неправилный, то должно быть показано сообщение с правильным ответом.
# import random
#
#
# def main():
#     def examination(num1, num2, result):
#         res = int(input('Введите Ваш вариант ответа: '))
#         if res == result:
#             print('Поздравляю, Вы правильно ответили!!!')
#         else:
#             print(f'Ответ не верный, правильный ответ - {result}')
#
#     val1 = random.randint(100, 1000)
#     val2 = random.randint(100, 1000)
#     q = int(len(str(val2)))
#     print(f'{val1:>{q + 3}}\n+  {val2}')
#     sum = val1 + val2
#     examination(val1, val2, sum)
#
#
# main()


# Максимальное из двух значений. Напишите функцию max, которая в качестве аргументов принимает два целочисленных
# значения и возвращает значение, которое является бОльшим из двух. Например, если в качестве аргументов переданы
# 7 и 12, то функция должна вернуть 12. Примение функцию в программе, которая предлагает пользователю
# ввести два целочисленных значения. Программа должна показать большее значение из двух.
# def main():
#     def max():
#         val1 = int(input('Введите первое число: '))
#         val2 = int(input('Введите второе число: '))
#         if val1 > val2:
#             return val1
#         else:
#             return val2
#
#     max_value = max()
#     print(f'Большее число - {max_value}')
#
#
# main()


# Высота падения. При падении тела под действием силы тяжести для определения расстояния, которое тело пролетит за
# определенное время, применяется формула:
# d=1/2gt^2, где d - расстояние, м; g=9.8м/с^2; t - время падения тела, с.
# Напишите функцию falling_distance, которая в качестве аргумента принимает время падения тела (в секундах).
# Функция должна вернуть расстояние в метрах, которе тело пролетело в течение этого времени. Напишите программу,
# которая вызывает эту функцию в цикле, передает значения от 1 до 10 в качестве аргументов и
# показыавет возвращаемое значение.
# def main():
#     TIME = 10
#     g = 9.8
#
#     def falling_distance(second):
#         d = 1 / 2 * g * second ** 2
#         return d
#
#     for i in range(1, TIME + 1):
#         print(f'За {i} секунд, тело упадет на {falling_distance(i):.2f} метров.')
#
#
# main()


# Кинетическая энергия. Из физики известно, что движущееся тело имеет кинетическую энергию. Приведенная ниже формула
# может использоваться для определения кинетичской энергии движущегося тела:
# Ke=1/2mv^2, где Ke - это кинетическая энергия; m - масса тела, кг; v - скорость тела, м/с.
# Напишите функцию kinetic_energy, которая в качесвте аргументов принимает массу тела (в килограммах) и его
# скорость (в метрах в секунду).
# Данная функция должна вевнуть величину кинетической энергии этого тела. Напишите программу, которая
# просит пользователя ввести значения массы и скорости, а затем вызывает фнукцию
# kinetic_energy, чтобы получить кинетическую энергию тела.
# def main():
#     def kinetic_energy(weight, speed):
#         k = 1 / 2 * weight * speed ** 2
#         return k
#
#     m = int(input('Введите массу тела в кг: '))
#     v = int(input('Введите скорость в м/с: '))
#     result = kinetic_energy(m, v)
#     print(f'Кинетическая энергия равна - {result}')
#
#
# main()


# Написать код, который выводит числа от 0 до 1000, которые делятся на 3, но не делятся на 5, и сумма цифр меньше десяти.
# for i in range(1001):
#     if i % 3 == 0 and i % 5 != 0:
#         s = str(i)
#         sum = 0
#         for j in s:
#             sum += int(j)
#         if sum < 10:
#             print(i, end=' ')

# Дана строка s, состоящая из слов и пробелов. Вернуть длину последнего слова в строке.
# s = 'esre  erwt er eter rty r6tyu65y4 df 1234p'
# print(s)
# count = 0
# for i in s:
#     if i != ' ':
#         count += 1
#     else:
#         count = 0
# print(count)


# Перевод из римских цифр в арабские
# например: XIV -> 14
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].
def main():
    def sum_roman(str_number):
        sum = 0
        xxx = {'I':1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        print(xxx['I'])

        # for i in range(len(str_number)):
        #     if

        return sum

    def input_validation():
        ls = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        valid = True
        # val = input('Введите римские цифры: ')
        while valid:
            valid = False
            val = input('Введите римские цифры: ')
            for i in val:
                if not i in ls:
                    valid = True
            if valid: print('Некорректный ввод, попробуйте еще раз: ')
            else: return val


    roman_numerals = input_validation()

    sum = sum_roman(roman_numerals)

    print(f'{roman_numerals} --> {sum}')

main()

# Даны три отсортированных массива, одинаковой длины. Найти и вывести одинаковые элементы
# a = [1, 2, 3, 4, 5]
# b = [3, 4, 5, 6, 7]
# c = [4, 5, 6, 7, 8]
# d = []
# for i in a:
#     if i in b and i in c:
#         d.append(i)

# print(d)