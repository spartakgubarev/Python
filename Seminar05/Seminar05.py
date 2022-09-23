# Дискорд: http://discord.gg/cJvrFc2w
# **********************
# 1. В файле находятся N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# Например: [1, 2, 3, 5] -> пропущен число 4
# path = 'G:/Учеба/Разработчик/repo/Python/Seminar05/text.txt'
# file = open(path, 'r')
# data = file.read() + ' '
# file.close()

# numbers = []
# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos + 1:]

# for x in range(1, len(numbers)):
#     if numbers[x] != numbers[x-1]+1:
#         find = numbers[x] - 1
# print(f'{numbers} --> пропущено число {find}')

# **********************
# 2. Дан список чисел. Создайте список, в который попадают числа, описываемые
# возрастающую последовательность. Порядок элементов менять нельзя.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] и т.д.
path = 'G:/Учеба/Разработчик/repo/Python/Seminar05/Text_Task02.txt'
file = open(path, 'r')
data = file.read()
file.close()

numbers = data.split()
numbers = [int(x) for x in numbers]
list = [numbers[0]]
find = numbers[0]
for i in numbers:
    if find < i:
        find = i
        list.append(find)

print(f'{numbers} => {list}')


# **********************
# 3. Напишите программу, удалающую из текста все слова, содержащие "абв".
