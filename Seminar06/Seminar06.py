# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +, -, /, *. Приоритет операций стандартный.
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => 5.
# - добавьте возможность использования скобок, меняющих приоритет операций.
# Пример: 1+2*3 => 7; (1+2)*3 => 9.
# text = input('Введите арифметическое выражение используя +, -, /, *: ')
# def calculations(find_actions, sign):
#     while sign in find_actions:
#         find_index = find_actions.find(sign)
#         i = find_index
#         min_index = 0
#         max_index = 0

#         while i > 0 and find_actions[i-1] >= '0' and find_actions[i-1] <= '9' or find_actions[i-1] == '.':
#             i -= 1
#         min_index = i
#         i = find_index
#         print(find_actions)
#         while i+1 < len(find_actions)-1 and find_actions[i+1] >= '0' and find_actions[i+1] <= '9' or find_actions[i+1] == '.':
#             i += 1
#         max_index = i
#         first_value = float(find_actions[min_index:find_index])
#         second_value = float(find_actions[find_index+1:max_index+1])

#         if sign == '*':
#             result = first_value * second_value
#         if sign == '/':
#             result = first_value / second_value
#         if sign == '+':
#             result = first_value + second_value
#         if sign == '-':
#             result = first_value - second_value
#         # print(find_actions)
#         # result = int(find_actions[min_index:find_index]) + int(find_actions[find_index+1:max_index+1])
#         find_actions = find_actions.replace(find_actions[min_index:max_index+1], str(result))
#         # print(find_actions)
#         # print(find_actions[min_index:max_index+1])
#         # print(find_actions)

#     return find_actions

# FIND = "*/+-"
# text = '4+3+5*6+6-4/2+6*4+2+1'
# find_text = text
# print(find_text)
# for i in FIND:
#     find_text = calculations(find_text, i)
#     print(find_text)

# # 2. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# # Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

