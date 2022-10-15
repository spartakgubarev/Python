def result(x, y, sign):
    if sign == '*':
        res = multiplication(x, y)
    elif sign == '/':
        res = division(x, y)
    elif sign == '+':
        res = sum(x, y)
    elif sign == '-':
        res = difference(x, y)
    return res

def sum(x, y):
    return str(x + y)

def difference(x, y):
    return str(x - y)

def multiplication(x, y):
    return str(x * y)

def division(x, y):
    return str(x / y)
