#************
# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.
def int_number_str(number):
    list = []
    for i in number:
        list.append(int(i))
    return list


number_str = input('Введите числа разделяя пробелом: ').split()
list = int_number_str(number_str)
print(f'список {list} min = {min(list)}, max = {max(list)}')

#************
# # 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python
# abc = input('Введите значения квадратного уравнения через пробел, a= b= c= : ').split()
# list_abc = int_number_str(abc)
# print(list_abc)


#************
# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# Ответ записать в файл.