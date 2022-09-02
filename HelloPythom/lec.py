# print('Hello World!')
# # - комментарий
# value = None

# a = 123
# b = 1.987
# print(type(a))  # type(a) указывает тип данный переменной a
# print(b)

# value = 555
# print(value)
# s = 'Hello \nWorld'  # - \n переход на новую строку
# print(s)

# print(a, '-', b, s)

# print('{} - {} - {}'.format(a, b, s))
# print(f'{a} - {b} - {s}')
# print('{2} - {1} - {0}'.format(a, b, s))

# f = True
# print(f)

# list = []  # - объявить список пустой, но можно и сразу с данными

# # тип может быть любой, но не стоит так делать
# list = [1, 2, 3, 'Hello World!', True]
# print(list)

# print('Введите a')
# # float () - переводит из строки в число вещественное (5,2) (иначе будет склеивание!!!)
# a = float(input())
# print('Введите b')
# b = float(input())
# print(a, '+', b, '=', a+b)
# print('{1} - {0}'.format(a, b))
# print(f'{a} - {b}')

# # / - деление вещественных чисел с остатком, // - деление целых чисел без остатка
# # % - получить остаток от деления
# # ** - возведение в степень
# # при умножении целого числа на вещественное может быть ерунда например 3*1.3
# # для исправления нужно округлить round(a *b,4) - 4 это сколько чисел после запятой
# a = 12
# b = 8
# c = a/b
# d = a//b
# print(c)
# print(d)


# # логические операции
# a = 1 < 4 and 5 > 2
# print(a)  # - будет True

# a = 1 > 4 or 5 > 2
# print(a)  # - будет True

# f = [1, 2, 3, 4]
# print(f)
# print(2 in f)  # True
# print(not 2 in f)  # False

# # - проверка остатка от деления на 2 из списка первого элемента с остатком 0
# is_odd = f[0] % 2 == 0
# print(is_odd)


# # нахождение максимального из двух чисел
# a = int(input('a='))
# b = int(input('b='))
# if a > b:
#     print(a)
# else:
#     print(b)

# # if - оператор если
# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет, ', username)

# # циклы While, For
# original = 123456789
# inverted = 0
# while original != 0:
#     inverted = inverted*10+(original % 10)
#     original //= 10
#     print(inverted)

# original = 234567
# inverted = 0
# while original !=0:
#     inverted = inverted*10+(original%10)
#     original //=10
# else:
#     print ('Пожалуй')
#     print ('хватит')
# print(inverted)
