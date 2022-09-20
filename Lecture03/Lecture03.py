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

list = [i for i in range(1, 21)]
