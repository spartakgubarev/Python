# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +, -, /, *. Приоритет операций стандартный.
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => 5.
# - добавьте возможность использования скобок, меняющих приоритет операций.
# Пример: 1+2*3 => 7; (1+2)*3 => 9.
# text = input('Введите арифметическое выражение используя +, -, /, *: ')
def multiplication(find_mult):
    start_index = 0
    end_index = 0

FIND = '*/+-'
text = '5*6+6-4/2+6*4'
find_text = ''

multiplication = text.find('*')
index = multiplication + 1
first_act = ''
while text[index] >= '0' and text[index] <= '9':
    first_act += text[index]
    index += 1
print(first_act)
for i in FIND:
    if i in text:
        find_text = multiplication(text)

# 2. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

