def number_request():
    return int(input('Введите число: '))

def operation_request():
    return input('Введите действие (+, -, *, /): ')

def output(a, b, operation, result):
    print(f'{a} {operation} {b} = {result}')