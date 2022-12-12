# Урок 1. Знакомство с Python
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
# def correctness(day):
#     if day.isdigit():
#         day = int(day)
#         if day >= 1 and day <= 5:
#             print(f'{day} -> нет')
#         elif day == 6 or day == 7:
#             print(f'{day} -> да')
#     else:
#         print('Некорректные данные')

# week = input('Введите день недели: ')
# correctness(week)


# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) для всех значений предикат.
# VAL = range(2)
# for x in VAL:
#     for y in VAL:
#         for z in VAL:
#             a = not(x or y or z)
#             b = not(x) and not(y) and not(z)
#             print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z}  --> {a == b}')


# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка .
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
# def correctness():  # проверка корректности ввода данных
#     while True:
#         number = input()
#         if number.isdigit() or number[0]=='-' and number[1:].isdigit(): # доп проверка на знак "-" и символы после него
#             num = int(number)
#             if num != 0:
#                 return num
#         print('Не корректные данные!\nЕще раз:', end='')

# def quarter(x, y):  # поиск в какой четверти находится точка
#     if x > 0 and y > 0:
#         print(f'x={x}; y={y} --> 1')
#     elif x > 0 and y < 0:
#         print(f'x={x}; y={y} --> 4')
#     elif x < 0 and y > 0:
#         print(f'x={x}; y={y} --> 2')
#     elif x < 0 and y < 0:
#         print(f'x={x}; y={y} --> 3')

# print('Введите координаты точки (X, Y), причем X и Y не равын 0')
# print('Введите X:')
# x = correctness()
# print('Введите Y:')
# y = correctness()
# quarter(x, y)

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# def correctness():
#     while True:
#         val = input('Введите номер четверти от 1 до 4: ')
#         if val.isdigit():
#             val = int(val)
#             if val >= 1 and val <= 4:
#                 return val
#         print('Неверные данные!!!')

# def value_output(val):
#     if val == 1: print('X(0;+oo) U Y(0;+oo)')
#     elif val == 2: print('X(0;-oo) U Y(0;+oo)')
#     elif val == 3: print('X(0;-oo) U Y(0;-oo)')
#     elif val == 4: print('X(0;+oo) U Y(0;-oo)')

# value = correctness()
# value_output(value)


# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
def correctness():
    while True:
        value = input()
        if value.isdigit() or (value[0] == '-' and value[1:].isdigit()):
            return int(value)
        print('Неверные данные, еще раз: ')

def hypotenuse(ax, ay, bx, by):
    c = ((ax - bx)**2 + (ay - by)**2)**0.5
    return c

print('Введите координаты точки А(x1, y1) x1=: ')
x1 = correctness()
print('Введите координаты точки А(x1, y1) y1=: ')
y1 = correctness()
print('Введите координаты точки B(x2, y2) x2=: ')
x2 = correctness()
print('Введите координаты точки B(x2, y2) x2=: ')
y2 = correctness()
c = hypotenuse(x1, y1, x2, y2)
print(f'A ({x1},{y1}); B({x2};{y2}) --> {c:.2f}')
