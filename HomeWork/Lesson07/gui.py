import db

def read_write():
    return int(input('Что делаем? (1 - ищем, 2 - записываем, 3 - изменяем, 4 - выход): '))

def write_f():
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    tel_number = input('Введите телефон в формате (89211234567): ')
    description = input('Введите описание: ')
    return first_name,last_name,tel_number,description

def read_f():
    return input('Что ищем? (введите имя, фамилию, телефон или описание: ')


def rewrite_f():
    pass
