# lambda Лямда функция (если код нужно выполнить всего один раз)
# def f(x):
#     return x**2
# g = f
# print(type(f))
# print(type(g))
# print(f(2))
# print(g(2))

# def math(op, x): # Создал ф-ию math в которой создал функцию и передал x
#     print(op(x))

# math(f, 5) # вызвал ф-ию и передал ей функцию f со значение 5

# def sum(x, y):
#     return x+y

# sum = lambda x, y: x + y # то же самое что и функция sum выше ЛЯМБДА

# def mylt(x, y):
#     return x*y

# def calc(op, a, b):
#     print(op(a, b))
#     # return op(a, b)

# calc(sum, 4, 5)

# # List Comprehension
# list = []
# for i in range(1, 21):
#     # if i%2 == 0:
#     list.append(i)
# print(list)

# def f(x):
#     return x**3

# list = [f(i) for i in range(1, 21) if i % 2 == 0] # списки
# print(list)

# list = [(i, f(i))  for i in range(1, 21) if i % 2 == 0] # кортежи
# print(list)

# ***************
# Есть список 1 2 3 5 8 15 23 38, Получить: # [(2, 4), (8, 64), (38, 144)]
# path = 'G:/Учеба/Разработчик/repo/Python/Lecture03/text.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# print(data)
# f.close()

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos +1:]

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e **2))
# print(out)

# ***************
# sum = lambda x: x**2
# list = [1, 2, 3, 5, 8, 15, 23, 38]
# list_sum = [(i,sum(i)) for i in list if i%2 == 0]
# print(list_sum)


# ***************
# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = select(int, data)
# res = where(lambda x: not  x % 2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)


# map ******************** map
# li = [x for x in range(1, 21)]
# li = list(map(lambda x: (x, x+10), li))
# print(li)

# data = list(map(int, input().split()))
# print(data)


# data = map(int, '1 2 3 23 12 12'.split())

# for e in data: 
#     print(e*10)


# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = where(lambda x: not  x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)


# filter **************
data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data)
res = filter(lambda x: not  x % 2, res)
res = list(map(lambda x: (x, x**2), res))
print(res)

