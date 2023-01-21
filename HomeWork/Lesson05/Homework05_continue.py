# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension


#*******************************   LAMBDA, FILTER  *********************************** Это было сделано в домашке пятого семинара
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# def read_file(path_doc):
#     with open(path_doc, 'r', encoding="utf-8") as d:
#         return d.read()


# def find_text(find, txt):
#     b = filter(lambda a: not find in a, txt.split())
#     return ' '.join(b)


# def save_text(path, txt):
#     with open(path, 'a', encoding="utf-8") as s:
#         s.write(txt)


# path = 'G:/Учеба/Разработчик/repo/Python/HomeWork/Lesson05/abv.txt'
# path_save = 'G:/Учеба/Разработчик/repo/Python/HomeWork/Lesson05/abv_new.txt'
# find_txt = 'абв'
# text = read_file(path)
# new_text = find_text(find_txt, text)
# save_text(path_save, new_text)





#******************   ENUMERATE, LIST  COMPREHENSION  ***********************
# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности. [8, 7, 6, 1, 2, 4, 1, 5, 6, 7, 9, 8, 1, 3, 4] -> [2, 5, 9, 3]
# new_list = [8, 7, 6, 1, 2, 4, 1, 5, 6, 7, 9, 8, 1, 3, 4]
# print(new_list)
# list = [y for x, y in enumerate(new_list) if not y in new_list[x+1:] and not y in new_list[:x]]
# print(list)





#********************************   MAP   ************************************

# number_str = input('Введите числа разделяя пробелом: ').split()
# a = list(map(int, number_str))
# print(max(a), min(a))
