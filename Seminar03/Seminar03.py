# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
import time
def rnd():
    str_list = input(
        'Введите диапозон случайных чисел через пробел, пример: [1 10]: ').split(sep=' ')
    int_list = [int(x) for x in str_list]
    # str_list = ['50', '1000']
    # int_list = [50, 1000]
    b = True
    find = ''
    while b:
        if len(find) > len(str(1)):
            find = ''
        sec = time.time()
        time.sleep(1/int(str(sec)[-4:]))
        find += str(sec)[-2]             # предпоследний символ чтобы нуль включался тоже, иначе ноль обрезается
        if int(str(sec)[-1]) > 5:
            find += str(sec)[-2]
        if int_list[0] < int(find) < int_list[1]:
            b = False
    return find
rnd_rnd = int(rnd())
print(rnd_rnd)

 
# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['efg23'. '79234gefg', 'sdgs', 'g53']
# '2
# ['efg23', '79234gefg']

# 3. Напишите программу, которая определит позицию второго вхождения строки в списке, либо сообщит, что ее нет.
# Пример:
# список ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список [], ищем: "123" ответ: -1
