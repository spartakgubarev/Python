# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +, -, /, *. Приоритет операций стандартный.
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => 5.
# - добавьте возможность использования скобок, меняющих приоритет операций.
# Пример: 1+2*3 => 7; (1+2)*3 => 9.
# import main


# main.main()

# # 2. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# # Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
arr = [1, 2, 3, 5, 1, 5, 3, 10]
# num = [arr[n] for n in range(len(arr)) if arr[n] not in arr[n+1:] and arr[n] not in arr[:n]]
num = [i for i in arr if arr.count(i) == 1]
print(arr)
print(num)
