# 1.расчитать НОД двух чисел(быстрый и медленный способ)
# def multipliers(x):
#     list = []
#     count = 2
#     while x != 1:
#         if x % count == 0:
#             list.append(count)
#             x /= count
#             count = 2
#         else:
#             count += 1
#     return list


# val1 = int(input('Введите первое число: '))
# val2 = int(input('Введите второе число: '))

# list1 = multipliers(val1)
# list2 = multipliers(val2)
# list = []
# result = 1

# if len(list1) > len(list2):
#     list1, list2 = list2, list1

# print(list1, list2)
# for i in list1:
#     if i in list2:
#         list.append(i)
#         list2.remove(i)

# for i in list:
#     result *= i

# print(list)
# print(result)
# ********************* быстрый способ***************
# val1 = int(input('Введите первое число: '))
# val2 = int(input('Введите второе число: '))

# min_val = min(val1, val2)
# max_val = max(val1, val2)

# ls = []

# if max_val % min_val == 0:
#     ls.append(min_val)
# else:
#     ost = max_val % min_val
#     while ost != 0:
#         ls.append(ost)
#         temp = ost
#         ost = min_val % ost
#         min_val = temp
# print(ls[-1])


# 2.Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "plr". То есть,
# функция должна возвращать True, если такой фрагмент присутствует в строке и False - в противном случае.
# str_txt = 'asferge rthryjeg g3tq4 sdrty jfhplryh '
# result = lambda x: 'plr' in x
# print(result(str_txt))


# 3.Вводится список в виде вещественных чисел в одну строку через пробел. Сначала нужно сформировать список из введенной строки.
#  Затем, все отрицательные значения в этом списке заменить на -1.0. Результат вывести на экран в виде строки чисел через пробел.
#  Программу следует реализовать с использованием функции enumerate.
# text = '1 2 3 -1 -25.25 23.3 -4 -5.21'
# text = input('Введите список вещественных чисел через пробел: ')
# ls = text.split()
# print(ls)
# ls = list(map(float, ls))
# print(ls)
# for id, txt in enumerate(ls):
#     if txt < 0:
#         ls[id] = -1.0
# print(ls)


# 4.Саша и Галя коллекционируют монетки. Каждый из них решил записать номиналы монеток из своей коллекции.
#  Получилось два списка. Эти списки поступают на вход программы в виде двух строк из целых чисел, записанных через пробел.
#  Необходимо выделить значения, присутствующие в обоих списках и оставить среди них только четные.
#  Результат вывести на экран в виде строки полученных чисел в порядке их возрастания через пробел.
# При реализации программы используйте функцию filter и кое-что еще (для упрощения программы), подумайте что.
# sasha = '6 8 3 11 4 5 12 7 2 1'
# galya = '6 7 12 2 3 4 5 99 11 45'
# sa_ls = list(map(int, sasha.split()))
# ga_ls = list(map(int, galya.split()))
# print(sa_ls)
# print(ga_ls)
# ls = list(filter(lambda x: x in ga_ls and x % 2 == 0, sa_ls))
# # ls = [i for i in sa_ls if i in ga_ls and i % 2 == 0]
# print(ls)
# [print(i, end=' ') for i in sorted(ls)]


# 5.Напишите программу, удаляющую из текста все слова, содержащие "абв".
s = ''
find_txt = 'абв'
text = 'вкапеабвукапетыувкпе спарта выабввап уке кабвуерап сделал укабвпто программу р45абвн5кноыварп'
lis = text.split()
print(lis)
res = list(filter(lambda x: not find_txt in x, lis))
# res = [i for i in list if not find_txt in i]
print(res)
s = ' '.join(res)
print(s)
