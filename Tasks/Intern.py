## Почувствуй себя интерном*
#  0. Вывести квадрат числа
# def main():
#     value = int(input('Введите число: '))
#     square = value ** 2
#     print(f'Квадрат числп {value} равен - {square}')
# main()


#  1. По двум заданным числам проверять является ли первое квадратом второго
# def main():
#     def number_int():
#         while True:
#             num = input()
#             if num.isdigit():
#                 return int(num)
#             print('Введенное значение не число, попробуйте еще раз: ')
#     print('Введите первое число: ', end='')
#     number1 = number_int()
#     print('Введите второе число: ', end='')
#     number2 = number_int()
#     if number1 ** 2 == number2:
#         print(f'Первое число {number1} является квадратом второго числа {number2}')
#     else:
#         print(f'Первое число {number1} не является квадратом второго числа {number2}')
# main()


#  2. Даны два числа. Показать большее и меньшее число
# def main():
#     def examination():
#         while True:
#             num = input()
#             if num.isdigit():
#                 return int(num)
#             print('Ввели не число, попробуйте еще раз: ')
#     print('Программа покажет большее и меньшее число.')
#     print('Введите первое число:', end='')
#     val1 = examination()
#     print('Введите второе число:', end='')
#     val2 = examination()
#     val_max = max(val1, val2)
#     val_min = min(val1, val2)
#     print(f'Большее число - {val_max}, меньшее числое - {val_min}')
# main()


#  3. По заданному номеру дня недели вывести его название
def main():
    def examination_days(val):
        if val == 1: return 'понедельник'
        elif val == 2: return 'вторник'
        elif val == 3: return 'среда'
        elif val == 4: return 'четверг'
        elif val == 5: return 'пятница'
        elif val == 6: return 'суббота'
        elif val == 7: return 'воскресенье'
        return 'такой недели не существует :-)'
    def examination_integer():
        while True:
            num = input()
            if num.isdigit():
                return int(num)
            print('Введенное значение не является числом, попробуйте еще раз:')
    print('Введите номер дня недели, я выведу название: ', end='')
    day = examination_integer()
    print(examination_days(day))
main()


#  4. Найти максимальное из трех чисел
#  5. Написать программу вычисления значения функции y = f(a)
#  6. Выяснить является ли число чётным
#  7. Показать числа от -N до N
#  8. Показать четные числа от 1 до N
#  9. Показать последнюю цифру трёхзначного числа
# 10. Показать вторую цифру трёхзначного числа
# 11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа
# 12. Удалить вторую цифру трёхзначного числа
# 13. Выяснить, кратно ли число заданному, если нет, вывести остаток.
# 14. Найти третью цифру числа или сообщить, что её нет