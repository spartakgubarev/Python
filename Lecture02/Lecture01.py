# Файлы
# Как работать с файлами: Связать файловую переменную с файлом, определив модификатор работы
# a - открытие для добавления данных (если нечего открывать, создаст новый)
# r - открытие для чтения данных
# w - открытие для запси данных
# w+, r+

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors)  # разделителей не будет
# data.close()

# with open('file.txt', 'a') as data:
#     data.write('line 123\n')
#     data.write('line 2345\n')


# Чтение данных из файла
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close
# exit()      # после этой команды код не будет выполнять никакой!!!

# ФУНКЦИИ
# def function_name (x):
#     body line 1
#     ...
#     body line
#     optional return

# import lec as abrakadabra
# print(abrakadabra.f(1))

# def new_string(symbol, count):
#   return symbol * count
# print(new_string('!', 5))     # !!!!!
# print(new_string('!'))        # TypeError missing 1 required...

# def new_string(symbol, count = 3):
#   return symbol * count
# print(new_string('!', 5))     # !!!!!
# print(new_string('!'))        # !!!
# print(new_string(4))          # 12

# def concatenatio(*params):       # * звездочка показывает что параметров может быть сколько угодно
#     res: str = ""                # res - переменная, : str - тип данных
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w'))     # asdw
# print(concatenatio('a', '1', 'd', '2'))     # a1d2
# print(concatenatio(1, 2, 3, 4))             # TypeError...

# РЕКУРСИЯ
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)


# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)     # 1 1 2 3 5 8 13 21 34

# КОРТЕЖИ
# Кортеж - это неизменяемый "список"
# t = ()
# print(type(t))          # tuple
# t = (1, )
# print(type(t))          # tuple
# t = (1)
# print(type(t))          # int
# t = (28, 9, 1990)
# print(type(t))          # tuple
# colors = ('red', 'green', 'blue')
# t = tuple(colors)
# print(t)          # ('red', 'green', 'blue')

# в картедже нельзя присвоить значение элементов как например в списке a[0] = 3 - будет ОШИБКА
# если записать что а = (3) - это будет число
# нужно записать а = (3, ) - тогда будет картедж
# a = (3, 1, 41, 4)
# print(a)
# print(a[-2])
# кортежи можно с for использовать

# СЛОВАРИ
# Неупорядоченные коллекции произвольных объектов с доступом по ключу
# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# print(dictionary)  # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary['left'])   # ←
# типы ключей могут отличаться
# \ {  ..} - слеш и фигурные скобки чтоб удобней описание было
# for k in dictionary.keys(): # - показать все ключи
#     print(k)

# for k in dictionary.values(): # - показать все значения
#     print(k)

# МНОЖЕСТВА

colors = {'red', 'green', 'blue'}
print(type(colors)) # тип данный set - множества
print(colors) # тип данный set - множества
colors.add('red') # не добавит, т.к. есть элемент
print(colors) # тип данный set - множества
colors.add('grey') # добавит элемент в конец
print(colors) # тип данный set - множества
colors.remove('red') # удалит, если элемента нет, будет ошибка
colors.discard('blue') # удалит blue, если нет, то ошибки не будет
print(colors) # тип данный set - множества
colors.clear() # { } очистить множества
print(colors) # тип данный set - множества
